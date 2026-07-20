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
