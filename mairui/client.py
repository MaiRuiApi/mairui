"""麦蕊 Client：绑定 licence 后调用官网公开接口。"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Callable, Iterable, List, Mapping, Optional, Sequence, TypeVar

from mairui._http import (
    DEFAULT_BASE_URL,
    DEFAULT_TIMEOUT,
    HttpTransport,
    build_query,
    quote_path,
)
from mairui.exceptions import MairuiAPIError

T = TypeVar("T")

FINANCIAL_TABLES = (
    "balance",
    "income",
    "cashflow",
    "pershareindex",
    "capital",
    "hm",
    "topholder",
    "flowholder",
)

INDICATORS = ("macd", "ma", "boll", "kdj")

POOL_TYPES = ("ztgc", "dtgc", "qsgc", "cxgc", "zbgc")

HSCP_SLUGS = (
    "gsjj",
    "sszs",
    "ljds",
    "ljgg",
    "ljjj",
    "sdgd",
    "ltgd",
    "gdbh",
    "jnfh",
    "jnzf",
    "jjxs",
    "jjcg",
    "yjyg",
    "cwzb",
    "jdlr",
    "jdxj",
)


class Client:
    """
    麦蕊行情 API 客户端。

    用法::

        from mairui import Client

        api = Client(licence="YOUR-LICENCE-UUID")
        rows = api.stock_history("000001.SZ", "d", "n", st="20240101", et="20241231")
        api.close()

    也支持 with::

        with Client(licence="...") as api:
            print(api.stock_list())
    """

    def __init__(
        self,
        licence: str,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float | tuple[float, float] = DEFAULT_TIMEOUT,
        max_retries: int = 3,
        pool_connections: int = 32,
        pool_maxsize: int = 64,
        headers: Optional[Mapping[str, str]] = None,
        session: Any = None,
    ) -> None:
        lic = (licence or "").strip()
        if not lic:
            raise MairuiAPIError("licence 不能为空")
        self.licence = lic
        self._http = HttpTransport(
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            pool_connections=pool_connections,
            pool_maxsize=pool_maxsize,
            headers=headers,
            session=session,
        )

    # ------------------------------------------------------------------ #
    # 生命周期
    # ------------------------------------------------------------------ #

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "Client":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def set_licence(self, licence: str) -> None:
        """运行时更换证书。"""
        lic = (licence or "").strip()
        if not lic:
            raise MairuiAPIError("licence 不能为空")
        self.licence = lic

    # ------------------------------------------------------------------ #
    # 内部
    # ------------------------------------------------------------------ #

    def _get(
        self,
        path_parts: Sequence[str],
        *,
        st: Optional[str] = None,
        et: Optional[str] = None,
        lt: Optional[int] = None,
        extra: Optional[Mapping[str, Any]] = None,
    ) -> Any:
        segs = [quote_path(p) for p in path_parts if p is not None and str(p) != ""]
        path = "/" + "/".join(segs)
        params = build_query(st=st, et=et, lt=lt, extra=extra)
        return self._http.get_json(path, params=params or None)

    def _lic(self, *parts: str) -> List[str]:
        return [*(str(p) for p in parts), self.licence]

    def map(
        self,
        fn: Callable[..., T],
        items: Iterable[Any],
        *,
        max_workers: int = 8,
        **kwargs: Any,
    ) -> List[T]:
        """
        并发对多只股票/参数调用同一函数（连接池复用，适合批量拉历史）。

        例::

            data = api.map(api.stock_history, ["000001.SZ", "600519.SH"],
                           period="d", dividend="n", st="20240101", lt=10)
        """
        items = list(items)
        if not items:
            return []
        workers = max(1, min(int(max_workers), len(items)))
        results: List[Optional[T]] = [None] * len(items)
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futs = {
                pool.submit(fn, item, **kwargs): i for i, item in enumerate(items)
            }
            for fut in as_completed(futs):
                i = futs[fut]
                results[i] = fut.result()
        return results  # type: ignore[return-value]

    # ================================================================== #
    # 沪深 A 股 — 股票列表
    # ================================================================== #

    def stock_list(self) -> Any:
        """股票列表 — GET /hslt/list/{licence}"""
        return self._get(self._lic("hslt", "list"))

    def new_stock_calendar(self) -> Any:
        """新股日历 — GET /hslt/new/{licence}"""
        return self._get(self._lic("hslt", "new"))

    def sectors_list(self) -> Any:
        """概念指数列表（券商数据）— GET /hslt/sectorslist/{licence}"""
        return self._get(self._lic("hslt", "sectorslist"))

    def primary_sectors_list(self) -> Any:
        """一级市场板块列表 — GET /hslt/primarylist/{licence}"""
        return self._get(self._lic("hslt", "primarylist"))

    def sector_detail(self, sector_name: str) -> Any:
        """板块明细列表 — GET /hslt/sectors/{name}/{licence}"""
        return self._get(self._lic("hslt", "sectors", sector_name))

    # ================================================================== #
    # 沪深 A 股 — 行情数据 / 技术指标
    # ================================================================== #

    def stock_history(
        self,
        code: str,
        period: str = "d",
        dividend: str = "n",
        *,
        st: Optional[str] = None,
        et: Optional[str] = None,
        lt: Optional[int] = None,
    ) -> Any:
        """历史分时交易 — /hsstock/history/{code}/{period}/{div}/{licence}"""
        return self._get(
            self._lic("hsstock", "history", code, period, dividend),
            st=st, et=et, lt=lt,
        )

    def stock_latest(
        self,
        code: str,
        period: str = "d",
        dividend: str = "n",
        *,
        lt: Optional[int] = None,
    ) -> Any:
        """最新分时交易 — /hsstock/latest/{code}/{period}/{div}/{licence}"""
        return self._get(
            self._lic("hsstock", "latest", code, period, dividend),
            lt=lt,
        )

    def stock_vip_history(
        self,
        code: str,
        period: str = "d",
        dividend: str = "n",
        *,
        st: Optional[str] = None,
        et: Optional[str] = None,
        lt: Optional[int] = None,
    ) -> Any:
        """企业版历史（含 1m 等）— /hsstock/vip/{code}/{period}/{div}/{licence}"""
        return self._get(
            self._lic("hsstock", "vip", code, period, dividend),
            st=st, et=et, lt=lt,
        )

    def stock_stopprice(
        self,
        code: str,
        *,
        st: Optional[str] = None,
        et: Optional[str] = None,
        lt: Optional[int] = None,
    ) -> Any:
        """历史涨跌停价格 — /hsstock/stopprice/history/{code}/{licence}"""
        return self._get(
            self._lic("hsstock", "stopprice", "history", code),
            st=st, et=et, lt=lt,
        )

    def stock_indicators(
        self,
        code: str,
        *,
        st: Optional[str] = None,
        et: Optional[str] = None,
        lt: Optional[int] = None,
    ) -> Any:
        """行情指标快照 — /hsstock/indicators/{code}/{licence}"""
        return self._get(
            self._lic("hsstock", "indicators", code),
            st=st, et=et, lt=lt,
        )

    def stock_indicator(
        self,
        indicator: str,
        code: str,
        period: str = "d",
        dividend: str = "n",
        *,
        st: Optional[str] = None,
        et: Optional[str] = None,
        lt: Optional[int] = None,
    ) -> Any:
        """历史技术指标 macd/ma/boll/kdj — /hsstock/history/{ind}/..."""
        ind = indicator.strip().lower()
        if ind not in INDICATORS:
            raise MairuiAPIError(f"indicator 须为 {INDICATORS}，收到: {indicator}")
        return self._get(
            self._lic("hsstock", "history", ind, code, period, dividend),
            st=st, et=et, lt=lt,
        )

    def stock_macd(self, code: str, period: str = "d", dividend: str = "n", **kw: Any) -> Any:
        """历史分时 MACD"""
        return self.stock_indicator("macd", code, period, dividend, **kw)

    def stock_ma(self, code: str, period: str = "d", dividend: str = "n", **kw: Any) -> Any:
        """历史分时 MA"""
        return self.stock_indicator("ma", code, period, dividend, **kw)

    def stock_boll(self, code: str, period: str = "d", dividend: str = "n", **kw: Any) -> Any:
        """历史分时 BOLL"""
        return self.stock_indicator("boll", code, period, dividend, **kw)

    def stock_kdj(self, code: str, period: str = "d", dividend: str = "n", **kw: Any) -> Any:
        """历史分时 KDJ"""
        return self.stock_indicator("kdj", code, period, dividend, **kw)

    # ================================================================== #
    # 沪深 A 股 — 实时交易
    # ================================================================== #

    def stock_real_time(self, code: str) -> Any:
        """实时交易数据（券商源）— /hsstock/real/time/{code}/{licence}"""
        return self._get(self._lic("hsstock", "real", "time", code))

    def stock_real_five(self, code: str) -> Any:
        """买卖五档盘口 — /hsstock/real/five/{code}/{licence}"""
        return self._get(self._lic("hsstock", "real", "five", code))

    def stock_ssjy(self, code: str) -> Any:
        """实时交易数据（网络源）— /hsrl/ssjy/{code}/{licence}"""
        return self._get(self._lic("hsrl", "ssjy", code))

    def stock_ssjy_all(self) -> Any:
        """实时交易数据全部（券商源）— /hsrl/ssjy/all/{licence}"""
        return self._get(self._lic("hsrl", "ssjy", "all"))

    def stock_real_all(self) -> Any:
        """实时交易数据全部（网络源）— /hsrl/real/all/{licence}"""
        return self._get(self._lic("hsrl", "real", "all"))

    def stock_ssjy_more(self, stock_codes: Sequence[str] | str) -> Any:
        """
        批量实时（最多约 20 只）— /hsrl/ssjy_more/{licence}?stock_codes=...
        """
        if isinstance(stock_codes, str):
            codes = stock_codes
        else:
            codes = ",".join(str(c).strip() for c in stock_codes if str(c).strip())
        return self._get(self._lic("hsrl", "ssjy_more"), extra={"stock_codes": codes})

    def stock_zbjy(self, code: str) -> Any:
        """当天逐笔交易 — /hsrl/zbjy/{code}/{licence}"""
        return self._get(self._lic("hsrl", "zbjy", code))

    def stock_transaction(
        self,
        code: str,
        *,
        st: Optional[str] = None,
        et: Optional[str] = None,
        lt: Optional[int] = None,
    ) -> Any:
        """资金流向 — /hsstock/history/transaction/{code}/{licence}"""
        return self._get(
            self._lic("hsstock", "history", "transaction", code),
            st=st, et=et, lt=lt,
        )

    # ================================================================== #
    # 沪深 A 股 — 财务报表 / 基础信息
    # ================================================================== #

    def stock_financial(
        self,
        table: str,
        code: str,
        *,
        st: Optional[str] = None,
        et: Optional[str] = None,
        lt: Optional[int] = None,
    ) -> Any:
        """财务报表通用 — /hsstock/financial/{table}/{code}/{licence}"""
        t = table.strip().lower()
        if t not in FINANCIAL_TABLES:
            raise MairuiAPIError(f"table 须为 {FINANCIAL_TABLES}，收到: {table}")
        return self._get(
            self._lic("hsstock", "financial", t, code),
            st=st, et=et, lt=lt,
        )

    def stock_balance(self, code: str, **kw: Any) -> Any:
        """资产负债表"""
        return self.stock_financial("balance", code, **kw)

    def stock_income(self, code: str, **kw: Any) -> Any:
        """利润表"""
        return self.stock_financial("income", code, **kw)

    def stock_cashflow(self, code: str, **kw: Any) -> Any:
        """现金流量表"""
        return self.stock_financial("cashflow", code, **kw)

    def stock_pershareindex(self, code: str, **kw: Any) -> Any:
        """财务主要指标"""
        return self.stock_financial("pershareindex", code, **kw)

    def stock_capital(self, code: str, **kw: Any) -> Any:
        """公司股本表"""
        return self.stock_financial("capital", code, **kw)

    def stock_shareholder_count(self, code: str, **kw: Any) -> Any:
        """公司股东数"""
        return self.stock_financial("hm", code, **kw)

    def stock_top_holders(self, code: str, **kw: Any) -> Any:
        """公司十大股东"""
        return self.stock_financial("topholder", code, **kw)

    def stock_flow_holders(self, code: str, **kw: Any) -> Any:
        """公司十大流通股东"""
        return self.stock_financial("flowholder", code, **kw)

    def stock_instrument(self, code: str) -> Any:
        """股票基础信息 — /hsstock/instrument/{code}/{licence}"""
        return self._get(self._lic("hsstock", "instrument", code))

    # ================================================================== #
    # 沪深 A 股 — 上市公司详情 (F10 / hscp)
    # ================================================================== #

    def company(self, slug: str, code: str) -> Any:
        """上市公司详情通用 — /hscp/{slug}/{code}/{licence}"""
        s = slug.strip().lower()
        if s not in HSCP_SLUGS:
            raise MairuiAPIError(f"slug 须为 {HSCP_SLUGS}，收到: {slug}")
        return self._get(self._lic("hscp", s, code))

    def company_profile(self, code: str) -> Any:
        """公司简介"""
        return self.company("gsjj", code)

    def company_indexes(self, code: str) -> Any:
        """所属指数"""
        return self.company("sszs", code)

    def company_directors(self, code: str) -> Any:
        """历届董事会成员"""
        return self.company("ljds", code)

    def company_executives(self, code: str) -> Any:
        """历届高管成员"""
        return self.company("ljgg", code)

    def company_supervisors(self, code: str) -> Any:
        """历届监事会成员"""
        return self.company("ljjj", code)

    def company_top10_holders(self, code: str) -> Any:
        """十大股东"""
        return self.company("sdgd", code)

    def company_top10_float_holders(self, code: str) -> Any:
        """十大流通股东"""
        return self.company("ltgd", code)

    def company_holder_change(self, code: str) -> Any:
        """股东变化趋势"""
        return self.company("gdbh", code)

    def company_dividends(self, code: str) -> Any:
        """近年分红"""
        return self.company("jnfh", code)

    def company_seo(self, code: str) -> Any:
        """近年增发"""
        return self.company("jnzf", code)

    def company_unlock(self, code: str) -> Any:
        """解禁限售"""
        return self.company("jjxs", code)

    def company_fund_holding(self, code: str) -> Any:
        """基金持股"""
        return self.company("jjcg", code)

    def company_earnings_forecast(self, code: str) -> Any:
        """近年业绩预告"""
        return self.company("yjyg", code)

    def company_financial_index(self, code: str) -> Any:
        """财务指标"""
        return self.company("cwzb", code)

    def company_quarter_profit(self, code: str) -> Any:
        """近一年各季度利润"""
        return self.company("jdlr", code)

    def company_quarter_cashflow(self, code: str) -> Any:
        """近一年各季度现金流"""
        return self.company("jdxj", code)

    # ================================================================== #
    # 沪深 A 股 — 涨跌股池 / 概念树 / 特色
    # ================================================================== #

    def stock_pool(self, pool: str, date: str) -> Any:
        """涨跌股池通用 — /hslt/{ztgc|dtgc|...}/{date}/{licence}"""
        p = pool.strip().lower()
        if p not in POOL_TYPES:
            raise MairuiAPIError(f"pool 须为 {POOL_TYPES}，收到: {pool}")
        return self._get(self._lic("hslt", p, date))

    def limit_up_pool(self, date: str) -> Any:
        """涨停股池"""
        return self.stock_pool("ztgc", date)

    def limit_down_pool(self, date: str) -> Any:
        """跌停股池"""
        return self.stock_pool("dtgc", date)

    def strong_pool(self, date: str) -> Any:
        """强势股池"""
        return self.stock_pool("qsgc", date)

    def new_stock_pool(self, date: str) -> Any:
        """次新股池"""
        return self.stock_pool("cxgc", date)

    def broken_board_pool(self, date: str) -> Any:
        """炸板股池"""
        return self.stock_pool("zbgc", date)

    def concept_tree(self) -> Any:
        """指数、行业、概念树 — /hszg/list/{licence}"""
        return self._get(self._lic("hszg", "list"))

    def concepts_of_stock(self, code: str) -> Any:
        """根据股票找相关指数/行业/概念 — /hszg/zg/{code}/{licence}"""
        return self._get(self._lic("hszg", "zg", code))

    def stocks_of_concept(self, concept_code: str) -> Any:
        """根据指数/行业/概念找相关股票 — /hszg/gg/{code}/{licence}"""
        return self._get(self._lic("hszg", "gg", concept_code))

    def stock_interactiveqa(
        self,
        code: str,
        *,
        st: Optional[str] = None,
        et: Optional[str] = None,
        lt: Optional[int] = None,
    ) -> Any:
        """问董秘 — /hsstock/interactiveqa/{code}/{licence}"""
        return self._get(
            self._lic("hsstock", "interactiveqa", code),
            st=st, et=et, lt=lt,
        )

    def stock_announcement(
        self,
        code: str,
        *,
        st: Optional[str] = None,
        et: Optional[str] = None,
        lt: Optional[int] = None,
    ) -> Any:
        """交易所公告 — /hsstock/announcement/{code}/{licence}"""
        return self._get(
            self._lic("hsstock", "announcement", code),
            st=st, et=et, lt=lt,
        )

    # ================================================================== #
    # 沪深指数
    # ================================================================== #

    def index_list(self) -> Any:
        """沪深主要指数列表 — /hsindex/list/{licence}"""
        return self._get(self._lic("hsindex", "list"))

    def index_history(
        self,
        code: str,
        period: str = "d",
        *,
        st: Optional[str] = None,
        et: Optional[str] = None,
        lt: Optional[int] = None,
    ) -> Any:
        """指数历史分时 — /hsindex/history/{code}/{period}/{licence}"""
        return self._get(
            self._lic("hsindex", "history", code, period),
            st=st, et=et, lt=lt,
        )

    def index_latest(self, code: str, period: str = "d", *, lt: Optional[int] = None) -> Any:
        """指数最新分时 — /hsindex/latest/{code}/{period}/{licence}"""
        return self._get(self._lic("hsindex", "latest", code, period), lt=lt)

    def index_indicator(
        self,
        indicator: str,
        code: str,
        period: str = "d",
        *,
        st: Optional[str] = None,
        et: Optional[str] = None,
        lt: Optional[int] = None,
    ) -> Any:
        """指数技术指标 macd/ma/boll/kdj"""
        ind = indicator.strip().lower()
        if ind not in INDICATORS:
            raise MairuiAPIError(f"indicator 须为 {INDICATORS}，收到: {indicator}")
        return self._get(
            self._lic("hsindex", "history", ind, code, period),
            st=st, et=et, lt=lt,
        )

    def index_macd(self, code: str, period: str = "d", **kw: Any) -> Any:
        return self.index_indicator("macd", code, period, **kw)

    def index_ma(self, code: str, period: str = "d", **kw: Any) -> Any:
        return self.index_indicator("ma", code, period, **kw)

    def index_boll(self, code: str, period: str = "d", **kw: Any) -> Any:
        return self.index_indicator("boll", code, period, **kw)

    def index_kdj(self, code: str, period: str = "d", **kw: Any) -> Any:
        return self.index_indicator("kdj", code, period, **kw)

    def index_real_time(self, code: str) -> Any:
        """指数实时 — /hsindex/real/time/{code}/{licence}"""
        return self._get(self._lic("hsindex", "real", "time", code))

    # ================================================================== #
    # 京市 A 股
    # ================================================================== #

    def bj_stock_list(self) -> Any:
        """京市股票列表"""
        return self._get(self._lic("bj", "list", "all"))

    def bj_index_list(self) -> Any:
        """京市指数列表"""
        return self._get(self._lic("bj", "list", "index"))

    def bj_stock_real_time(self, code: str) -> Any:
        return self._get(self._lic("bj", "stock", "real", "time", code))

    def bj_stock_real_five(self, code: str) -> Any:
        return self._get(self._lic("bj", "stock", "real", "five", code))

    def bj_index_real_time(self, code: str) -> Any:
        return self._get(self._lic("bj", "index", "real", "time", code))

    def bj_history(
        self,
        code: str,
        period: str = "d",
        dividend: str = "n",
        *,
        st: Optional[str] = None,
        et: Optional[str] = None,
        lt: Optional[int] = None,
    ) -> Any:
        """京市历史分时"""
        return self._get(
            self._lic("bj", "history", code, period, dividend),
            st=st, et=et, lt=lt,
        )

    def bj_financial(
        self,
        table: str,
        code: str,
        *,
        st: Optional[str] = None,
        et: Optional[str] = None,
        lt: Optional[int] = None,
    ) -> Any:
        t = table.strip().lower()
        if t not in FINANCIAL_TABLES:
            raise MairuiAPIError(f"table 须为 {FINANCIAL_TABLES}，收到: {table}")
        return self._get(
            self._lic("bj", "financial", t, code),
            st=st, et=et, lt=lt,
        )

    def bj_balance(self, code: str, **kw: Any) -> Any:
        return self.bj_financial("balance", code, **kw)

    def bj_income(self, code: str, **kw: Any) -> Any:
        return self.bj_financial("income", code, **kw)

    def bj_cashflow(self, code: str, **kw: Any) -> Any:
        return self.bj_financial("cashflow", code, **kw)

    def bj_pershareindex(self, code: str, **kw: Any) -> Any:
        return self.bj_financial("pershareindex", code, **kw)

    def bj_capital(self, code: str, **kw: Any) -> Any:
        return self.bj_financial("capital", code, **kw)

    def bj_shareholder_count(self, code: str, **kw: Any) -> Any:
        return self.bj_financial("hm", code, **kw)

    def bj_top_holders(self, code: str, **kw: Any) -> Any:
        return self.bj_financial("topholder", code, **kw)

    def bj_flow_holders(self, code: str, **kw: Any) -> Any:
        return self.bj_financial("flowholder", code, **kw)

    # ================================================================== #
    # 沪深基金 / 科创
    # ================================================================== #

    def fund_list(self) -> Any:
        """沪深基金列表"""
        return self._get(self._lic("fd", "list", "all"))

    def etf_list(self) -> Any:
        """ETF 基金列表"""
        return self._get(self._lic("fd", "list", "etf"))

    def fund_real_time(self, code: str) -> Any:
        """基金实时"""
        return self._get(self._lic("fd", "real", "time", code))

    def star_stock_list(self) -> Any:
        """科创股票列表"""
        return self._get(self._lic("kc", "list", "all"))

    def star_real_time(self, code: str) -> Any:
        """科创实时"""
        return self._get(self._lic("kc", "real", "time", code))

    def star_real_five(self, code: str) -> Any:
        """科创五档"""
        return self._get(self._lic("kc", "real", "five", code))
