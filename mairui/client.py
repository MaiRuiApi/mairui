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

    # === SDK_GENERATED_BEGIN_v1_2_0 ===
    # 目录驱动生成：勿手改；重跑 gen_sdk_from_catalog.py

    # ------------------------------------------------------------------ #
    # 沪深数据中心
    # ------------------------------------------------------------------ #

    def hsdc_jrts(self) -> Any:
        """今日交易提示 — GET /hitc/jrts/{licence}"""
        return self._get(self._lic("hitc", "jrts"))

    def hsdc_rzrqzl(self) -> Any:
        """融资融券交易总量 — GET /hitc/rzrqzl/{licence}"""
        return self._get(self._lic("hitc", "rzrqzl"))

    def hsdc_rzrqmx(self) -> Any:
        """融资融券交易明细 — GET /hitc/rzrqmx/{licence}"""
        return self._get(self._lic("hitc", "rzrqmx"))

    def hsdc_dzjy(self) -> Any:
        """大宗交易 — GET /hitc/dzjy/{licence}"""
        return self._get(self._lic("hitc", "dzjy"))

    def hsdc_jjxs(self) -> Any:
        """解禁限售 — GET /hitc/jjxs/{licence}"""
        return self._get(self._lic("hitc", "jjxs"))

    def hsdc_dxsy(self) -> Any:
        """打新收益 — GET /hitc/dxsy/{licence}"""
        return self._get(self._lic("hitc", "dxsy"))

    def hsdc_lsfh(self) -> Any:
        """历史累计分红 — GET /hitc/lsfh/{licence}"""
        return self._get(self._lic("hitc", "lsfh"))

    def hsdc_hilh_mrxq(self) -> Any:
        """每日详情 — GET /hilh/mrxq/{licence}"""
        return self._get(self._lic("hilh", "mrxq"))

    def hsdc_hilh_xwmx(self) -> Any:
        """机构席位成交明细 — GET /hilh/xwmx/{licence}"""
        return self._get(self._lic("hilh", "xwmx"))

    def hsdc_himk_jdzgzd(self) -> Any:
        """阶段最高最低 — GET /himk/jdzgzd/{licence}"""
        return self._get(self._lic("himk", "jdzgzd"))

    def hsdc_himk_pzxg(self) -> Any:
        """盘中创新高个股 — GET /himk/pzxg/{licence}"""
        return self._get(self._lic("himk", "pzxg"))

    def hsdc_himk_pzxd(self) -> Any:
        """盘中创新低个股 — GET /himk/pzxd/{licence}"""
        return self._get(self._lic("himk", "pzxd"))

    def hsdc_himk_cjzz(self) -> Any:
        """成交骤增个股 — GET /himk/cjzz/{licence}"""
        return self._get(self._lic("himk", "cjzz"))

    def hsdc_himk_cjzj(self) -> Any:
        """成交骤减个股 — GET /himk/cjzj/{licence}"""
        return self._get(self._lic("himk", "cjzj"))

    def hsdc_himk_lxfl(self) -> Any:
        """连续放量个股 — GET /himk/lxfl/{licence}"""
        return self._get(self._lic("himk", "lxfl"))

    def hsdc_himk_lxsl(self) -> Any:
        """连续缩量个股 — GET /himk/lxsl/{licence}"""
        return self._get(self._lic("himk", "lxsl"))

    def hsdc_himk_lxsz(self) -> Any:
        """连续上涨个股 — GET /himk/lxsz/{licence}"""
        return self._get(self._lic("himk", "lxsz"))

    def hsdc_himk_lxxd(self) -> Any:
        """连续下跌个股 — GET /himk/lxxd/{licence}"""
        return self._get(self._lic("himk", "lxxd"))

    def hsdc_himk_zzd(self) -> Any:
        """周涨跌排名 — GET /himk/zzd/{licence}"""
        return self._get(self._lic("himk", "zzd"))

    def hsdc_himk_yzd(self) -> Any:
        """月涨跌排名 — GET /himk/yzd/{licence}"""
        return self._get(self._lic("himk", "yzd"))

    def hsdc_himk_zqsg(self) -> Any:
        """本周强势股 — GET /himk/zqsg/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("himk", "zqsg"))

    def hsdc_himk_mqsg(self) -> Any:
        """本月强势股 — GET /himk/mqsg/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("himk", "mqsg"))

    def hsdc_himk_ltszph(self) -> Any:
        """流通市值排行 — GET /himk/ltszph/{licence}"""
        return self._get(self._lic("himk", "ltszph"))

    def hsdc_himk_syl(self) -> Any:
        """市盈率排行 — GET /himk/syl/{licence}"""
        return self._get(self._lic("himk", "syl"))

    def hsdc_himk_sjl(self) -> Any:
        """市净率排行 — GET /himk/sjl/{licence}"""
        return self._get(self._lic("himk", "sjl"))

    def hsdc_himk_roe(self) -> Any:
        """ROE排行 — GET /himk/roe/{licence}"""
        return self._get(self._lic("himk", "roe"))

    def hsdc_hicw_lr(self) -> Any:
        """利润细分 — GET /hicw/lr/{licence}"""
        return self._get(self._lic("hicw", "lr"))

    def hsdc_hibk_zjhhy(self) -> Any:
        """证监会行业 — GET /hibk/zjhhy/{licence}"""
        return self._get(self._lic("hibk", "zjhhy"))

    def hsdc_hibk_gnbk(self) -> Any:
        """概念板块 — GET /hibk/gnbk/{licence}"""
        return self._get(self._lic("hibk", "gnbk"))

    def hsdc_jlr(self) -> Any:
        """净流入额排名 — GET /higg/jlr/{licence}"""
        return self._get(self._lic("higg", "jlr"))

    def hsdc_jlrl(self) -> Any:
        """净流入率排名 — GET /higg/jlrl/{licence}"""
        return self._get(self._lic("higg", "jlrl"))

    def hsdc_zljlr(self) -> Any:
        """主力净流入额排名 — GET /higg/zljlr/{licence}"""
        return self._get(self._lic("higg", "zljlr"))

    def hsdc_zljlrl(self) -> Any:
        """主力净流入率排名 — GET /higg/zljlrl/{licence}"""
        return self._get(self._lic("higg", "zljlrl"))

    def hsdc_shzlr(self) -> Any:
        """散户净流入额排名 — GET /higg/shzlr/{licence}"""
        return self._get(self._lic("higg", "shzlr"))

    def hsdc_shjlrl(self) -> Any:
        """散户净流入率排名 — GET /higg/shjlrl/{licence}"""
        return self._get(self._lic("higg", "shjlrl"))

    def hsdc_zjh(self) -> Any:
        """证监会行业资金路线图 — GET /hizj/zjh/{licence}"""
        return self._get(self._lic("hizj", "zjh"))

    def hsdc_bk(self) -> Any:
        """概念板块资金路线图 — GET /hizj/bk/{licence}"""
        return self._get(self._lic("hizj", "bk"))

    def hsdc_ggzl(self) -> Any:
        """个股阶段统计总览 — GET /hizj/ggzl/{licence}"""
        return self._get(self._lic("hizj", "ggzl"))

    def hsdc_lxlr(self) -> Any:
        """主力连续净流入/流出 — GET /hizj/lxlr/{licence}"""
        return self._get(self._lic("hizj", "lxlr"))

    def hsdc_nbzj_lxgl(self) -> Any:
        """最新资金流向概览 — GET /ht/nbzj/lxgl/{licence}"""
        return self._get(self._lic("ht", "nbzj", "lxgl"))

    def hsdc_nbzj_bxls(self, jd: str) -> Any:
        """北向资金历史走势 — GET /ht/nbzj/bxls/{jd}/{licence}"""
        return self._get(self._lic("ht", "nbzj", "bxls", jd))

    def hsdc_nbzj_nxls(self, jd: str) -> Any:
        """南向资金历史走势 — GET /ht/nbzj/nxls/{jd}/{licence}"""
        return self._get(self._lic("ht", "nbzj", "nxls", jd))

    def hsdc_nbzj_bxzl(self) -> Any:
        """北向资金历史总览 — GET /ht/nbzj/bxzl/{licence}"""
        return self._get(self._lic("ht", "nbzj", "bxzl"))

    def hsdc_nbzj_nxzl(self) -> Any:
        """南向资金历史总览 — GET /ht/nbzj/nxzl/{licence}"""
        return self._get(self._lic("ht", "nbzj", "nxzl"))

    def hsdc_nbzj_hgtc(self) -> Any:
        """沪股通成分股行情 — GET /ht/nbzj/hgtc/{licence}"""
        return self._get(self._lic("ht", "nbzj", "hgtc"))

    def hsdc_nbzj_sgtc(self) -> Any:
        """深股通成分股行情 — GET /ht/nbzj/sgtc/{licence}"""
        return self._get(self._lic("ht", "nbzj", "sgtc"))

    def hsdc_nbzj_ggth(self) -> Any:
        """港股通（沪）成分股行情 — GET /ht/nbzj/ggth/{licence}"""
        return self._get(self._lic("ht", "nbzj", "ggth"))

    def hsdc_nbzj_ggts(self) -> Any:
        """港股通（深）成分股行情 — GET /ht/nbzj/ggts/{licence}"""
        return self._get(self._lic("ht", "nbzj", "ggts"))

    def hsdc_nbzj_ah(self) -> Any:
        """AH股比价 — GET /ht/nbzj/ah/{licence}"""
        return self._get(self._lic("ht", "nbzj", "ah"))

    def hsdc_nbzj_hgts(self) -> Any:
        """沪股通十大成交股 — GET /ht/nbzj/hgts/{licence}"""
        return self._get(self._lic("ht", "nbzj", "hgts"))

    def hsdc_nbzj_sgts(self) -> Any:
        """深股通十大成交股 — GET /ht/nbzj/sgts/{licence}"""
        return self._get(self._lic("ht", "nbzj", "sgts"))

    def hsdc_nbzj_hcjd(self) -> Any:
        """港股通（沪）十大成交股 — GET /ht/nbzj/hcjd/{licence}"""
        return self._get(self._lic("ht", "nbzj", "hcjd"))

    def hsdc_nbzj_scjd(self) -> Any:
        """港股通（深）十大成交股 — GET /ht/nbzj/scjd/{licence}"""
        return self._get(self._lic("ht", "nbzj", "scjd"))

    def hsdc_nbzj_bxpm(self, zq: str) -> Any:
        """北向个股周期排名 — GET /ht/nbzj/bxpm/{zq}/{licence}"""
        return self._get(self._lic("ht", "nbzj", "bxpm", zq))

    def hsdc_nbzj_hgpm(self, zq: str) -> Any:
        """沪股通个股周期排名 — GET /ht/nbzj/hgpm/{zq}/{licence}"""
        return self._get(self._lic("ht", "nbzj", "hgpm", zq))

    def hsdc_nbzj_sgpm(self, zq: str) -> Any:
        """深股通个股周期排名 — GET /ht/nbzj/sgpm/{zq}/{licence}"""
        return self._get(self._lic("ht", "nbzj", "sgpm", zq))

    def hsdc_nbzj_hgls(self) -> Any:
        """沪股通历史数据 — GET /ht/nbzj/hgls/{licence}"""
        return self._get(self._lic("ht", "nbzj", "hgls"))

    def hsdc_nbzj_shls(self) -> Any:
        """深股通历史数据 — GET /ht/nbzj/shls/{licence}"""
        return self._get(self._lic("ht", "nbzj", "shls"))

    def hsdc_nbzj_ghls(self) -> Any:
        """港股通（沪）历史数据 — GET /ht/nbzj/ghls/{licence}"""
        return self._get(self._lic("ht", "nbzj", "ghls"))

    def hsdc_nbzj_gsls(self) -> Any:
        """港股通（深）历史数据 — GET /ht/nbzj/gsls/{licence}"""
        return self._get(self._lic("ht", "nbzj", "gsls"))

    def hsdc_list(self) -> Any:
        """可转债一览 — GET /kzz/list/{licence}"""
        return self._get(self._lic("kzz", "list"))

    def hsdc_comparison(self) -> Any:
        """可转债比价表 — GET /kzz/comparison/{licence}"""
        return self._get(self._lic("kzz", "comparison"))

    def hsdc_spot(self) -> Any:
        """可转债实时行情 — GET /kzz/spot/{licence}"""
        return self._get(self._lic("kzz", "spot"))


    # ------------------------------------------------------------------ #
    # 基金数据中心
    # ------------------------------------------------------------------ #

    def fundc_pm_kfjzg(self) -> Any:
        """开放式基金净值排名（股、混合、债、QDII类） — GET /js/pm/kfjzg/kfsjj_gpxjj_zsx/{licence}"""
        return self._get(self._lic("js", "pm", "kfjzg", "kfsjj_gpxjj_zsx"))

    def fundc_pm_kfjzq(self) -> Any:
        """开放式基金净值排名（货币类） — GET /js/pm/kfjzq/kfsjj_hbxjj_hba/{licence}"""
        return self._get(self._lic("js", "pm", "kfjzq", "kfsjj_hbxjj_hba"))

    def fundc_pm_fbjz(self) -> Any:
        """封闭式基金净值排名 — GET /js/pm/fbjz/kfsjj_fbqy_ctfj/{licence}"""
        return self._get(self._lic("js", "pm", "fbjz", "kfsjj_fbqy_ctfj"))

    def fundc_pm_kfpm(self) -> Any:
        """开放式基金业绩排行（股、混合、债、QDII类） — GET /js/pm/kfpm/kfsjj_gpxjj_zsx/{licence}"""
        return self._get(self._lic("js", "pm", "kfpm", "kfsjj_gpxjj_zsx"))

    def fundc_pm_fbpm(self) -> Any:
        """封闭式基金业绩排行 — GET /js/pm/fbpm/kfsjj_fbqy_ctfj/{licence}"""
        return self._get(self._lic("js", "pm", "fbpm", "kfsjj_fbqy_ctfj"))

    def fundc_pm_fzyj(self) -> Any:
        """分级子基金业绩排行 — GET /js/pm/fzyj/kfsjj_fjgs_wjzqx/{licence}"""
        return self._get(self._lic("js", "pm", "fzyj", "kfsjj_fjgs_wjzqx"))

    def fundc_jf_kffh(self) -> Any:
        """开放式基金基金分红 — GET /js/jf/kffh/kfsjj_gpxjj_zsx/{licence}"""
        return self._get(self._lic("js", "jf", "kffh", "kfsjj_gpxjj_zsx"))

    def fundc_jf_fzfh(self) -> Any:
        """分级子基金基金分红 — GET /js/jf/fzfh/kfsjj_fjgs_wjzqx/{licence}"""
        return self._get(self._lic("js", "jf", "fzfh", "kfsjj_fjgs_wjzqx"))

    def fundc_gm_kfgm(self) -> Any:
        """开放式基金基金规模 — GET /js/gm/kfgm/kfsjj_gpxjj_zsx/{licence}"""
        return self._get(self._lic("js", "gm", "kfgm", "kfsjj_gpxjj_zsx"))

    def fundc_gm_fbgm(self) -> Any:
        """封闭式基金基金规模 — GET /js/gm/fbgm/kfsjj_fbqy_ctfj/{licence}"""
        return self._get(self._lic("js", "gm", "fbgm", "kfsjj_fbqy_ctfj"))

    def fundc_gm_fzgm(self) -> Any:
        """分级子基金基金规模 — GET /js/gm/fzgm/kfsjj_fjgs_wjzqx/{licence}"""
        return self._get(self._lic("js", "gm", "fzgm", "kfsjj_fjgs_wjzqx"))

    def fundc_other_jjzc(self, yyyy_j: str) -> Any:
        """基金重仓股 — GET /js/other/jjzc/{yyyy_j}/{licence}"""
        return self._get(self._lic("js", "other", "jjzc", yyyy_j))

    def fundc_other_zcbd(self, yyyy_j: str) -> Any:
        """基金重仓股变动 — GET /js/other/zcbd/{yyyy_j}/{licence}"""
        return self._get(self._lic("js", "other", "zcbd", yyyy_j))

    def fundc_other_dxjg(self) -> Any:
        """代销机构 — GET /js/other/dxjg/yh/{licence}"""
        return self._get(self._lic("js", "other", "dxjg", "yh"))


    # ------------------------------------------------------------------ #
    # 基金行情档案
    # ------------------------------------------------------------------ #

    def fundf10_all(self) -> Any:
        """所有基金列表 — GET /jj/all/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "all"))

    def fundf10_gzlb(self) -> Any:
        """估值基金列表 — GET /jj/gzlb/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "gzlb"))

    def fundf10_pzzzgz(self, code: str) -> Any:
        """盘中最新估值 — GET /jj/pzzzgz/{code}/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "pzzzgz", code))

    def fundf10_hqzksjz(self, code: str) -> Any:
        """开放式基金净值 — GET /jj/hqzksjz/{code}/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "hqzksjz", code))

    def fundf10_jjyj(self, code: str) -> Any:
        """基金业绩 — GET /jj/jjyj/{code}/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "jjyj", code))

    def fundf10_jjfh(self, code: str) -> Any:
        """基金分红 — GET /jj/jjfh/{code}/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "jjfh", code))

    def fundf10_jjgm(self, code: str) -> Any:
        """基金规模 — GET /jj/jjgm/{code}/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "jjgm", code))

    def fundf10_fbs(self) -> Any:
        """封闭式基金列表 — GET /jj/fbs/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "fbs"))

    def fundf10_etf(self) -> Any:
        """ETF基金列表 — GET /jj/etf/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "etf"))

    def fundf10_lof(self) -> Any:
        """LOF基金列表 — GET /jj/lof/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "lof"))

    def fundf10_jjgk(self, code: str) -> Any:
        """基金概况 — GET /jj/jjgk/{code}/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "jjgk", code))

    def fundf10_zrjl(self) -> Any:
        """在任基金经理列表 — GET /jj/zrjl/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "zrjl"))

    def fundf10_lsjz(self, code: str) -> Any:
        """历史净值 — GET /jj/lsjz/{code}/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "lsjz", code))

    def fundf10_fhps(self, code: str) -> Any:
        """分红送配 — GET /jj/fhps/{code}/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "fhps", code))

    def fundf10_jdtj(self, code: str) -> Any:
        """阶段统计 — GET /jj/jdtj/{code}/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "jdtj", code))

    def fundf10_jdzfmx(self, code: str) -> Any:
        """季度涨幅明细 — GET /jj/jdzfmx/{code}/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "jdzfmx", code))

    def fundf10_gpcc(self, code: str) -> Any:
        """股票持仓 — GET /jj/gpcc/{code}/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "gpcc", code))

    def fundf10_zqcc(self, code: str) -> Any:
        """债券持仓 — GET /jj/zqcc/{code}/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "zqcc", code))

    def fundf10_hypz(self, code: str) -> Any:
        """行业配置 — GET /jj/hypz/{code}/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "hypz", code))

    def fundf10_zcpz(self, code: str) -> Any:
        """资产配置 — GET /jj/zcpz/{code}/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "zcpz", code))

    def fundf10_gmbd(self, code: str) -> Any:
        """规模变动 — GET /jj/gmbd/{code}/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "gmbd", code))

    def fundf10_cyrjg(self, code: str) -> Any:
        """持有人结构 — GET /jj/cyrjg/{code}/{licence}（文档页可能隐藏）"""
        return self._get(self._lic("jj", "cyrjg", code))


    # ------------------------------------------------------------------ #
    # 量化因子
    # ------------------------------------------------------------------ #

    def factor_list(self) -> Any:
        """因子列表 — GET /factor/list/{licence}"""
        return self._get(self._lic("factor", "list"))

    def factor_categories(self) -> Any:
        """因子分类树 — GET /factor/categories/{licence}"""
        return self._get(self._lic("factor", "categories"))

    def factor_valuation(self, code: str) -> Any:
        """估值因子 — GET /factor/valuation/{code}/{licence}"""
        return self._get(self._lic("factor", "valuation", code))

    def factor_quality(self, code: str) -> Any:
        """质量因子 — GET /factor/quality/{code}/{licence}"""
        return self._get(self._lic("factor", "quality", code))

    def factor_growth(self, code: str) -> Any:
        """成长因子 — GET /factor/growth/{code}/{licence}"""
        return self._get(self._lic("factor", "growth", code))

    def factor_momentum(self, code: str) -> Any:
        """动量因子 — GET /factor/momentum/{code}/{licence}"""
        return self._get(self._lic("factor", "momentum", code))

    def factor_capital(self, code: str) -> Any:
        """资金面因子 — GET /factor/capital/{code}/{licence}"""
        return self._get(self._lic("factor", "capital", code))

    def factor_signal(self, code: str) -> Any:
        """技术信号因子 — GET /factor/signal/{code}/{licence}"""
        return self._get(self._lic("factor", "signal", code))

    def factor_risk(self, code: str) -> Any:
        """风险因子 — GET /factor/risk/{code}/{licence}"""
        return self._get(self._lic("factor", "risk", code))

    def factor_dividend(self, code: str) -> Any:
        """分红因子 — GET /factor/dividend/{code}/{licence}"""
        return self._get(self._lic("factor", "dividend", code))

    def factor_scale(self, code: str) -> Any:
        """规模流动性因子 — GET /factor/scale/{code}/{licence}"""
        return self._get(self._lic("factor", "scale", code))

    def factor_sentiment(self, code: str) -> Any:
        """情绪事件因子 — GET /factor/sentiment/{code}/{licence}"""
        return self._get(self._lic("factor", "sentiment", code))

    def factor_all(self, code: str) -> Any:
        """单股全因子 — GET /factor/all/{code}/{licence}"""
        return self._get(self._lic("factor", "all", code))

    def factor_rank(self, factor_id: str) -> Any:
        """因子排名 — GET /factor/rank/{factor_id}/{licence}"""
        return self._get(self._lic("factor", "rank", factor_id))

    def factor_top(self, factor_id: str, arg: str) -> Any:
        """因子 Top N — GET /factor/top/{factor_id}/{arg}/{licence}"""
        return self._get(self._lic("factor", "top", factor_id, arg))

    def factor_history(self, factor_id: str, code: str) -> Any:
        """因子历史序列 — GET /factor/history/{factor_id}/{code}/{licence}"""
        return self._get(self._lic("factor", "history", factor_id, code))

    def factor_percentile(self, factor_id: str, code: str) -> Any:
        """因子分位数 — GET /factor/percentile/{factor_id}/{code}/{licence}"""
        return self._get(self._lic("factor", "percentile", factor_id, code))

    # === SDK_GENERATED_END_v1_2_0 ===
