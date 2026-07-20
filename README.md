# mairui — 麦蕊智数 Python SDK

面向 `https://api.mairuiapi.com`，覆盖官网 API 文档（如 [`https://mairuiapi.com/hsdata`](https://mairuiapi.com/hsdata)）中对外公开的全部接口。

源码仓库：[`https://github.com/MaiRuiApi/mairui`](https://github.com/MaiRuiApi/mairui)

## 安装

```bash
pip install mairui
```

尚未发布到 PyPI 时，可从本仓库安装：

```bash
pip install git+https://github.com/MaiRuiApi/mairui.git
# 或克隆后本地安装
git clone https://github.com/MaiRuiApi/mairui.git
cd mairui
pip install -e .
```

## 30 秒上手

```python
from mairui import Client

with Client(licence="YOUR-LICENCE-UUID") as api:
    # 股票列表
    stocks = api.stock_list()

    # 日线历史（可选 st/et/lt）
    bars = api.stock_history("000001.SZ", "d", "n", st="20240101", et="20241231")

    # 实时
    tick = api.stock_real_time("000001")

    # 财务
    bal = api.stock_balance("000001.SZ")

    # 批量并发（复用连接池）
    batch = api.map(
        api.stock_history,
        ["000001.SZ", "600519.SH", "000002.SZ"],
        period="d",
        dividend="n",
        lt=5,
        max_workers=8,
    )
```

只需绑定一次 `licence`，之后所有方法自动拼到 URL 末段。

## 设计要点（效率与工程）

| 措施 | 说明 |
|------|------|
| `requests.Session` + 连接池 | 默认 `pool_connections=32` / `pool_maxsize=64`，避免每次握手 |
| Gzip | 默认 `Accept-Encoding: gzip, deflate` |
| 自动重试 | 对 `429/502/503/504` 指数退避重试（仅 GET） |
| 超时 | 默认连接 5s / 读 60s，可构造时覆盖 |
| `api.map(...)` | 线程池批量拉多标的，适合回测灌数 |
| 路径编码 | 板块名等中文/特殊字符自动 `quote` |
| 异常分层 | `MairuiAuthError` / `MairuiTimeoutError` / `MairuiHTTPError` |

## 接口 ↔ 方法对照（摘要）

完整对照见 [API_METHOD_MAP.md](API_METHOD_MAP.md)。常用：

| 文档分类 | 示例方法 |
|----------|----------|
| 股票列表 | `stock_list` / `sectors_list` / `sector_detail` |
| 行情 / 指标 | `stock_history` / `stock_latest` / `stock_macd` / `stock_vip_history` |
| 实时 | `stock_real_time` / `stock_ssjy` / `stock_ssjy_more` / `stock_ssjy_all` |
| 财务 | `stock_balance` / `stock_income` / `stock_financial(table, code)` |
| F10 | `company_profile` / `company_dividends` / … |
| 股池 | `limit_up_pool(date)` / `limit_down_pool` / … |
| 指数 | `index_history` / `index_macd` / `index_list` |
| 北交所 | `bj_history` / `bj_balance` / … |
| 基金 / 科创 | `fund_list` / `etf_list` / `star_real_time` |

查询参数与文档一致：

- `st` / `et`：开始 / 结束时间（如 `20240101` 或 `20240101153000`）
- `lt`：最新条数（从尾部截取）

不传则返回服务端完整可用数据（由证书权限与数据存量决定）。

## 构造参数

```python
Client(
    licence="...",
    base_url="https://api.mairuiapi.com",  # 一般无需改
    timeout=(5, 60),
    max_retries=3,
    pool_connections=32,
    pool_maxsize=64,
)
```

## 异常处理

```python
from mairui import Client, MairuiAuthError, MairuiHTTPError, MairuiTimeoutError

try:
    with Client(licence="...") as api:
        print(api.stock_history("000001.SZ", "d", "n", lt=3))
except MairuiAuthError as e:
    print("证书问题", e)
except MairuiTimeoutError as e:
    print("超时", e)
except MairuiHTTPError as e:
    print("HTTP", e.status_code, e.payload)
```

## 目录

```text
mairui/
  __init__.py
  client.py      # 全部接口方法
  _http.py       # Session / 重试 / 编码
  exceptions.py
examples/
  quickstart.py
pyproject.toml
README.md
API_METHOD_MAP.md
LICENSE
```

## 说明

- 接口清单与官网文档页一致，例如沪深 A 股：[`https://mairuiapi.com/hsdata`](https://mairuiapi.com/hsdata)（同站还有指数、基金等文档入口）。
- SDK 默认请求主站 `https://api.mairuiapi.com`；证书可在官网获取。
- 本包为同步 SDK；若需 asyncio，可在外层用 `asyncio.to_thread` 包一层，或后续再发 async 版。
