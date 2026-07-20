"""SDK 异常类型。"""

from __future__ import annotations


class MairuiAPIError(Exception):
    """麦蕊 API SDK 基类异常。"""


class MairuiAuthError(MairuiAPIError):
    """证书无效、未授权或鉴权失败（常见 HTTP 401/403）。"""


class MairuiHTTPError(MairuiAPIError):
    """非成功 HTTP 状态或业务错误体。"""

    def __init__(self, message: str, *, status_code: int | None = None, payload=None):
        super().__init__(message)
        self.status_code = status_code
        self.payload = payload


class MairuiTimeoutError(MairuiAPIError):
    """请求超时。"""
