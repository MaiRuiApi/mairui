# 文档接口 ↔ SDK 方法对照

来源：官网公开 API 文档（如 [`https://mairuiapi.com/hsdata`](https://mairuiapi.com/hsdata)）。  
基址默认：`https://api.mairuiapi.com`；`{licence}` 由 `Client(licence=...)` 注入。

## 沪深A股

### 股票列表

| 文档名称 | SDK 方法 | 路径 |
|----------|----------|------|
| 股票列表 | `stock_list()` | `/hslt/list/{licence}` |
| 新股日历 | `new_stock_calendar()` | `/hslt/new/{licence}` |
| 概念指数列表 | `sectors_list()` | `/hslt/sectorslist/{licence}` |
| 一级市场板块列表 | `primary_sectors_list()` | `/hslt/primarylist/{licence}` |
| 板块明细列表 | `sector_detail(name)` | `/hslt/sectors/{name}/{licence}` |

### 行情数据 / 技术指标

| 文档名称 | SDK 方法 |
|----------|----------|
| 历史分时交易 | `stock_history(code, period, dividend, st=, et=, lt=)` |
| 最新分时交易 | `stock_latest(code, period, dividend, lt=)` |
| 企业版历史数据 | `stock_vip_history(code, period, dividend, ...)` |
| 历史涨跌停价格 | `stock_stopprice(code, ...)` |
| 行情指标 | `stock_indicators(code, ...)` |
| 历史分时 MACD/MA/BOLL/KDJ | `stock_macd` / `stock_ma` / `stock_boll` / `stock_kdj` 或 `stock_indicator(ind, ...)` |

### 实时交易

| 文档名称 | SDK 方法 |
|----------|----------|
| 实时交易（券商源） | `stock_real_time(code)` |
| 买卖五档盘口 | `stock_real_five(code)` |
| 实时交易（网络源） | `stock_ssjy(code)` |
| 实时全部（券商） | `stock_ssjy_all()` |
| 实时全部（网络） | `stock_real_all()` |
| 实时多股 | `stock_ssjy_more(codes)` |
| 当天逐笔交易 | `stock_zbjy(code)` |
| 资金流向 | `stock_transaction(code, ...)` |

### 财务报表 / 基础信息

| 文档名称 | SDK 方法 |
|----------|----------|
| 资产负债表等八表 | `stock_financial(table, code)` 或 `stock_balance` / `stock_income` / … |
| 股票基础信息 | `stock_instrument(code)` |

### 上市公司详情

| 文档名称 | SDK 方法 |
|----------|----------|
| 公司简介等 16 项 | `company(slug, code)` 或 `company_profile` / `company_indexes` / … |

### 涨跌股池 / 概念 / 特色

| 文档名称 | SDK 方法 |
|----------|----------|
| 涨停/跌停/强势/次新/炸板 | `limit_up_pool` / `limit_down_pool` / `strong_pool` / `new_stock_pool` / `broken_board_pool` |
| 指数行业概念树 | `concept_tree()` |
| 股票→概念 | `concepts_of_stock(code)` |
| 概念→股票 | `stocks_of_concept(code)` |
| 问董秘 | `stock_interactiveqa(code, ...)` |
| 交易所公告 | `stock_announcement(code, ...)` |

## 沪深指数

| 文档名称 | SDK 方法 |
|----------|----------|
| 指数列表 | `index_list()` |
| 历史 / 最新分时 | `index_history` / `index_latest` |
| MACD/MA/BOLL/KDJ | `index_macd` / `index_ma` / `index_boll` / `index_kdj` |
| 实时 | `index_real_time(code)` |

## 京市A股

| 文档名称 | SDK 方法 |
|----------|----------|
| 股票/指数列表 | `bj_stock_list` / `bj_index_list` |
| 实时 / 五档 / 指数实时 | `bj_stock_real_time` / `bj_stock_real_five` / `bj_index_real_time` |
| 历史分时 | `bj_history` |
| 财务八表 | `bj_financial` / `bj_balance` / … |

## 沪深基金 / 科创行情

| 文档名称 | SDK 方法 |
|----------|----------|
| 基金列表 / ETF 列表 | `fund_list` / `etf_list` |
| 基金实时 | `fund_real_time(code)` |
| 科创列表 / 实时 / 五档 | `star_stock_list` / `star_real_time` / `star_real_five` |

## 批量

| 能力 | 方法 |
|------|------|
| 多标的并发 | `api.map(api.stock_history, codes, period="d", dividend="n", max_workers=8)` |

<!-- SDK_1_2_0_MAP_BEGIN -->

## v1.2.0 新增（沪深数据中心 / 基金 / 因子）

| 分类 | 文档名称 | SDK 方法 | 路径 |
|------|----------|----------|------|
| 沪深数据中心 | 净流入额排名 | `hsdc_jlr()` | `/higg/jlr/{licence}` |
| 沪深数据中心 | 净流入率排名 | `hsdc_jlrl()` | `/higg/jlrl/{licence}` |
| 沪深数据中心 | 主力净流入额排名 | `hsdc_zljlr()` | `/higg/zljlr/{licence}` |
| 沪深数据中心 | 主力净流入率排名 | `hsdc_zljlrl()` | `/higg/zljlrl/{licence}` |
| 沪深数据中心 | 散户净流入额排名 | `hsdc_shzlr()` | `/higg/shzlr/{licence}` |
| 沪深数据中心 | 散户净流入率排名 | `hsdc_shjlrl()` | `/higg/shjlrl/{licence}` |
| 沪深数据中心 | 最新资金流向概览 | `hsdc_nbzj_lxgl()` | `/ht/nbzj/lxgl/{licence}` |
| 沪深数据中心 | 北向资金历史走势 | `hsdc_nbzj_bxls(jd)` | `/ht/nbzj/bxls/{jd}/{licence}` |
| 沪深数据中心 | 南向资金历史走势 | `hsdc_nbzj_nxls(jd)` | `/ht/nbzj/nxls/{jd}/{licence}` |
| 沪深数据中心 | 北向资金历史总览 | `hsdc_nbzj_bxzl()` | `/ht/nbzj/bxzl/{licence}` |
| 沪深数据中心 | 南向资金历史总览 | `hsdc_nbzj_nxzl()` | `/ht/nbzj/nxzl/{licence}` |
| 沪深数据中心 | 沪股通成分股行情 | `hsdc_nbzj_hgtc()` | `/ht/nbzj/hgtc/{licence}` |
| 沪深数据中心 | 深股通成分股行情 | `hsdc_nbzj_sgtc()` | `/ht/nbzj/sgtc/{licence}` |
| 沪深数据中心 | 港股通（沪）成分股行情 | `hsdc_nbzj_ggth()` | `/ht/nbzj/ggth/{licence}` |
| 沪深数据中心 | 港股通（深）成分股行情 | `hsdc_nbzj_ggts()` | `/ht/nbzj/ggts/{licence}` |
| 沪深数据中心 | AH股比价 | `hsdc_nbzj_ah()` | `/ht/nbzj/ah/{licence}` |
| 沪深数据中心 | 沪股通十大成交股 | `hsdc_nbzj_hgts()` | `/ht/nbzj/hgts/{licence}` |
| 沪深数据中心 | 深股通十大成交股 | `hsdc_nbzj_sgts()` | `/ht/nbzj/sgts/{licence}` |
| 沪深数据中心 | 港股通（沪）十大成交股 | `hsdc_nbzj_hcjd()` | `/ht/nbzj/hcjd/{licence}` |
| 沪深数据中心 | 港股通（深）十大成交股 | `hsdc_nbzj_scjd()` | `/ht/nbzj/scjd/{licence}` |
| 沪深数据中心 | 北向个股周期排名 | `hsdc_nbzj_bxpm(zq)` | `/ht/nbzj/bxpm/{zq}/{licence}` |
| 沪深数据中心 | 沪股通个股周期排名 | `hsdc_nbzj_hgpm(zq)` | `/ht/nbzj/hgpm/{zq}/{licence}` |
| 沪深数据中心 | 深股通个股周期排名 | `hsdc_nbzj_sgpm(zq)` | `/ht/nbzj/sgpm/{zq}/{licence}` |
| 沪深数据中心 | 沪股通历史数据 | `hsdc_nbzj_hgls()` | `/ht/nbzj/hgls/{licence}` |
| 沪深数据中心 | 深股通历史数据 | `hsdc_nbzj_shls()` | `/ht/nbzj/shls/{licence}` |
| 沪深数据中心 | 港股通（沪）历史数据 | `hsdc_nbzj_ghls()` | `/ht/nbzj/ghls/{licence}` |
| 沪深数据中心 | 港股通（深）历史数据 | `hsdc_nbzj_gsls()` | `/ht/nbzj/gsls/{licence}` |
| 沪深数据中心 | 可转债一览 | `hsdc_list()` | `/kzz/list/{licence}` |
| 沪深数据中心 | 可转债比价表 | `hsdc_comparison()` | `/kzz/comparison/{licence}` |
| 沪深数据中心 | 可转债实时行情 | `hsdc_spot()` | `/kzz/spot/{licence}` |
| 沪深数据中心 | 阶段最高最低 | `hsdc_himk_jdzgzd()` | `/himk/jdzgzd/{licence}` |
| 沪深数据中心 | 盘中创新高个股 | `hsdc_himk_pzxg()` | `/himk/pzxg/{licence}` |
| 沪深数据中心 | 盘中创新低个股 | `hsdc_himk_pzxd()` | `/himk/pzxd/{licence}` |
| 沪深数据中心 | 成交骤增个股 | `hsdc_himk_cjzz()` | `/himk/cjzz/{licence}` |
| 沪深数据中心 | 成交骤减个股 | `hsdc_himk_cjzj()` | `/himk/cjzj/{licence}` |
| 沪深数据中心 | 连续放量个股 | `hsdc_himk_lxfl()` | `/himk/lxfl/{licence}` |
| 沪深数据中心 | 连续缩量个股 | `hsdc_himk_lxsl()` | `/himk/lxsl/{licence}` |
| 沪深数据中心 | 连续上涨个股 | `hsdc_himk_lxsz()` | `/himk/lxsz/{licence}` |
| 沪深数据中心 | 连续下跌个股 | `hsdc_himk_lxxd()` | `/himk/lxxd/{licence}` |
| 沪深数据中心 | 周涨跌排名 | `hsdc_himk_zzd()` | `/himk/zzd/{licence}` |
| 沪深数据中心 | 月涨跌排名 | `hsdc_himk_yzd()` | `/himk/yzd/{licence}` |
| 沪深数据中心 | 本周强势股 | `hsdc_himk_zqsg()` | `/himk/zqsg/{licence}` |
| 沪深数据中心 | 本月强势股 | `hsdc_himk_mqsg()` | `/himk/mqsg/{licence}` |
| 沪深数据中心 | 流通市值排行 | `hsdc_himk_ltszph()` | `/himk/ltszph/{licence}` |
| 沪深数据中心 | 市盈率排行 | `hsdc_himk_syl()` | `/himk/syl/{licence}` |
| 沪深数据中心 | 市净率排行 | `hsdc_himk_sjl()` | `/himk/sjl/{licence}` |
| 沪深数据中心 | ROE排行 | `hsdc_himk_roe()` | `/himk/roe/{licence}` |
| 沪深数据中心 | 今日交易提示 | `hsdc_jrts()` | `/hitc/jrts/{licence}` |
| 沪深数据中心 | 融资融券交易总量 | `hsdc_rzrqzl()` | `/hitc/rzrqzl/{licence}` |
| 沪深数据中心 | 融资融券交易明细 | `hsdc_rzrqmx()` | `/hitc/rzrqmx/{licence}` |
| 沪深数据中心 | 大宗交易 | `hsdc_dzjy()` | `/hitc/dzjy/{licence}` |
| 沪深数据中心 | 解禁限售 | `hsdc_jjxs()` | `/hitc/jjxs/{licence}` |
| 沪深数据中心 | 打新收益 | `hsdc_dxsy()` | `/hitc/dxsy/{licence}` |
| 沪深数据中心 | 历史累计分红 | `hsdc_lsfh()` | `/hitc/lsfh/{licence}` |
| 沪深数据中心 | 证监会行业 | `hsdc_hibk_zjhhy()` | `/hibk/zjhhy/{licence}` |
| 沪深数据中心 | 概念板块 | `hsdc_hibk_gnbk()` | `/hibk/gnbk/{licence}` |
| 沪深数据中心 | 利润细分 | `hsdc_hicw_lr()` | `/hicw/lr/{licence}` |
| 沪深数据中心 | 证监会行业资金路线图 | `hsdc_zjh()` | `/hizj/zjh/{licence}` |
| 沪深数据中心 | 概念板块资金路线图 | `hsdc_bk()` | `/hizj/bk/{licence}` |
| 沪深数据中心 | 个股阶段统计总览 | `hsdc_ggzl()` | `/hizj/ggzl/{licence}` |
| 沪深数据中心 | 主力连续净流入/流出 | `hsdc_lxlr()` | `/hizj/lxlr/{licence}` |
| 沪深数据中心 | 每日详情 | `hsdc_hilh_mrxq()` | `/hilh/mrxq/{licence}` |
| 沪深数据中心 | 机构席位成交明细 | `hsdc_hilh_xwmx()` | `/hilh/xwmx/{licence}` |
| 基金数据中心 | 开放式基金业绩排行（股、混合、债、QDII类） | `fundc_pm_kfpm()` | `/js/pm/kfpm/kfsjj_gpxjj_zsx/{licence}` |
| 基金数据中心 | 封闭式基金业绩排行 | `fundc_pm_fbpm()` | `/js/pm/fbpm/kfsjj_fbqy_ctfj/{licence}` |
| 基金数据中心 | 分级子基金业绩排行 | `fundc_pm_fzyj()` | `/js/pm/fzyj/kfsjj_fjgs_wjzqx/{licence}` |
| 基金数据中心 | 基金重仓股 | `fundc_other_jjzc(yyyy_j)` | `/js/other/jjzc/{yyyy_j}/{licence}` |
| 基金数据中心 | 基金重仓股变动 | `fundc_other_zcbd(yyyy_j)` | `/js/other/zcbd/{yyyy_j}/{licence}` |
| 基金数据中心 | 代销机构 | `fundc_other_dxjg()` | `/js/other/dxjg/yh/{licence}` |
| 基金数据中心 | 开放式基金净值排名（股、混合、债、QDII类） | `fundc_pm_kfjzg()` | `/js/pm/kfjzg/kfsjj_gpxjj_zsx/{licence}` |
| 基金数据中心 | 开放式基金净值排名（货币类） | `fundc_pm_kfjzq()` | `/js/pm/kfjzq/kfsjj_hbxjj_hba/{licence}` |
| 基金数据中心 | 封闭式基金净值排名 | `fundc_pm_fbjz()` | `/js/pm/fbjz/kfsjj_fbqy_ctfj/{licence}` |
| 基金数据中心 | 开放式基金基金分红 | `fundc_jf_kffh()` | `/js/jf/kffh/kfsjj_gpxjj_zsx/{licence}` |
| 基金数据中心 | 分级子基金基金分红 | `fundc_jf_fzfh()` | `/js/jf/fzfh/kfsjj_fjgs_wjzqx/{licence}` |
| 基金数据中心 | 开放式基金基金规模 | `fundc_gm_kfgm()` | `/js/gm/kfgm/kfsjj_gpxjj_zsx/{licence}` |
| 基金数据中心 | 封闭式基金基金规模 | `fundc_gm_fbgm()` | `/js/gm/fbgm/kfsjj_fbqy_ctfj/{licence}` |
| 基金数据中心 | 分级子基金基金规模 | `fundc_gm_fzgm()` | `/js/gm/fzgm/kfsjj_fjgs_wjzqx/{licence}` |
| 基金行情档案 | 历史净值 | `fundf10_lsjz(code)` | `/jj/lsjz/{code}/{licence}` |
| 基金行情档案 | 分红送配 | `fundf10_fhps(code)` | `/jj/fhps/{code}/{licence}` |
| 基金行情档案 | 阶段统计 | `fundf10_jdtj(code)` | `/jj/jdtj/{code}/{licence}` |
| 基金行情档案 | 季度涨幅明细 | `fundf10_jdzfmx(code)` | `/jj/jdzfmx/{code}/{licence}` |
| 基金行情档案 | 基金概况 | `fundf10_jjgk(code)` | `/jj/jjgk/{code}/{licence}` |
| 基金行情档案 | 基金业绩 | `fundf10_jjyj(code)` | `/jj/jjyj/{code}/{licence}` |
| 基金行情档案 | 基金分红 | `fundf10_jjfh(code)` | `/jj/jjfh/{code}/{licence}` |
| 基金行情档案 | 基金规模 | `fundf10_jjgm(code)` | `/jj/jjgm/{code}/{licence}` |
| 基金行情档案 | 估值基金列表 | `fundf10_gzlb()` | `/jj/gzlb/{licence}` |
| 基金行情档案 | 盘中最新估值 | `fundf10_pzzzgz(code)` | `/jj/pzzzgz/{code}/{licence}` |
| 基金行情档案 | 开放式基金净值 | `fundf10_hqzksjz(code)` | `/jj/hqzksjz/{code}/{licence}` |
| 基金行情档案 | 所有基金列表 | `fundf10_all()` | `/jj/all/{licence}` |
| 基金行情档案 | 在任基金经理列表 | `fundf10_zrjl()` | `/jj/zrjl/{licence}` |
| 基金行情档案 | 封闭式基金列表 | `fundf10_fbs()` | `/jj/fbs/{licence}` |
| 基金行情档案 | ETF基金列表 | `fundf10_etf()` | `/jj/etf/{licence}` |
| 基金行情档案 | LOF基金列表 | `fundf10_lof()` | `/jj/lof/{licence}` |
| 基金行情档案 | 股票持仓 | `fundf10_gpcc(code)` | `/jj/gpcc/{code}/{licence}` |
| 基金行情档案 | 债券持仓 | `fundf10_zqcc(code)` | `/jj/zqcc/{code}/{licence}` |
| 基金行情档案 | 行业配置 | `fundf10_hypz(code)` | `/jj/hypz/{code}/{licence}` |
| 基金行情档案 | 资产配置 | `fundf10_zcpz(code)` | `/jj/zcpz/{code}/{licence}` |
| 基金行情档案 | 规模变动 | `fundf10_gmbd(code)` | `/jj/gmbd/{code}/{licence}` |
| 基金行情档案 | 持有人结构 | `fundf10_cyrjg(code)` | `/jj/cyrjg/{code}/{licence}` |
| 量化因子 | 估值因子 | `factor_valuation(code)` | `/factor/valuation/{code}/{licence}` |
| 量化因子 | 质量因子 | `factor_quality(code)` | `/factor/quality/{code}/{licence}` |
| 量化因子 | 成长因子 | `factor_growth(code)` | `/factor/growth/{code}/{licence}` |
| 量化因子 | 动量因子 | `factor_momentum(code)` | `/factor/momentum/{code}/{licence}` |
| 量化因子 | 资金面因子 | `factor_capital(code)` | `/factor/capital/{code}/{licence}` |
| 量化因子 | 技术信号因子 | `factor_signal(code)` | `/factor/signal/{code}/{licence}` |
| 量化因子 | 风险因子 | `factor_risk(code)` | `/factor/risk/{code}/{licence}` |
| 量化因子 | 分红因子 | `factor_dividend(code)` | `/factor/dividend/{code}/{licence}` |
| 量化因子 | 规模流动性因子 | `factor_scale(code)` | `/factor/scale/{code}/{licence}` |
| 量化因子 | 情绪事件因子 | `factor_sentiment(code)` | `/factor/sentiment/{code}/{licence}` |
| 量化因子 | 单股全因子 | `factor_all(code)` | `/factor/all/{code}/{licence}` |
| 量化因子 | 因子列表 | `factor_list()` | `/factor/list/{licence}` |
| 量化因子 | 因子分类树 | `factor_categories()` | `/factor/categories/{licence}` |
| 量化因子 | 因子排名 | `factor_rank(factor_id)` | `/factor/rank/{factor_id}/{licence}` |
| 量化因子 | 因子 Top N | `factor_top(factor_id, arg)` | `/factor/top/{factor_id}/{arg}/{licence}` |
| 量化因子 | 因子历史序列 | `factor_history(factor_id, code)` | `/factor/history/{factor_id}/{code}/{licence}` |
| 量化因子 | 因子分位数 | `factor_percentile(factor_id, code)` | `/factor/percentile/{factor_id}/{code}/{licence}` |

<!-- SDK_1_2_0_MAP_END -->
