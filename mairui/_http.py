"""HTTP 会话：连接池、超时、有限重试。"""

from __future__ import annotations

import time
from typing import Any, Mapping, MutableMapping, Optional
from urllib.parse import quote

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from mairui.exceptions import (
    MairuiAuthError,
    MairuiHTTPError,
    MairuiTimeoutError,
)

DEFAULT_BASE_URL = "https://api.mairuiapi.com"
DEFAULT_TIMEOUT = (5.0, 60.0)  # connect, read
DEFAULT_UA = "mairui-python/1.0 (+https://www.mairuiapi.com)"


def quote_path(segment: str) -> str:
    """路径段编码（保留常见股票代码字符）。"""
    return quote(str(segment).strip(), safe=".-_")


def build_query(
    *,
    st: Optional[str] = None,
    et: Optional[str] = None,
    lt: Optional[int] = None,
    extra: Optional[Mapping[str, Any]] = None,
) -> dict[str, Any]:
    q: dict[str, Any] = {}
    if st is not None and str(st).strip() != "":
        q["st"] = str(st).strip()
    if et is not None and str(et).strip() != "":
        q["et"] = str(et).strip()
    if lt is not None:
        q["lt"] = int(lt)
    if extra:
        for k, v in extra.items():
            if v is None:
                continue
            q[k] = v
    return q


class HttpTransport:
    def __init__(
        self,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float | tuple[float, float] = DEFAULT_TIMEOUT,
        max_retries: int = 3,
        pool_connections: int = 32,
        pool_maxsize: int = 64,
        headers: Optional[Mapping[str, str]] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._owns_session = session is None
        self.session = session or requests.Session()

        retry_kwargs = dict(
            total=max_retries,
            connect=max_retries,
            read=max_retries,
            status=max_retries,
            backoff_factor=0.4,
            status_forcelist=(429, 502, 503, 504),
            raise_on_status=False,
        )
        # urllib3>=1.26 用 allowed_methods；更旧版本用 method_whitelist
        try:
            retry = Retry(allowed_methods=frozenset(["GET"]), **retry_kwargs)
        except TypeError:
            retry = Retry(method_whitelist=frozenset(["GET"]), **retry_kwargs)
        adapter = HTTPAdapter(
            max_retries=retry,
            pool_connections=pool_connections,
            pool_maxsize=pool_maxsize,
        )
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

        # Accept-Encoding 交由 requests 默认处理并自动解压；勿在 Session 上硬编码后
        # 再配合关闭解压的自定义适配器，否则会出现 gzip 二进制「乱码」。
        default_headers: MutableMapping[str, str] = {
            "User-Agent": DEFAULT_UA,
            "Accept": "application/json, text/plain, */*",
            "Connection": "keep-alive",
        }
        if headers:
            default_headers.update(headers)
        self.session.headers.update(default_headers)

    def close(self) -> None:
        if self._owns_session:
            self.session.close()

    def get_json(
        self,
        path: str,
        *,
        params: Optional[Mapping[str, Any]] = None,
        timeout: float | tuple[float, float] | None = None,
    ) -> Any:
        if not path.startswith("/"):
            path = "/" + path
        url = f"{self.base_url}{path}"
        t0 = time.perf_counter()
        try:
            resp = self.session.get(url, params=params or None, timeout=timeout or self.timeout)
        except requests.Timeout as e:
            raise MairuiTimeoutError(f"请求超时: {url}") from e
        except requests.RequestException as e:
            raise MairuiHTTPError(f"网络错误: {e}") from e

        elapsed_ms = (time.perf_counter() - t0) * 1000.0
        if resp.status_code in (401, 403):
            raise MairuiAuthError(
                f"鉴权失败 HTTP {resp.status_code}: 请检查 licence 是否有效 / 是否欠费限流"
            )
        if resp.status_code == 404:
            raise MairuiHTTPError(
                f"资源不存在 HTTP 404: {url}",
                status_code=404,
                payload=_safe_json(resp),
            )
        if resp.status_code >= 400:
            raise MairuiHTTPError(
                f"HTTP {resp.status_code}: {url} ({elapsed_ms:.0f}ms)",
                status_code=resp.status_code,
                payload=_safe_json(resp),
            )
        return _decode_body(resp)


def _safe_json(resp: requests.Response) -> Any:
    try:
        return resp.json()
    except Exception:
        text = (resp.text or "")[:500]
        return text


def _decode_body(resp: requests.Response) -> Any:
    ctype = (resp.headers.get("Content-Type") or "").lower()
    if "json" in ctype or not ctype:
        try:
            return resp.json()
        except Exception:
            pass
    text = resp.text
    # 少数接口可能返回纯文本
    return text
