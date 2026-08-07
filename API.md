# 麦蕊智数 SDK API 参考（python）

版本：**1.2.0**

基址默认：`https://api.mairuiapi.com`；路径末段 `{licence}` 由 Client 注入。

本文件由 `sdks/_tools/gen_api_md.py` 根据文档库目录生成。
既有沪深 A 股 / 指数 / 北交 / 科创等方法见各仓库 `API_METHOD_MAP.md`。

> 基金行情档案等接口即使官网文档页未展示（`visible=0`），只要网关可用仍已封装；调用规则与公开接口一致。

本批新增方法数：116（抽测跳过见 `sdks/_tools/sdk_api_skip_report.md`）。

## 沪深数据中心

### 个股资金流向

#### 净流入额排名

- **方法**：`hsdc_jlr()`
- **路径**：`/higg/jlr/{licence}`
- **更新频率**：每日15:40
- **说明**：个股净流入额倒序排列。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 服务器更新时间yyyy-MM-ddHH:mm:ss |
| `mc` | `string` | 名称 |
| `dm` | `string` | 代码 |
| `zxj` | `number` | 最新价（元） |
| `zdf` | `number` | 涨跌幅（%） |
| `hsl` | `number` | 换手率（%） |
| `cje` | `number` | 成交额（元） |
| `lczj` | `number` | 流出资金（元） |
| `lrzj` | `number` | 流入资金（元） |
| `jlr` | `string` | 净流入（元） |
| `jlrl` | `string` | 净流入率（%） |

#### 净流入率排名

- **方法**：`hsdc_jlrl()`
- **路径**：`/higg/jlrl/{licence}`
- **更新频率**：每日15:40
- **说明**：个股净流入率倒序排列。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 服务器更新时间yyyy-MM-ddHH:mm:ss |
| `mc` | `string` | 名称 |
| `dm` | `string` | 代码 |
| `zxj` | `number` | 最新价（元） |
| `zdf` | `number` | 涨跌幅（%） |
| `hsl` | `number` | 换手率（%） |
| `cje` | `number` | 成交额（元） |
| `lczj` | `number` | 流出资金（元） |
| `lrzj` | `number` | 流入资金（元） |
| `jlr` | `string` | 净流入（元） |
| `jlrl` | `string` | 净流入率（%） |

#### 主力净流入额排名

- **方法**：`hsdc_zljlr()`
- **路径**：`/higg/zljlr/{licence}`
- **更新频率**：每日15:40
- **说明**：个股主力净流入额倒序排列。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 服务器更新时间yyyy-MM-ddHH:mm:ss |
| `mc` | `string` | 名称 |
| `dm` | `string` | 代码 |
| `zxj` | `number` | 最新价（元） |
| `zdf` | `number` | 涨跌幅（%） |
| `hsl` | `number` | 换手率（%） |
| `cje` | `number` | 成交额（元） |
| `zllczj` | `number` | 主力流出资金（元） |
| `zllrzj` | `number` | 主力流入资金（元） |
| `zljlr` | `number` | 主力净流入（元） |
| `zljlrl` | `number` | 主力净流入率（%） |
| `lczj` | `number` | 流出资金(元)，与zllczj同值 |
| `lrzj` | `number` | 流入资金(元)，与zllrzj同值 |
| `jlr` | `number` | 净流入(元)，与zljlr同值 |
| `jlrl` | `number` | 净流入率(%)，与zljlrl同值 |

#### 主力净流入率排名

- **方法**：`hsdc_zljlrl()`
- **路径**：`/higg/zljlrl/{licence}`
- **更新频率**：每日15:40
- **说明**：个股主力净流入率倒序排列。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 服务器更新时间yyyy-MM-ddHH:mm:ss |
| `mc` | `string` | 名称 |
| `dm` | `string` | 代码 |
| `zxj` | `number` | 最新价（元） |
| `zdf` | `number` | 涨跌幅（%） |
| `hsl` | `number` | 换手率（%） |
| `cje` | `number` | 成交额（元） |
| `zllczj` | `number` | 主力流出资金（元） |
| `zllrzj` | `number` | 主力流入资金（元） |
| `zljlr` | `number` | 主力净流入（元） |
| `zljlrl` | `number` | 主力净流入率（%） |
| `lczj` | `number` | 流出资金(元)，与zllczj同值 |
| `lrzj` | `number` | 流入资金(元)，与zllrzj同值 |
| `jlr` | `number` | 净流入(元)，与zljlr同值 |
| `jlrl` | `number` | 净流入率(%)，与zljlrl同值 |

#### 散户净流入额排名

- **方法**：`hsdc_shzlr()`
- **路径**：`/higg/shzlr/{licence}`
- **更新频率**：每日15:40
- **说明**：个股散户净流入额倒序排列。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 服务器更新时间yyyy-MM-ddHH:mm:ss |
| `mc` | `string` | 名称 |
| `dm` | `string` | 代码 |
| `zxj` | `number` | 最新价（元） |
| `zdf` | `number` | 涨跌幅（%） |
| `hsl` | `number` | 换手率（%） |
| `cje` | `number` | 成交额（元） |
| `shlczj` | `number` | 散户流出资金（元） |
| `shlrzj` | `number` | 散户流入资金（元） |
| `shjlr` | `number` | 散户净流入（元） |
| `shjlrl` | `number` | 散户净流入率（%） |
| `lczj` | `number` | 流出资金(元)，与shlczj同值 |
| `lrzj` | `number` | 流入资金(元)，与shlrzj同值 |
| `jlr` | `number` | 净流入(元)，与shjlr同值 |
| `jlrl` | `number` | 净流入率(%)，与shjlrl同值 |

#### 散户净流入率排名

- **方法**：`hsdc_shjlrl()`
- **路径**：`/higg/shjlrl/{licence}`
- **更新频率**：每日15:40
- **说明**：个股散户净流入率倒序排列。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 服务器更新时间yyyy-MM-ddHH:mm:ss |
| `mc` | `string` | 名称 |
| `dm` | `string` | 代码 |
| `zxj` | `number` | 最新价（元） |
| `zdf` | `number` | 涨跌幅（%） |
| `hsl` | `number` | 换手率（%） |
| `cje` | `number` | 成交额（元） |
| `shlczj` | `number` | 散户流出资金（元） |
| `shlrzj` | `number` | 散户流入资金（元） |
| `shjlr` | `number` | 散户净流入（元） |
| `shjlrl` | `number` | 散户净流入率（%） |
| `lczj` | `number` | 流出资金(元)，与shlczj同值 |
| `lrzj` | `number` | 流入资金(元)，与shlrzj同值 |
| `jlr` | `number` | 净流入(元)，与shjlr同值 |
| `jlrl` | `number` | 净流入率(%)，与shjlrl同值 |

### 南向、北向资金

#### 最新资金流向概览

- **方法**：`hsdc_nbzj_lxgl()`
- **路径**：`/ht/nbzj/lxgl/{licence}`
- **更新频率**：每日20:10
- **说明**：当前交易日的南向、北向最新资金流向概览。

| 字段 | 类型 | 说明 |
|------|------|------|
| `type` | `string` | 类型:沪港通/沪港通/深港通/深港通 |
| `tname` | `string` | 板块:沪股通(港>沪)
/港股通(沪>港)/深股通(港>深)/港股通(深>港)。港股通(沪)代表沪港通的港股通部分，港股通(深)代表深港通的港股通部分。 |
| `dir` | `string` | 资金方向:北向/南向。香港投资者交易内地股票，称为北向资金，内地投资者交易香港股票，称为南向资金。北向资金包含沪股通和深股通两部分。南向资金包含港股通(沪)和港股通(深)两部分。 |
| `netbuy` | `number` | 成交净买额，单位（万）。当日成交净买额=买入成交额-卖出成交额 |
| `netin` | `number` | 资金净流入，单位（万）:当日资金流入额=当日限额-当日余额。当日资金流入额包含两部分：当日成交净买额，当日申报但未成交的买单金额。 |
| `remain` | `number` | 当日资金余额，单位（万） |
| `up` | `number` | 上涨股票数 |
| `ping` | `number` | 持平股票数 |
| `down` | `number` | 下跌股票数 |
| `idx` | `number` | 相关指数 |
| `idxdm` | `number` | 相关指数代码 |
| `idxzd` | `number` | 相关指数涨跌幅（%） |
| `status` | `number` | 交易状态。3:收盘，4:休市 |

#### 北向资金历史走势

- **方法**：`hsdc_nbzj_bxls(jd)`
- **路径**：`/ht/nbzj/bxls/{jd}/{licence}`
- **更新频率**：每日20:10
- **说明**：北向资金历史每天走势。可通过阶段参数可选近一月、近六月、近一年、全部的历史数据，对应的参数为1、6、12、all，按照交易日升序排序。

路径参数：
- `jd`

| 字段 | 类型 | 说明 |
|------|------|------|
| `bx` | `number` | 北向资金净流入（百万） |
| `hgt` | `number` | 沪股通净流入（百万） |
| `sgt` | `number` | 深股通净流入（百万） |
| `t` | `string` | 日期：yyyy-MM-dd |

#### 南向资金历史走势

- **方法**：`hsdc_nbzj_nxls(jd)`
- **路径**：`/ht/nbzj/nxls/{jd}/{licence}`
- **更新频率**：每日20:10
- **说明**：南向资金历史每天走势。可通过阶段参数可选近一月、近六月、近一年、全部的历史数据，对应的参数为1、6、12、all，按照交易日升序排序。

路径参数：
- `jd`

| 字段 | 类型 | 说明 |
|------|------|------|
| `nx` | `number` | 南向资金净流入（百万） |
| `ggth` | `number` | 港股通（沪）净流入（百万） |
| `ggts` | `number` | 港股通（深）净流入（百万） |
| `t` | `string` | 日期：yyyy-MM-dd |

#### 北向资金历史总览

- **方法**：`hsdc_nbzj_bxzl()`
- **路径**：`/ht/nbzj/bxzl/{licence}`
- **更新频率**：每日20:10
- **说明**：北向资金历史累计净流入总览（含北向合计、沪股通、深股通）。当前接口仅返回累计口径字段 bxall/hgtall/sgtall，不含分阶段(1个月/6个月/1年)字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `bxall` | `number` | 北向资金历史累计净流入(万元) |
| `hgtall` | `number` | 沪股通历史累计净流入(万元) |
| `sgtall` | `number` | 深股通历史累计净流入(万元) |

#### 南向资金历史总览

- **方法**：`hsdc_nbzj_nxzl()`
- **路径**：`/ht/nbzj/nxzl/{licence}`
- **更新频率**：每日20:10
- **说明**：南向资金历史总览。

| 字段 | 类型 | 说明 |
|------|------|------|
| `nx1m` | `number` | 南向资金近一月净流入（百万） |
| `ggth1m` | `number` | 港股通（沪）近一月净流入（百万） |
| `ggts1m` | `number` | 港股通（深）近一月净流入（百万） |
| `nx6m` | `number` | 南向资金近六月净流入（百万） |
| `ggth6m` | `number` | 港股通（沪）近六月净流入（百万） |
| `ggts6m` | `number` | 港股通（深）近六月净流入（百万） |
| `nx1y` | `number` | 南向资金近一年净流入（百万） |
| `ggth1y` | `number` | 港股通（沪）近一年净流入（百万） |
| `ggts1y` | `number` | 港股通（深）近一年净流入（百万） |
| `nxall` | `number` | 南向资金历史净流入（百万） |
| `ggthall` | `number` | 港股通（沪）历史净流入（百万） |
| `ggtsall` | `number` | 港股通（深）历史净流入（百万） |

#### 沪股通成分股行情

- **方法**：`hsdc_nbzj_hgtc()`
- **路径**：`/ht/nbzj/hgtc/{licence}`
- **更新频率**：每日20:10
- **说明**：沪股通（港>沪）成分股行情明细，按涨跌幅降序。

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `fm` | `number` | 五分钟涨跌幅（%） |
| `h` | `number` | 最高价（元） |
| `hs` | `number` | 换手（%） |
| `lb` | `number` | 量比（%） |
| `l` | `number` | 最低价（元） |
| `lt` | `number` | 流通市值（元） |
| `o` | `number` | 开盘价（元） |
| `pe` | `number` | 市盈率（动态，总市值除以预估全年净利润，例如当前公布一季度净利润1000万，则预估全年净利润4000万） |
| `pc` | `number` | 涨跌幅（%） |
| `p` | `number` | 当前价格（元） |
| `sz` | `number` | 总市值（元） |
| `cje` | `number` | 成交额（元） |
| `ud` | `number` | 涨跌额（元） |
| `v` | `number` | 成交量（手） |
| `yc` | `number` | 昨日收盘价（元） |
| `zf` | `number` | 振幅（%） |
| `zs` | `number` | 涨速（%） |
| `sjl` | `number` | 市净率 |
| `zdf60` | `number` | 60日涨跌幅（%） |
| `zdfnc` | `number` | 年初至今涨跌幅（%） |
| `t` | `string` | 更新时间yyyy-MM-ddHH:mm:ss |

#### 深股通成分股行情

- **方法**：`hsdc_nbzj_sgtc()`
- **路径**：`/ht/nbzj/sgtc/{licence}`
- **更新频率**：每日20:10
- **说明**：深股通（港>深）成分股行情明细，按涨跌幅降序。

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `fm` | `number` | 五分钟涨跌幅（%） |
| `h` | `number` | 最高价（元） |
| `hs` | `number` | 换手（%） |
| `lb` | `number` | 量比（%） |
| `l` | `number` | 最低价（元） |
| `lt` | `number` | 流通市值（元） |
| `o` | `number` | 开盘价（元） |
| `pe` | `number` | 市盈率（动态，总市值除以预估全年净利润，例如当前公布一季度净利润1000万，则预估全年净利润4000万） |
| `pc` | `number` | 涨跌幅（%） |
| `p` | `number` | 当前价格（元） |
| `sz` | `number` | 总市值（元） |
| `cje` | `number` | 成交额（元） |
| `ud` | `number` | 涨跌额（元） |
| `v` | `number` | 成交量（手） |
| `yc` | `number` | 昨日收盘价（元） |
| `zf` | `number` | 振幅（%） |
| `zs` | `number` | 涨速（%） |
| `sjl` | `number` | 市净率 |
| `zdf60` | `number` | 60日涨跌幅（%） |
| `zdfnc` | `number` | 年初至今涨跌幅（%） |
| `t` | `string` | 更新时间yyyy-MM-ddHH:mm:ss |

#### 港股通（沪）成分股行情

- **方法**：`hsdc_nbzj_ggth()`
- **路径**：`/ht/nbzj/ggth/{licence}`
- **更新频率**：每日20:10
- **说明**：港股通（沪）成分股行情明细，按涨跌幅降序。
【说明·2026-08】实测东财板块 b:DLMK0146（沪）与 b:DLMK0144（深）成分列表可能完全一致；两接口仍分别落盘，使用时请以源站网页交叉核对。

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `h` | `number` | 最高价（港元） |
| `l` | `number` | 最低价（港元） |
| `o` | `number` | 开盘价（港元） |
| `pc` | `number` | 涨跌幅（%） |
| `p` | `number` | 当前价格（港元） |
| `cje` | `number` | 成交额（港元） |
| `ud` | `number` | 涨跌额（港元） |
| `v` | `number` | 成交量（股） |
| `yc` | `number` | 昨日收盘价（元） |
| `t` | `string` | 更新时间yyyy-MM-ddHH:mm:ss |

#### 港股通（深）成分股行情

- **方法**：`hsdc_nbzj_ggts()`
- **路径**：`/ht/nbzj/ggts/{licence}`
- **更新频率**：每日20:10
- **说明**：港股通（深）成分股行情明细，按涨跌幅降序。
【说明·2026-08】实测东财板块 b:DLMK0144（深）与 b:DLMK0146（沪）成分列表可能完全一致；两接口仍分别落盘，使用时请以源站网页交叉核对。

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `h` | `number` | 最高价（港元） |
| `l` | `number` | 最低价（港元） |
| `o` | `number` | 开盘价（港元） |
| `pc` | `number` | 涨跌幅（%） |
| `p` | `number` | 当前价格（港元） |
| `cje` | `number` | 成交额（港元） |
| `ud` | `number` | 涨跌额（港元） |
| `v` | `number` | 成交量（股） |
| `yc` | `number` | 昨日收盘价（元） |
| `t` | `string` | 更新时间yyyy-MM-ddHH:mm:ss |

#### AH股比价

- **方法**：`hsdc_nbzj_ah()`
- **路径**：`/ht/nbzj/ah/{licence}`
- **更新频率**：每日20:10
- **说明**：AH股比价，按涨跌幅降序。

| 字段 | 类型 | 说明 |
|------|------|------|
| `mc` | `string` | 名称 |
| `hdm` | `string` | H股代码 |
| `hzxj` | `number` | H股最新价（HKD） |
| `hzdf` | `number` | H股涨跌幅（%） |
| `adm` | `string` | A股代码 |
| `azxj` | `number` | A股最新价（RMB） |
| `azdf` | `number` | A股涨跌幅（%） |
| `ahbj` | `number` | 比价（A/H） |
| `ahyj` | `number` | 溢价（A/H）% |
| `t` | `string` | 更新时间yyyy-MM-ddHH:mm:ss |

#### 沪股通十大成交股

- **方法**：`hsdc_nbzj_hgts()`
- **路径**：`/ht/nbzj/hgts/{licence}`
- **更新频率**：每日20:10
- **说明**：沪股通近30个交易日十大成交股，按日期倒序。

| 字段 | 类型 | 说明 |
|------|------|------|
| `pm` | `number` | 排名 |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `c` | `number` | 收盘价（元） |
| `zdf` | `number` | 涨跌幅（%） |
| `jm` | `number` | 沪股通净买额（元） |
| `mr` | `number` | 沪股通买入额（元） |
| `mce` | `number` | 沪股通卖出额（元） |
| `cj` | `number` | 沪股通成交额（元） |
| `t` | `string` | 日期yyyy-MM-dd |

#### 深股通十大成交股

- **方法**：`hsdc_nbzj_sgts()`
- **路径**：`/ht/nbzj/sgts/{licence}`
- **更新频率**：每日20:10
- **说明**：深股通近30个交易日十大成交股，按日期倒序。

| 字段 | 类型 | 说明 |
|------|------|------|
| `pm` | `number` | 排名 |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `c` | `number` | 收盘价（元） |
| `zdf` | `number` | 涨跌幅（%） |
| `jm` | `number` | 深股通净买额（元） |
| `mr` | `number` | 深股通买入额（元） |
| `mce` | `number` | 深股通卖出额（元） |
| `cj` | `number` | 深股通成交额（元） |
| `t` | `string` | 日期yyyy-MM-dd |

#### 港股通（沪）十大成交股

- **方法**：`hsdc_nbzj_hcjd()`
- **路径**：`/ht/nbzj/hcjd/{licence}`
- **更新频率**：每日20:10
- **说明**：港股通（沪）近30个交易日十大成交股，按日期倒序。

| 字段 | 类型 | 说明 |
|------|------|------|
| `pm` | `number` | 排名 |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `c` | `number` | 收盘价（港元） |
| `zdf` | `number` | 涨跌幅（%） |
| `jm` | `number` | 港股通（沪）净买额（港元） |
| `mr` | `number` | 港股通（沪）买入额（港元） |
| `mce` | `number` | 港股通（沪）卖出额（港元） |
| `cj` | `number` | 港股通（沪）成交额（港元） |
| `t` | `string` | 日期yyyy-MM-dd |

#### 港股通（深）十大成交股

- **方法**：`hsdc_nbzj_scjd()`
- **路径**：`/ht/nbzj/scjd/{licence}`
- **更新频率**：每日20:10
- **说明**：港股通（深）近30个交易日十大成交股，按日期倒序。

| 字段 | 类型 | 说明 |
|------|------|------|
| `pm` | `number` | 排名 |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `c` | `number` | 收盘价（港元） |
| `zdf` | `number` | 涨跌幅（%） |
| `jm` | `number` | 港股通（深）净买额（港元） |
| `mr` | `number` | 港股通（深）买入额（港元） |
| `mce` | `number` | 港股通（深）卖出额（港元） |
| `cj` | `number` | 港股通（深）成交额（港元） |
| `t` | `string` | 日期yyyy-MM-dd |

#### 北向个股周期排名

- **方法**：`hsdc_nbzj_bxpm(zq)`
- **路径**：`/ht/nbzj/bxpm/{zq}/{licence}`
- **更新频率**：每季度（季末披露后更新；非每日更新）
- **说明**：【口径变更·2026-08】上游北向个股日频持股明细已停更，本接口降级为「季频持股快照」。
数据为最近季末（或上游最近一次披露日）北向合计持股排名，按持股市值倒序；不再提供 d/3/5/10/m/q/y 等多周期日频增持排名。
字段说明：jrcg/jrsz/jrltb/jrzgbb 等为快照日持股；zqzc/zqsz/zqszzf/zqltb/zqzgbb 等周期增持类字段上游已不披露，当前多为 null；落盘可含 t（快照日）与 _freq=quarterly。
正式落盘路径：all/nxbx/bxggpm（及 LD）。

路径参数：
- `zq`

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `ssbk` | `string` | 所属板块 |
| `c` | `number` | 快照日收盘价（元） |
| `zdf` | `number` | 快照日涨跌幅（%） |
| `jrcg` | `number` | 持股股数（万股，季末/快照日） |
| `jrsz` | `number` | 持股市值（万元，季末/快照日） |
| `jrltb` | `number` | 持股占流通股比（%，季末/快照日） |
| `jrzgbb` | `number` | 持股占总股本比（%，季末/快照日） |
| `zqzc` | `number` | 周期增持估计股数（万股）——上游日频停更后多为 null |
| `zqsz` | `number` | 周期增持估计市值（万元）——上游日频停更后多为 null |
| `zqszzf` | `number` | 周期增持估计市值增幅（%）——上游日频停更后多为 null |
| `zqltb` | `number` | 周期增持估计占流通股比（%）——上游日频停更后多为 null |
| `zqzgbb` | `number` | 周期增持估计占总股本比（%）——上游日频停更后多为 null |
| `t` | `string` | 快照日期（季末或上游最近披露日，YYYY-MM-DD） |
| `_freq` | `string` | 更新频率标记；季频降级后为 quarterly |

#### 沪股通个股周期排名

- **方法**：`hsdc_nbzj_hgpm(zq)`
- **路径**：`/ht/nbzj/hgpm/{zq}/{licence}`
- **更新频率**：每季度（季末披露后更新；非每日更新）
- **说明**：【口径变更·2026-08】上游北向个股日频持股明细已停更，本接口降级为「季频持股快照」（沪股通 MUTUAL_TYPE=001）。
数据为最近季末沪股通持股排名，按持股市值倒序；不再提供多周期日频增持排名。
周期增持类字段（zq*）当前多为 null；落盘可含 t、_freq=quarterly。
正式落盘路径：all/nxbx/bxhgtpm（及 LD）。

路径参数：
- `zq`

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `ssbk` | `string` | 所属板块 |
| `c` | `number` | 快照日收盘价（元） |
| `zdf` | `number` | 快照日涨跌幅（%） |
| `jrcg` | `number` | 持股股数（万股，季末/快照日） |
| `jrsz` | `number` | 持股市值（万元，季末/快照日） |
| `jrltb` | `number` | 持股占流通股比（%，季末/快照日） |
| `jrzgbb` | `number` | 持股占总股本比（%，季末/快照日） |
| `zqzc` | `number` | 周期增持估计股数（万股）——上游日频停更后多为 null |
| `zqsz` | `number` | 周期增持估计市值（万元）——上游日频停更后多为 null |
| `zqszzf` | `number` | 周期增持估计市值增幅（%）——上游日频停更后多为 null |
| `zqltb` | `number` | 周期增持估计占流通股比（%）——上游日频停更后多为 null |
| `zqzgbb` | `number` | 周期增持估计占总股本比（%）——上游日频停更后多为 null |
| `t` | `string` | 快照日期（季末或上游最近披露日，YYYY-MM-DD） |
| `_freq` | `string` | 更新频率标记；季频降级后为 quarterly |

#### 深股通个股周期排名

- **方法**：`hsdc_nbzj_sgpm(zq)`
- **路径**：`/ht/nbzj/sgpm/{zq}/{licence}`
- **更新频率**：每季度（季末披露后更新；非每日更新）
- **说明**：【口径变更·2026-08】上游北向个股日频持股明细已停更，本接口降级为「季频持股快照」（深股通 MUTUAL_TYPE=003）。
数据为最近季末深股通持股排名，按持股市值倒序；不再提供多周期日频增持排名。
周期增持类字段（zq*）当前多为 null；落盘可含 t、_freq=quarterly。
正式落盘路径：all/nxbx/bxsgtpm（及 LD）。

路径参数：
- `zq`

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `ssbk` | `string` | 所属板块 |
| `c` | `number` | 快照日收盘价（元） |
| `zdf` | `number` | 快照日涨跌幅（%） |
| `jrcg` | `number` | 持股股数（万股，季末/快照日） |
| `jrsz` | `number` | 持股市值（万元，季末/快照日） |
| `jrltb` | `number` | 持股占流通股比（%，季末/快照日） |
| `jrzgbb` | `number` | 持股占总股本比（%，季末/快照日） |
| `zqzc` | `number` | 周期增持估计股数（万股）——上游日频停更后多为 null |
| `zqsz` | `number` | 周期增持估计市值（万元）——上游日频停更后多为 null |
| `zqszzf` | `number` | 周期增持估计市值增幅（%）——上游日频停更后多为 null |
| `zqltb` | `number` | 周期增持估计占流通股比（%）——上游日频停更后多为 null |
| `zqzgbb` | `number` | 周期增持估计占总股本比（%）——上游日频停更后多为 null |
| `t` | `string` | 快照日期（季末或上游最近披露日，YYYY-MM-DD） |
| `_freq` | `string` | 更新频率标记；季频降级后为 quarterly |

#### 沪股通历史数据

- **方法**：`hsdc_nbzj_hgls()`
- **路径**：`/ht/nbzj/hgls/{licence}`
- **更新频率**：每日20:10
- **说明**：沪股通（港→沪）历史数据，按日期倒序。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期 |
| `jme` | `number` | 当日成交净买额（百万）：当日成交净买额=买入成交额-卖出成交额。 |
| `mr` | `number` | 买入成交额（百万） |
| `mc` | `number` | 卖出成交额（百万） |
| `lj` | `number` | 历史累计净买额（百万） |
| `drlr` | `number` | 当日资金流入（百万）：当日资金流入额=当日限额-当日余额。当日资金流入额包含两部分：当日成交净买额，当日申报但未成交的买单金额。 |
| `drye` | `number` | 当日余额（百万） |
| `lzgdm` | `string` | 领涨股代码 |
| `lzgmc` | `string` | 领涨股名称 |
| `lzgzdf` | `number` | 领涨股涨跌幅（%） |
| `zs` | `number` | 上证指数点位 |
| `zszdf` | `number` | 指数涨跌幅（%） |

#### 深股通历史数据

- **方法**：`hsdc_nbzj_shls()`
- **路径**：`/ht/nbzj/shls/{licence}`
- **更新频率**：每日20:10
- **说明**：深股通（港→深）历史数据，按日期倒序。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期 |
| `jme` | `number` | 当日成交净买额（百万）：当日成交净买额=买入成交额-卖出成交额。 |
| `mr` | `number` | 买入成交额（百万） |
| `mc` | `number` | 卖出成交额（百万） |
| `lj` | `number` | 历史累计净买额（百万） |
| `drlr` | `number` | 当日资金流入（百万）：当日资金流入额=当日限额-当日余额。当日资金流入额包含两部分：当日成交净买额，当日申报但未成交的买单金额。 |
| `drye` | `number` | 当日余额（百万） |
| `lzgdm` | `string` | 领涨股代码 |
| `lzgmc` | `string` | 领涨股名称 |
| `lzgzdf` | `number` | 领涨股涨跌幅（%） |
| `zs` | `number` | 深证指数点位 |
| `zszdf` | `number` | 指数涨跌幅（%） |

#### 港股通（沪）历史数据

- **方法**：`hsdc_nbzj_ghls()`
- **路径**：`/ht/nbzj/ghls/{licence}`
- **更新频率**：每日20:10
- **说明**：港深股通（沪→港）历史数据，按日期倒序。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期 |
| `jme` | `number` | 当日成交净买额（百万）：当日成交净买额=买入成交额-卖出成交额。 |
| `mr` | `number` | 买入成交额（百万） |
| `mc` | `number` | 卖出成交额（百万） |
| `lj` | `number` | 历史累计净买额（百万） |
| `drlr` | `number` | 当日资金流入（百万）：当日资金流入额=当日限额-当日余额。当日资金流入额包含两部分：当日成交净买额，当日申报但未成交的买单金额。 |
| `drye` | `number` | 当日余额（百万） |
| `lzgdm` | `string` | 领涨股代码 |
| `lzgmc` | `string` | 领涨股名称 |
| `lzgzdf` | `number` | 领涨股涨跌幅（%） |
| `zs` | `number` | 恒生指数点位 |
| `zszdf` | `number` | 指数涨跌幅（%） |

#### 港股通（深）历史数据

- **方法**：`hsdc_nbzj_gsls()`
- **路径**：`/ht/nbzj/gsls/{licence}`
- **更新频率**：每日20:10
- **说明**：港深股通（深→港）历史数据，按日期倒序。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期 |
| `jme` | `number` | 当日成交净买额（百万）：当日成交净买额=买入成交额-卖出成交额。 |
| `mr` | `number` | 买入成交额（百万） |
| `mc` | `number` | 卖出成交额（百万） |
| `lj` | `number` | 历史累计净买额（百万） |
| `drlr` | `number` | 当日资金流入（百万）：当日资金流入额=当日限额-当日余额。当日资金流入额包含两部分：当日成交净买额，当日申报但未成交的买单金额。 |
| `drye` | `number` | 当日余额（百万） |
| `lzgdm` | `string` | 领涨股代码 |
| `lzgmc` | `string` | 领涨股名称 |
| `lzgzdf` | `number` | 领涨股涨跌幅（%） |
| `zs` | `number` | 恒生指数点位 |
| `zszdf` | `number` | 指数涨跌幅（%） |

### 可转债(内测)

#### 可转债一览

- **方法**：`hsdc_list()`
- **路径**：`/kzz/list/{licence}`
- **更新频率**：每个交易日盘后（采集任务调度）
- **说明**：可转债一览：含转债代码/名称、正股信息、转股价/溢价率、发行与评级等基础档案。

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 可转债代码 |
| `mc` | `string` | 可转债简称 |
| `sg_t` | `string` | 申购日期 |
| `sgdm` | `string` | 申购代码 |
| `sgsx` | `number` | 申购上限（万元） |
| `zgdm` | `string` | 正股代码 |
| `zgmc` | `string` | 正股简称 |
| `zgsj` | `number` | 正股价格 |
| `zgjg` | `number` | 转股价格 |
| `zgjz` | `number` | 转股价值 |
| `zxj` | `number` | 转债现价 |
| `yjl` | `number` | 转股溢价率% |
| `gqdjr` | `string` | 原股东配售股权登记日 |
| `mgpse` | `string` | 每股配售额 |
| `fxgm` | `number` | 发行规模（亿元） |
| `zqh` | `string` | 中签号发布日 |
| `zql` | `number` | 中签率% |
| `sssj` | `string` | 上市时间 |
| `pj` | `string` | 信用评级 |

#### 可转债比价表

- **方法**：`hsdc_comparison()`
- **路径**：`/kzz/comparison/{licence}`
- **更新频率**：每个交易日盘后（采集任务调度）
- **说明**：可转债比价表：转债与正股行情对比，含溢价率、纯债价值、回售/强赎触发价等。

| 字段 | 类型 | 说明 |
|------|------|------|
| `xh` | `number` | 序号 |
| `dm` | `string` | 转债代码 |
| `mc` | `string` | 转债名称 |
| `zxj` | `number` | 转债最新价 |
| `zdf` | `number` | 转债涨跌幅% |
| `zgdm` | `string` | 正股代码 |
| `zgmc` | `string` | 正股名称 |
| `zgzxj` | `number` | 正股最新价 |
| `zgzdf` | `number` | 正股涨跌幅% |
| `zgjg` | `number` | 转股价 |
| `zgjz` | `number` | 转股价值 |
| `yjl` | `number` | 转股溢价率% |
| `czyjl` | `number` | 纯债溢价率% |
| `hscfj` | `number` | 回售触发价 |
| `qscfj` | `number` | 强赎触发价 |
| `dqshj` | `number` | 到期赎回价 |
| `czjz` | `number` | 纯债价值 |
| `kszgr` | `string` | 开始转股日 |
| `ssrq` | `string` | 上市日期 |
| `sgrq` | `string` | 申购日期 |

#### 可转债实时行情

- **方法**：`hsdc_spot()`
- **路径**：`/kzz/spot/{licence}`
- **更新频率**：每个交易日盘后（采集任务调度）
- **说明**：可转债实时行情：最新价、涨跌幅、买卖盘、开高低、成交量额等。

| 字段 | 类型 | 说明 |
|------|------|------|
| `symbol` | `string` | 带市场前缀代码，如 sh113052 |
| `code` | `string` | 纯数字代码 |
| `name` | `string` | 名称 |
| `trade` | `number` | 最新价 |
| `pricechange` | `number` | 涨跌额 |
| `changepercent` | `number` | 涨跌幅% |
| `buy` | `number` | 买一价 |
| `sell` | `number` | 卖一价 |
| `settlement` | `number` | 昨收 |
| `open` | `number` | 开盘 |
| `high` | `number` | 最高 |
| `low` | `number` | 最低 |
| `volume` | `number` | 成交量 |
| `amount` | `number` | 成交额 |
| `ticktime` | `string` | 行情时间 HH:MM:SS |

### 市场表现

#### 阶段最高最低

- **方法**：`hsdc_himk_jdzgzd()`
- **路径**：`/himk/jdzgzd/{licence}`
- **更新频率**：每日20:10
- **说明**：市场中所有股票与指数的阶段性（近5日、10日、20日、60日）的最高最低价以及涨跌幅。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `g5` | `number` | 近5日最高价 |
| `d5` | `number` | 近5日最低价 |
| `zd5` | `number` | 近5日涨跌幅（%） |
| `iscq5` | `number` | 近5日是否除权除息（0：否，1：是） |
| `g10` | `number` | 近10日最高价 |
| `d10` | `number` | 近10日最低价 |
| `zd10` | `number` | 近10日涨跌幅（%） |
| `iscq10` | `number` | 近10日是否除权除息（0：否，1：是） |
| `g20` | `number` | 近20日最高价 |
| `d20` | `number` | 近20日最低价 |
| `zd20` | `number` | 近20日涨跌幅（%） |
| `iscq20` | `number` | 近20日是否除权除息（0：否，1：是） |
| `g60` | `number` | 近60日最高价 |
| `d60` | `number` | 近60日最低价 |
| `zd60` | `number` | 近60日涨跌幅（%） |
| `iscq60` | `number` | 近60日是否除权除息（0：否，1：是） |

#### 盘中创新高个股

- **方法**：`hsdc_himk_pzxg()`
- **路径**：`/himk/pzxg/{licence}`
- **更新频率**：每日20:10
- **说明**：沪深A股今日创最近30个交易日内价格新高的股票。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `c` | `number` | 收盘价 |
| `h` | `number` | 最高价 |
| `l` | `number` | 最低价 |
| `zdf` | `number` | 涨跌幅（%） |
| `iscq` | `number` | 当天是否除权除息（0：否，1：是） |
| `hs` | `number` | 换手率（%） |
| `zdf5` | `number` | 5日涨跌幅（%） |
| `iscq5` | `number` | 近5日是否除权除息（0：否，1：是） |
| `zdf10` | `number` | 10日涨跌幅（%） |
| `iscq10` | `number` | 近10日是否除权除息（0：否，1：是） |
| `zdf20` | `number` | 20日涨跌幅（%） |
| `iscq20` | `number` | 近20日是否除权除息（0：否，1：是） |

#### 盘中创新低个股

- **方法**：`hsdc_himk_pzxd()`
- **路径**：`/himk/pzxd/{licence}`
- **更新频率**：每日20:10
- **说明**：沪深A股今日创最近30个交易日内价格新低的股票。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `c` | `number` | 收盘价 |
| `h` | `number` | 最高价 |
| `l` | `number` | 最低价 |
| `zdf` | `number` | 涨跌幅（%） |
| `iscq` | `number` | 当天是否除权除息（0：否，1：是） |
| `hs` | `number` | 换手率（%） |
| `zdf5` | `number` | 5日涨跌幅（%） |
| `iscq5` | `number` | 近5日是否除权除息（0：否，1：是） |
| `zdf10` | `number` | 10日涨跌幅（%） |
| `iscq10` | `number` | 近10日是否除权除息（0：否，1：是） |
| `zdf20` | `number` | 20日涨跌幅（%） |
| `iscq20` | `number` | 近20日是否除权除息（0：否，1：是） |

#### 成交骤增个股

- **方法**：`hsdc_himk_cjzz()`
- **路径**：`/himk/cjzz/{licence}`
- **更新频率**：每日20:10
- **说明**：沪深A股中今日成交量较上一交易日成交量大幅增加的股票。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `c` | `number` | 收盘价 |
| `zdf` | `number` | 涨跌幅（%） |
| `iscq` | `number` | 当天是否除权除息（0：否，1：是） |
| `v` | `number` | 成交量（股） |
| `pv` | `number` | 前一交易日成交量（股） |
| `zjl` | `number` | 增减量（股） |
| `zjf` | `number` | 增减幅（%） |

#### 成交骤减个股

- **方法**：`hsdc_himk_cjzj()`
- **路径**：`/himk/cjzj/{licence}`
- **更新频率**：每日20:10
- **说明**：沪深A股中今日成交量较上一交易日成交量大幅减少的股票。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `c` | `number` | 收盘价 |
| `zdf` | `number` | 涨跌幅（%） |
| `iscq` | `number` | 当天是否除权除息（0：否，1：是） |
| `v` | `number` | 成交量（股） |
| `pv` | `number` | 前一交易日成交量（股） |
| `zjl` | `number` | 增减量（股） |
| `zjf` | `number` | 增减幅（%） |

#### 连续放量个股

- **方法**：`hsdc_himk_lxfl()`
- **路径**：`/himk/lxfl/{licence}`
- **更新频率**：每日20:10
- **说明**：沪深A股中成交量连续放大的股票。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `c` | `number` | 收盘价 |
| `zdf` | `number` | 涨跌幅（%） |
| `iscq` | `number` | 当天是否除权除息（0：否，1：是） |
| `v` | `number` | 成交量（股） |
| `pv` | `number` | 前一交易日成交量（股） |
| `flday` | `number` | 放量天数 |
| `pzdf` | `number` | 阶段涨跌幅（%） |
| `ispcq` | `number` | 阶段是否除权除息（0：否，1：是） |
| `phs` | `number` | 阶段换手率（%） |

#### 连续缩量个股

- **方法**：`hsdc_himk_lxsl()`
- **路径**：`/himk/lxsl/{licence}`
- **更新频率**：每日20:10
- **说明**：沪深A股中成交量连续缩小的股票。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `c` | `number` | 收盘价 |
| `zdf` | `number` | 涨跌幅（%） |
| `iscq` | `number` | 当天是否除权除息（0：否，1：是） |
| `v` | `number` | 成交量（股） |
| `pv` | `number` | 前一交易日成交量（股） |
| `flday` | `number` | 放量天数 |
| `pzdf` | `number` | 阶段涨跌幅（%） |
| `ispcq` | `number` | 阶段是否除权除息（0：否，1：是） |
| `phs` | `number` | 阶段换手率（%） |

#### 连续上涨个股

- **方法**：`hsdc_himk_lxsz()`
- **路径**：`/himk/lxsz/{licence}`
- **更新频率**：每日20:10
- **说明**：沪深A股中连续上涨的股票。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `c` | `number` | 收盘价 |
| `zdf` | `number` | 涨跌幅（%） |
| `iscq` | `number` | 当天是否除权除息（0：否，1：是） |
| `v` | `number` | 成交量（股） |
| `hs` | `number` | 换手（%） |
| `szday` | `number` | 上涨天数 |
| `pzdf` | `number` | 阶段涨跌幅（%） |
| `ispcq` | `number` | 阶段是否除权除息（0：否，1：是） |

#### 连续下跌个股

- **方法**：`hsdc_himk_lxxd()`
- **路径**：`/himk/lxxd/{licence}`
- **更新频率**：每日20:10
- **说明**：沪深A股中连续下跌的股票。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `c` | `number` | 收盘价 |
| `zdf` | `number` | 涨跌幅（%） |
| `iscq` | `number` | 当天是否除权除息（0：否，1：是） |
| `v` | `number` | 成交量（股） |
| `hs` | `number` | 换手（%） |
| `szday` | `number` | 上涨天数 |
| `pzdf` | `number` | 阶段涨跌幅（%） |
| `ispcq` | `number` | 阶段是否除权除息（0：否，1：是） |

#### 周涨跌排名

- **方法**：`hsdc_himk_zzd()`
- **路径**：`/himk/zzd/{licence}`
- **更新频率**：每日20:10
- **说明**：沪深A股本周涨跌幅排名，涨跌幅以复权价进行计算。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `zdf` | `number` | 周涨跌幅（%） |
| `v` | `number` | 周成交量（股） |
| `amount` | `number` | 周成交额（元） |
| `hs` | `number` | 周换手率（%） |
| `hp` | `number` | 周最高价 |
| `lp` | `number` | 周最低价 |
| `zf` | `number` | 周振幅（%） |
| `h` | `number` | 周最高价 |
| `l` | `number` | 周最低价 |
| `e` | `number` | 总成交额(元) |

#### 月涨跌排名

- **方法**：`hsdc_himk_yzd()`
- **路径**：`/himk/yzd/{licence}`
- **更新频率**：每日20:10
- **说明**：沪深A股本月涨跌幅排名，涨跌幅以复权价进行计算。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `zdf` | `number` | 月涨跌幅（%） |
| `v` | `number` | 月成交量（股） |
| `amount` | `number` | 月成交额（元） |
| `hs` | `number` | 月换手率（%） |
| `hp` | `number` | 月最高价 |
| `lp` | `number` | 月最低价 |
| `zf` | `number` | 月振幅（%） |
| `h` | `number` | 月最高价 |
| `l` | `number` | 月最低价 |
| `e` | `number` | 月成交额(元) |

#### 本周强势股（官网文档页可能尚未展示）

- **方法**：`hsdc_himk_zqsg()`
- **路径**：`/himk/zqsg/{licence}`
- **更新频率**：每日20:10
- **说明**：沪深A股本周涨跌幅大于沪深300指数的股票，涨跌幅以复权价进行计算。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `zdf` | `number` | 周涨跌幅（%） |
| `o` | `number` | 周开盘价 |
| `c` | `number` | 周收盘价 |
| `h` | `number` | 周最高价 |
| `l` | `number` | 周最低价 |
| `v` | `number` | 周成交量（股） |
| `hs` | `number` | 周换手率（%） |
| `zf300` | `number` | 本周沪深300涨幅（%） |

#### 本月强势股（官网文档页可能尚未展示）

- **方法**：`hsdc_himk_mqsg()`
- **路径**：`/himk/mqsg/{licence}`
- **更新频率**：每日20:10
- **说明**：沪深A股本月涨跌幅大于沪深300指数的股票，涨跌幅以复权价进行计算。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `zdf` | `number` | 月涨跌幅（%） |
| `o` | `number` | 月开盘价 |
| `c` | `number` | 月收盘价 |
| `h` | `number` | 月最高价 |
| `l` | `number` | 月最低价 |
| `v` | `number` | 月成交量（股） |
| `hs` | `number` | 月换手率（%） |
| `zf300` | `number` | 本月沪深300涨幅（%） |

#### 流通市值排行

- **方法**：`hsdc_himk_ltszph()`
- **路径**：`/himk/ltszph/{licence}`
- **更新频率**：每日20:10
- **说明**：沪深A股流通市值排名。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `c` | `number` | 收盘价 |
| `zdf` | `number` | 涨跌幅（%） |
| `v` | `number` | 成交量（股） |
| `hs` | `number` | 换手率（%） |
| `ltsz` | `number` | 流通市值（万元） |
| `zsz` | `number` | 总市值（万元） |

#### 市盈率排行

- **方法**：`hsdc_himk_syl()`
- **路径**：`/himk/syl/{licence}`
- **更新频率**：每日20:10
- **说明**：沪深A股静态市盈率、动态市盈率排名，静态市盈率以最近一个年度收益进行计算，动态市盈率以最近四个季度的单季收益进行计算。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `c` | `number` | 收盘价 |
| `zdf` | `number` | 涨跌幅（%） |
| `v` | `number` | 成交量（股） |
| `hs` | `number` | 换手率（%） |
| `jpe` | `number` | 静态市盈率：总市值除以上年度净利润 |
| `dpe` | `number` | 市盈率(TTM)：最新价除以最近4个季度的每股收益 |

#### 市净率排行

- **方法**：`hsdc_himk_sjl()`
- **路径**：`/himk/sjl/{licence}`
- **更新频率**：每日20:10
- **说明**：沪深A股市净率排名。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `c` | `number` | 收盘价 |
| `zdf` | `number` | 涨跌幅（%） |
| `v` | `number` | 成交量（股） |
| `hs` | `number` | 换手率（%） |
| `sjl` | `number` | 市净率 |
| `jzc` | `number` | 每股净资产 |

#### ROE排行

- **方法**：`hsdc_himk_roe()`
- **路径**：`/himk/roe/{licence}`
- **更新频率**：每日16:30
- **说明**：沪深A股ROE排名，根据roe倒序。

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 股票代码 |
| `mc` | `string` | 股票名称 |
| `roe` | `number` | ROE（%） |
| `zsz` | `number` | 总市值（元） |
| `jzc` | `number` | 净资产（元） |
| `jlr` | `number` | 净利润（元） |
| `syld` | `number` | 市盈率（动） |
| `sjl` | `number` | 市净率 |
| `mll` | `number` | 毛利率（%） |
| `jll` | `number` | 净利率（%） |
| `hyroe` | `number` | 行业平均ROE（%） |
| `hyzsz` | `number` | 行业平均总市值（元） |
| `hyjzc` | `number` | 行业平均净资产（元） |
| `hyjlr` | `number` | 行业平均净利润（元） |
| `hysyld` | `number` | 行业平均市盈率（动） |
| `hysjl` | `number` | 行业平均市净率 |
| `hymll` | `number` | 行业平均毛利率（%） |
| `hyjll` | `number` | 行业平均净利率（%） |
| `roepm` | `number` | ROE行业排名 |
| `zszpm` | `number` | 总市值行业排名 |
| `jzcpm` | `number` | 净资产行业排名 |
| `jlrpm` | `number` | 净利润行业排名 |
| `syldpm` | `number` | 市盈率行业排名 |
| `sjlpm` | `number` | 市净率行业排名 |
| `mllpm` | `number` | 毛利率行业排名 |
| `jllpm` | `number` | 净利率行业排名 |
| `hym` | `string` | 行业名 |
| `hygpzs` | `number` | 同行业股票总数量 |

### 投资参考

#### 今日交易提示

- **方法**：`hsdc_jrts()`
- **路径**：`/hitc/jrts/{licence}`
- **更新频率**：每日15:40
- **说明**：今日股票、基金公告事项以及交易异动概览。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `tp` | `string` | 停牌。格式："tp":["xxx","xxx",...]。其中xxx格式为“(股票代码)股票名称：停牌说明” |
| `zfssr` | `string` | 转增上市日。格式："zfssr":["xxx","xxx",...]。其中xxx格式为“(股票代码)
股票名称：说明” |
| `gddh` | `string` | 召开股东大会。格式："gddh":["xxx","xxx",...]。其中xxx格式为“(股票代码)
股票名称：说明” |
| `zqdjr` | `string` | 债权登记日。格式："zqdjr":["xxx","xxx",...]。其中xxx格式为“(股票代码)
股票名称：说明” |
| `jjfp` | `string` | 基金收益分配款发放日。格式："jjfp":["xxx","xxx",...]。其中xxx格式为“(股票代码)
股票名称：说明” |
| `jjcx` | `string` | 基金收益分配除息日。格式："jjcx":["xxx","xxx",...]。其中xxx格式为“(股票代码)
股票名称：说明” |
| `jjdj` | `string` | 基金权益登记日。格式："jjdj":["xxx","xxx",...]。其中xxx格式为“(股票代码)
股票名称：说明” |
| `szgg` | `string` | 深交所公告。格式："szgg":["xxx","xxx",...]。其中xxx格式为“(股票代码)
股票名称：说明” |
| `shgg` | `string` | 上交所公告。格式："shgg":["xxx","xxx",...]。其中xxx格式为“(股票代码)
股票名称：说明” |
| `jjfx` | `string` | 开放式基金发行起始日。格式："jjfx":["xxx","xxx",...]。其中xxx格式为“(股票代码)
股票名称：说明” |
| `jjjz` | `string` | 开放式基金发行截止日。格式："jjjz":["xxx","xxx",...]。其中xxx格式为“(股票代码)
股票名称：说明” |
| `gpgk` | `string` | 股票交易公开信息。格式："gpgk":["xxx","xxx",...]。其中xxx格式为“(股票代码)
股票名称：说明” |
| `obsh` | `string` | 货币型基金结转份额可赎回起始日。格式："obsh":["xxx","xxx",...]。其中xxx格式为“(股票代码)
股票名称：说明” |
| `cqcx` | `string` | 恢复交易日。格式："cqcx":["xxx","xxx",...]。其中xxx格式为“(股票代码)
股票名称：说明” |
| `djr` | `string` | 股票登记日。格式："djr":["xxx","xxx",...]。其中xxx格式为“(股票代码)
股票名称：说明” |
| `fhjy` | `array` | 分红交易。格式："fhjy":["xxx",...]，其中xxx格式为：(股票代码) 股票名称：说明 |

#### 融资融券交易总量

- **方法**：`hsdc_rzrqzl()`
- **路径**：`/hitc/rzrqzl/{licence}`
- **更新频率**：每日15:40
- **说明**：上一个交易日（当前交易日的数据要到第二天才出）的两市融资融券概览。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `market` | `string` | 市场："沪市"或"深市" |
| `rzye` | `number` | 融资余额(元) |
| `rzmr` | `number` | 融资买入额(元) |
| `rzch` | `number` | 融资偿还额(元) |
| `rzyl` | `number` | 融券余量(元) |

#### 融资融券交易明细

- **方法**：`hsdc_rzrqmx()`
- **路径**：`/hitc/rzrqmx/{licence}`
- **更新频率**：每日15:40
- **说明**：上一个交易日（当前交易日的数据要到第二天才出）的两市各股票融资融券明细。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 股票代码 |
| `mc` | `string` | 股票名称 |
| `rzye` | `number` | 融资余额(元) |
| `rzmre` | `number` | 融资买入额(元) |
| `rzche` | `number` | 融资偿还额(元) |
| `rqyl` | `number` | 融券余量(股) |
| `rqmcl` | `number` | 融券卖出量(股) |
| `rqchl` | `number` | 偿还量(股) |

#### 大宗交易

- **方法**：`hsdc_dzjy()`
- **路径**：`/hitc/dzjy/{licence}`
- **更新频率**：每日15:40
- **说明**：上一个交易日（当前交易日的数据要到第二天才出）的大宗交易明细。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dm` | `string` | 股票代码 |
| `mc` | `string` | 股票名称 |
| `p` | `number` | 成交价格(元) |
| `v` | `number` | 成交量(万股) |
| `dp` | `number` | 成交金额(万元) |
| `buyi` | `string` | 买方营业部 |
| `selli` | `string` | 卖方营业部 |
| `type` | `string` | 证券类型 |

#### 解禁限售

- **方法**：`hsdc_jjxs()`
- **路径**：`/hitc/jjxs/{licence}`
- **更新频率**：每日15:40
- **说明**：以当前交易日的前后15天左右为时间范围，已经进行或者即将进行的解禁限售行为。

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 股票代码 |
| `mc` | `string` | 股票名称 |
| `rdate` | `string` | 解禁日期yyyy-MM-dd |
| `ramount` | `number` | 解禁数量(万股) |
| `rprice` | `number` | 解禁股流通市值(亿元) |
| `batch` | `number` | 上市批次 |
| `pdate` | `string` | 公告日期yyyy-MM-dd |

#### 打新收益

- **方法**：`hsdc_dxsy()`
- **路径**：`/hitc/dxsy/{licence}`
- **更新频率**：每日15:40
- **说明**：近几年（四年左右）的打新收益数据。

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 证券代码 |
| `sgdm` | `string` | 申购代码 |
| `mc` | `string` | 股票名称 |
| `pdate` | `string` | 上市日期yyyy-MM-dd |
| `ndate` | `String` | 网签日期yyyy-MM-dd |
| `pe` | `number` | 市盈率 |
| `zql` | `number` | 中签率(%) |
| `zdf` | `number` | 涨跌幅(%) |
| `sy` | `number` | 收益 |
| `p` | `number` | 发行价格 |
| `amount` | `number` | 发行数量 |

#### 历史累计分红

- **方法**：`hsdc_lsfh()`
- **路径**：`/hitc/lsfh/{licence}`
- **更新频率**：每日15:40
- **说明**：各只股票历史累计分红统计。

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 证券代码 |
| `mc` | `string` | 股票名称 |
| `pdate` | `string` | 上市日期yyyy-MM-dd |
| `totalgx` | `number` | 累计股息(%) |
| `pergx` | `number` | 年均股息(%) |
| `count` | `number` | 分红次数 |
| `totalrz` | `number` | 融资总额(亿) |
| `rzcount` | `number` | 融资次数 |

### 板块资金流向

#### 证监会行业

- **方法**：`hsdc_hibk_zjhhy()`
- **路径**：`/hibk/zjhhy/{licence}`
- **更新频率**：每日15:40
- **说明**：证监会行业资金流向，根据流入资金倒序排列。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 服务器更新时间yyyy-MM-ddHH:mm:ss |
| `mc` | `string` | 行业名称 |
| `dm` | `string` | 行业代码 |
| `jj` | `number` | 均价（元） |
| `zdf` | `number` | 涨跌幅（%） |
| `lrzj` | `number` | 流入资金（元） |
| `lczj` | `number` | 流出资金（元） |
| `jlr` | `number` | 净流入（元） |
| `jlrl` | `number` | 净流入率（%） |
| `lzgmc` | `string` | 领涨股名称 |
| `lzgdm` | `string` | 领涨股代码 |
| `lzgjlrl` | `number` | 领涨股净流入率（%） |

#### 概念板块

- **方法**：`hsdc_hibk_gnbk()`
- **路径**：`/hibk/gnbk/{licence}`
- **更新频率**：每日15:40
- **说明**：概念板块资金流向，根据流入资金倒序排列。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 服务器更新时间yyyy-MM-ddHH:mm:ss |
| `mc` | `string` | 概念板块名称 |
| `dm` | `string` | 概念板块代码 |
| `jj` | `number` | 均价（元） |
| `zdf` | `number` | 涨跌幅（%） |
| `lrzj` | `number` | 流入资金（元） |
| `lczj` | `number` | 流出资金（元） |
| `jlr` | `number` | 净流入（元） |
| `jlrl` | `number` | 净流入率（%） |
| `lzgmc` | `string` | 领涨股名称 |
| `lzgdm` | `string` | 领涨股代码 |
| `lzgjlrl` | `number` | 领涨股净流入率（%） |

### 财务分析

#### 利润细分

- **方法**：`hsdc_hicw_lr()`
- **路径**：`/hicw/lr/{licence}`
- **更新频率**：每日20:10
- **说明**：个股利润细分汇总。

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 代码 |
| `mc` | `string` | 名称 |
| `sshy` | `string` | 所属行业 |
| `sshysr` | `number` | 所属行业收入(万元) |
| `ckcb` | `number` | 所属行业参考成本(万元) |
| `cklr` | `number` | 参考利润(万元) |
| `lrms` | `string` | 利润描述 |
| `rdate` | `string` | 报告日期 |

### 资金路线图

#### 证监会行业资金路线图

- **方法**：`hsdc_zjh()`
- **路径**：`/hizj/zjh/{licence}`
- **更新频率**：每日15:40
- **说明**：统计近3、5、10天证监会行业资金流入情况。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 服务器更新时间yyyy-MM-ddHH:mm:ss |
| `mc` | `string` | 行业名 |
| `dm` | `string` | 行业代码 |
| `ac3` | `number` | 近三日涨跌幅（%） |
| `net3` | `number` | 近三日净流入（元） |
| `ra3` | `number` | 近三日净流入率（%） |
| `ac5` | `number` | 近五日涨跌幅（%） |
| `net5` | `number` | 近五日净流入（元） |
| `ra5` | `number` | 近五日净流入率（%） |
| `ac10` | `number` | 近十日涨跌幅（%） |
| `net10` | `number` | 近十日净流入（元） |
| `ra10` | `number` | 近十日净流入率（%） |

#### 概念板块资金路线图

- **方法**：`hsdc_bk()`
- **路径**：`/hizj/bk/{licence}`
- **更新频率**：每日15:40
- **说明**：统计近3、5、10天概念板块资金流入情况。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 服务器更新时间yyyy-MM-ddHH:mm:ss |
| `mc` | `string` | 概念板块名 |
| `dm` | `string` | 概念板块代码 |
| `ac3` | `number` | 近三日涨跌幅（%） |
| `net3` | `number` | 近三日净流入（元） |
| `ra3` | `number` | 近三日净流入率（%） |
| `ac5` | `number` | 近五日涨跌幅（%） |
| `net5` | `number` | 近五日净流入（元） |
| `ra5` | `number` | 近五日净流入率（%） |
| `ac10` | `number` | 近十日涨跌幅（%） |
| `net10` | `number` | 近十日净流入（元） |
| `ra10` | `number` | 近十日净流入率（%） |

#### 个股阶段统计总览

- **方法**：`hsdc_ggzl()`
- **路径**：`/hizj/ggzl/{licence}`
- **更新频率**：每日15:40
- **说明**：个股阶段净流入资金统计总览，根据股票代码升序排列。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 服务器更新时间yyyy-MM-ddHH:mm:ss |
| `mc` | `string` | 名称 |
| `dm` | `string` | 代码 |
| `zxj` | `number` | 最新价（元） |
| `zdf` | `number` | 涨跌幅（%） |
| `hsl` | `number` | 换手率（%） |
| `jlrl3` | `number` | 3日净流入率（%） |
| `jlrl5` | `number` | 5日净流入率（%） |
| `jlrl10` | `number` | 10日净流入率（%） |
| `jlrl20` | `number` | 20日净流入率（%） |
| `jlrl60` | `number` | 60日净流入率（%） |

#### 主力连续净流入/流出

- **方法**：`hsdc_lxlr()`
- **路径**：`/hizj/lxlr/{licence}`
- **更新频率**：每日15:40
- **说明**：主力连续净流入/流出统计，流入天数倒序排列。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 服务器更新时间yyyy-MM-ddHH:mm:ss |
| `mc` | `string` | 名称 |
| `dm` | `string` | 代码 |
| `ts` | `number` | 流入/流出天数（天）（正数表示流入，负数表示流出） |
| `zxj` | `number` | 最新价（元） |
| `jdzdf` | `number` | 阶段涨跌幅（%） |
| `jdhsl` | `number` | 阶段换手率（%） |
| `jdjlr` | `number` | 阶段净流入/流出（元）（正数表示流入，负数表示流出） |
| `jdjlrl` | `number` | 阶段流入/流出率（%）（正数表示流入，负数表示流出） |
| `zljlr` | `number` | 主力净流入/流出（元）（正数表示流入，负数表示流出） |

### 龙虎榜

#### 每日详情

- **方法**：`hsdc_hilh_mrxq()`
- **路径**：`/hilh/mrxq/{licence}`
- **更新频率**：每日20:00
- **说明**：今日龙虎榜概览。

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期yyyy-MM-dd |
| `dpl7` | `string` | 跌幅偏离值达7%的证券，格式："dpl7":[LhbDetail,...]，LhbDetail对象说明见下表。 |
| `z20` | `string` | 连续三个交易日内，涨幅偏离值累计达20%的证券，格式："z20":[LhbDetail,...]，LhbDetail对象说明见下表。 |
| `zpl7` | `string` | 涨幅偏离值达7%的证券，格式："zpl7":[LhbDetail,...]，LhbDetail对象说明见下表。 |
| `h20` | `string` | 换手率达20%的证券，格式："h20":[LhbDetail,...]，LhbDetail对象说明见下表。 |
| `st15` | `string` | 连续三个交易日内，涨幅偏离值累计达到15%的ST证券、*ST证券和未完成股改证券，格式："st15":[LhbDetail,...]，LhbDetail对象说明见下表。 |
| `st12` | `string` | 连续三个交易日内，涨幅偏离值累计达到12%的ST证券、*ST证券和未完成股改证券，格式："st12":[LhbDetail,...]，LhbDetail对象说明见下表。 |
| `std15` | `string` | 连续三个交易日内，跌幅偏离值累计达到15%的ST证券、*ST证券和未完成股改证券，格式："std15":[LhbDetail,...]，LhbDetail对象说明见下表。 |
| `std12` | `string` | 连续三个交易日内，跌幅偏离值累计达到12%的ST证券、*ST证券和未完成股改证券，格式："std12":[LhbDetail,...]，LhbDetail对象说明见下表。 |
| `zf15` | `string` | 振幅值达15%的证券，格式："zf15":[LhbDetail,...]，LhbDetail对象说明见下表。 |
| `df15` | `string` | 连续三个交易日内，跌幅偏离值累计达20%的证券，格式："df15":[LhbDetail,...]，LhbDetail对象说明见下表。 |
| `wxz` | `string` | 无价格涨跌幅限制的证券，格式："wxz":[LhbDetail,...]，LhbDetail对象说明见下表。 |
| `wxztp` | `string` | 当日无价格涨跌幅限制的A股，出现异常波动停牌的股票，格式："wxztp":[LhbDetail,...]，LhbDetail对象说明见下表。 |
| `dm` | `string` | 股票代码（LhbDetail） |
| `mc` | `string` | 股票名称（LhbDetail） |
| `c` | `number` | 收盘价（LhbDetail） |
| `val` | `number` | 涨跌幅%（LhbDetail） |
| `v` | `number` | 成交量（LhbDetail，手/万股口径以源站为准） |
| `e` | `number` | 成交额（LhbDetail） |

#### 机构席位成交明细

- **方法**：`hsdc_hilh_xwmx()`
- **路径**：`/hilh/xwmx/{licence}`
- **更新频率**：每日15:40
- **说明**：近五个交易日（按交易日期倒序）上榜个股被机构交易的总额，以及个股上榜原因。

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 股票代码 |
| `mc` | `string` | 股票名称 |
| `t` | `string` | 交易日期yyyy-MM-dd |
| `buy` | `number` | 机构席位买入额(万) |
| `sell` | `number` | 机构席位卖出额(万) |
| `type` | `number` | 类型 |

## 基金数据中心

### 基金业绩排行

#### 开放式基金业绩排行（股、混合、债、QDII类）

- **方法**：`fundc_pm_kfpm()`
- **路径**：`/js/pm/kfpm/kfsjj_gpxjj_zsx/{licence}`
- **更新频率**：每日21:30
- **说明**：根据【基金分类参数】（见下方“【基金分类参数】说明”）获取不同分类下的开放式基金的业绩排行，根据今年以来涨幅倒序。
没有提供“基金数据中心-业绩排行-开放式基金-开放式基金净值排名（货币类）”接口，因为和“基金数据中心-基金净值-开放式基金-开放式基金净值排名（货币类）”的接口一模一样。

| 参数 | 说明 |
|------|------|
| `kfsjj_gpxjj_zsx` | 开放式基金-股票型基金-指数型 |
| `kfsjj_gpxjj_ybgpx` | 开放式基金-股票型基金-一般股票型 |
| `kfsjj_hhxjj_wjhhx` | 开放式基金-混合型基金-稳健混合型 |
| `kfsjj_hhxjj_jjhhx` | 开放式基金-混合型基金-激进混合型 |
| `kfsjj_hhxjj_bbx` | 开放式基金-混合型基金-保本型 |
| `kfsjj_zqxjj_wjzqx` | 开放式基金-债券型基金-稳健债券型 |
| `kfsjj_zqxjj_jjzqx` | 开放式基金-债券型基金-激进债券型 |
| `kfsjj_zqxjj_cjzqx` | 开放式基金-债券型基金-纯债债券型 |
| `kfsjj_qdiijj_qt` | 开放式基金-QDII基金-其他 |
| `kfsjj_qdiijj_qyl` | 开放式基金-QDII基金-权益类 |
| `kfsjj_qdiijj_gdsyl` | 开放式基金-QDII基金-固定收益类 |

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001（华夏成长混合） |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `dwjz` | `number` | 单位净值 |
| `ljjz` | `number` | 累计净值 |
| `jsgy` | `number` | 近三个月(%) |
| `jlgy` | `number` | 近六个月(%) |
| `jyn` | `number` | 近一年(%) |
| `jnyl` | `number` | 今年以来(%) |
| `clyl` | `number` | 成立以来(%) |

#### 封闭式基金业绩排行

- **方法**：`fundc_pm_fbpm()`
- **路径**：`/js/pm/fbpm/kfsjj_fbqy_ctfj/{licence}`
- **更新频率**：每日21:30
- **说明**：根据【基金分类参数】（见下方“【基金分类参数】说明”）获取不同分类下的封闭式基金的业绩排行，根据今年以来涨幅倒序。

| 参数 | 说明 |
|------|------|
| `kfsjj_fbqy_ctfj` | 封闭式基金-封闭权益-传统封基 |
| `kfsjj_fbqy_cxfj` | 封闭式基金-封闭权益-创新封基 |
| `kfsjj_fbz_wjzqx` | 封闭式基金-封闭债-稳健债券型 |
| `kfsjj_fbz_jjzqx` | 封闭式基金-封闭债-激进债券型 |
| `kfsjj_fbz_czzqx` | 封闭式基金-封闭债-纯债债券型 |

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001（华夏成长混合） |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `dwjz` | `number` | 单位净值 |
| `ljjz` | `number` | 累计净值 |
| `jsgy` | `number` | 近三个月(%) |
| `jlgy` | `number` | 近六个月(%) |
| `jyn` | `number` | 近一年(%) |
| `jnyl` | `number` | 今年以来(%) |
| `clyl` | `number` | 成立以来(%) |

#### 分级子基金业绩排行

- **方法**：`fundc_pm_fzyj()`
- **路径**：`/js/pm/fzyj/kfsjj_fjgs_wjzqx/{licence}`
- **更新频率**：每日21:30
- **说明**：根据【基金分类参数】（见下方“【基金分类参数】说明”）获取不同分类下的分级子基金的业绩排行，根据今年以来涨幅倒序。

| 参数 | 说明 |
|------|------|
| `kfsjj_fjgs_wjzqx` | 分级子基金-分级固收-稳健债券型 |
| `kfsjj_fjgs_ybgpx` | 分级子基金-分级固收-一级股票型 |
| `kfsjj_fjgs_zsx` | 分级子基金-分级固收-指数型 |
| `kfsjj_fjgs_czzqx` | 分级子基金-分级固收-纯债债券型 |
| `kfsjj_fjgs_jjzqx` | 分级子基金-分级固收-激进债券型 |
| `kfsjj_fjgg_wjzqx` | 分级子基金-分级杠杆-稳健债券型 |
| `kfsjj_fjgg_ybgpx` | 分级子基金-分级杠杆-一级股票型 |
| `kfsjj_fjgg_zsx` | 分级子基金-分级杠杆-指数型 |
| `kfsjj_fjgg_czzqx` | 分级子基金-分级杠杆-纯债债券型 |
| `kfsjj_fjgg_jjzqx` | 分级子基金-分级杠杆-激进债券型 |

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001（华夏成长混合） |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `dwjz` | `number` | 单位净值 |
| `ljjz` | `number` | 累计净值 |
| `jsgy` | `number` | 近三个月(%) |
| `jlgy` | `number` | 近六个月(%) |
| `jyn` | `number` | 近一年(%) |
| `jnyl` | `number` | 今年以来(%) |
| `clyl` | `number` | 成立以来(%) |

### 基金其他

#### 基金重仓股

- **方法**：`fundc_other_jjzc(yyyy_j)`
- **路径**：`/js/other/jjzc/{yyyy_j}/{licence}`
- **更新频率**：每日21:30
- **说明**：基金重仓个股排名，根据基金覆盖面倒序。支持“年份_季度”查询，年份可选（1999~当前年份），季度可选（1:一季报，2：中报，3：三季报，4：年报），如“2021_1”，表示查询2021年一季度数据。

路径参数：
- `yyyy_j`

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 代码 |
| `wzdm` | `string` | 完整代码 |
| `mc` | `string` | 名称 |
| `jjs` | `number` | 基金覆盖面(只) |
| `cg` | `number` | 持股总数(万股) |
| `cgsz` | `number` | 持股总市值(万元) |
| `sqcgsz` | `number` | 上期持股总市值(万元) |
| `zb` | `number` | 占该股流通市值比例(%) |
| `y` | `number` | 报告年份，如2021 |
| `q` | `number` | 报告季度，1:一季报，2：中报，3：三季报，4：年报 |
| `yq` | `string` | 报告年份及季度合体，如"2026_2"表示2026年二季报 |

#### 基金重仓股变动

- **方法**：`fundc_other_zcbd(yyyy_j)`
- **路径**：`/js/other/zcbd/{yyyy_j}/{licence}`
- **更新频率**：每日21:30
- **说明**：基金重仓个股与往季变动情况排名，根据覆盖面变化倒序。支持“年份_季度”查询，年份可选（1999~当前年份），季度可选（1:一季报，2：中报，3：三季报，4：年报），如“2021_1”，表示查询2021年一季度数据。

路径参数：
- `yyyy_j`

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 代码 |
| `wzdm` | `string` | 完整代码 |
| `mc` | `string` | 名称 |
| `qfgm` | `number` | 上一个季度覆盖面(只) |
| `bfgm` | `number` | 本季度覆盖面(只) |
| `bhfgm` | `number` | 覆盖面变化(只) |
| `qcgs` | `number` | 上一个季度持股数（万股） |
| `bcgs` | `number` | 本季度持股数（万股） |
| `cgsbh` | `number` | 持股数变化（万股） |
| `ltbh` | `number` | 占流通股比例变化(%) |
| `y` | `number` | 报告年份，如2021 |
| `q` | `number` | 报告季度，1:一季报，2：中报，3：三季报，4：年报 |
| `yq` | `string` | 报告年份及季度合体，如"2026_2"表示2026年二季报 |

#### 代销机构

- **方法**：`fundc_other_dxjg()`
- **路径**：`/js/other/dxjg/yh/{licence}`
- **更新频率**：每日21:30
- **说明**：根据【参数】（见下方“【参数】说明”）获取代销机构中的银行、证券公司、独立资金销售机构，根据近三月超额收益率倒序。

| 参数 | 说明 |
|------|------|
| `yh` | 银行 |
| `zqgs` | 证券公司 |
| `dljjxsjg` | 独立资金销售机构 |

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 机构代码 |
| `mc` | `string` | 机构名称 |
| `lxr` | `string` | 联系人 |
| `bd` | `string` | 电话（与ph同值） |
| `num` | `number` | 代销数(只) |
| `ph` | `string` | 电话（与bd同值，兼容字段） |

### 基金净值排名

#### 开放式基金净值排名（股、混合、债、QDII类）

- **方法**：`fundc_pm_kfjzg()`
- **路径**：`/js/pm/kfjzg/kfsjj_gpxjj_zsx/{licence}`
- **更新频率**：每日21:30
- **说明**：根据【基金分类参数】（见下方“【基金分类参数】说明”）获取不同分类下的开放式基金的净值排名，根据净值日期倒序。

| 参数 | 说明 |
|------|------|
| `kfsjj_gpxjj_zsx` | 开放式基金-股票型基金-指数型 |
| `kfsjj_gpxjj_ybgpx` | 开放式基金-股票型基金-一般股票型 |
| `kfsjj_hhxjj_wjhhx` | 开放式基金-混合型基金-稳健混合型 |
| `kfsjj_hhxjj_jjhhx` | 开放式基金-混合型基金-激进混合型 |
| `kfsjj_hhxjj_bbx` | 开放式基金-混合型基金-保本型 |
| `kfsjj_zqxjj_wjzqx` | 开放式基金-债券型基金-稳健债券型 |
| `kfsjj_zqxjj_jjzqx` | 开放式基金-债券型基金-激进债券型 |
| `kfsjj_zqxjj_cjzqx` | 开放式基金-债券型基金-纯债债券型 |
| `kfsjj_qdiijj_qt` | 开放式基金-QDII基金-其他 |
| `kfsjj_qdiijj_qyl` | 开放式基金-QDII基金-权益类 |
| `kfsjj_qdiijj_gdsyl` | 开放式基金-QDII基金-固定收益类 |

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001（华夏成长混合） |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `dwjz` | `number` | 单位净值 |
| `ljjz` | `number` | 累计净值 |
| `qyrjz` | `number` | 前一日净值 |
| `zde` | `number` | 涨跌额 |
| `zzl` | `number` | 增长率（%） |
| `sgzt` | `string` | 申购状态 |
| `jzrq` | `string` | 净值日期 |
| `glr` | `string` | 基金管理人 |
| `jjlx` | `string` | 基金类型 |

#### 开放式基金净值排名（货币类）

- **方法**：`fundc_pm_kfjzq()`
- **路径**：`/js/pm/kfjzq/kfsjj_hbxjj_hba/{licence}`
- **更新频率**：每日21:30
- **说明**：根据【基金分类参数】（见下方“【基金分类参数】说明”）获取不同分类下的开放式基金的净值排名，
根据最近七日年化收益率倒序。和“开放式基金净值排名（股、混合、债、QDII类）接口”使用方式一样，但是由于返回数据结构不一样，因此单独抽离成一个接口。
同时，“基金数据中心-业绩排行-开放式基金-开放式基金净值排名（货币类）”也是此接口。

| 参数 | 说明 |
|------|------|
| `kfsjj_hbxjj_hba` | 开放式基金-货币型基金-货币A |
| `kfsjj_hbxjj_hbb` | 开放式基金-货币型基金-货币B |

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001（华夏成长混合） |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `dwsy` | `number` | 每万份基金单位收益 |
| `qnsy` | `number` | 最近七日年化收益率(%) |
| `jzrq` | `string` | 净值日期 |
| `clrq` | `string` | 成立日期 |
| `glr` | `string` | 基金管理人 |
| `jjlx` | `string` | 基金类型 |
| `sgzt` | `string` | 申购状态 |

#### 封闭式基金净值排名

- **方法**：`fundc_pm_fbjz()`
- **路径**：`/js/pm/fbjz/kfsjj_fbqy_ctfj/{licence}`
- **更新频率**：每日21:30
- **说明**：根据【基金分类参数】（见下方“【基金分类参数】说明”）获取不同分类下的封闭式基金的净值排名，根据净值日期倒序。

| 参数 | 说明 |
|------|------|
| `kfsjj_fbqy_ctfj` | 封闭式基金-封闭权益-传统封基 |
| `kfsjj_fbqy_cxfj` | 封闭式基金-封闭权益-创新封基 |
| `kfsjj_fbz_wjzqx` | 封闭式基金-封闭债-稳健债券型 |
| `kfsjj_fbz_jjzqx` | 封闭式基金-封闭债-激进债券型 |
| `kfsjj_fbz_czzqx` | 封闭式基金-封闭债-纯债债券型 |

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001（华夏成长混合） |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `dwjz` | `number` | 单位净值 |
| `ljjz` | `number` | 累计净值 |
| `zzl` | `number` | 增长率（%） |
| `zyjl` | `number` | 折溢价率（%） |
| `jzrq` | `string` | 净值日期 |
| `clrq` | `string` | 成立日期 |
| `dqrq` | `string` | 到期日期 |
| `glr` | `string` | 基金管理人 |
| `jjlx` | `string` | 基金类型 |

### 基金分红

#### 开放式基金基金分红

- **方法**：`fundc_jf_kffh()`
- **路径**：`/js/jf/kffh/kfsjj_gpxjj_zsx/{licence}`
- **更新频率**：每日21:30
- **说明**：根据【基金分类参数】（见下方“【基金分类参数】说明”）获取不同分类下的开放式基金的基金分红，根据最新派息日倒序。

| 参数 | 说明 |
|------|------|
| `kfsjj_gpxjj_zsx` | 开放式基金-股票型基金-指数型 |
| `kfsjj_gpxjj_ybgpx` | 开放式基金-股票型基金-一般股票型 |
| `kfsjj_hhxjj_wjhhx` | 开放式基金-混合型基金-稳健混合型 |
| `kfsjj_hhxjj_jjhhx` | 开放式基金-混合型基金-激进混合型 |
| `kfsjj_hhxjj_bbx` | 开放式基金-混合型基金-保本型 |
| `kfsjj_hbxjj_hba` | 开放式基金-货币型基金-货币A |
| `kfsjj_hbxjj_hbb` | 开放式基金-货币型基金-货币B |
| `kfsjj_zqxjj_wjzqx` | 开放式基金-债券型基金-稳健债券型 |
| `kfsjj_zqxjj_jjzqx` | 开放式基金-债券型基金-激进债券型 |
| `kfsjj_zqxjj_cjzqx` | 开放式基金-债券型基金-纯债债券型 |
| `kfsjj_qdiijj_qt` | 开放式基金-QDII基金-其他 |
| `kfsjj_qdiijj_qyl` | 开放式基金-QDII基金-权益类 |
| `kfsjj_qdiijj_gdsyl` | 开放式基金-QDII基金-固定收益类 |

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001（华夏成长混合） |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `zxcxr` | `string` | 最新除息日 |
| `zxpxr` | `string` | 最新派息日 |
| `zxdwfh` | `number` | 最新单位分红 |
| `clrq` | `string` | 成立日期 |
| `qjfhcs` | `number` | 期间分红次数 |
| `qjljfh` | `number` | 期间累计分红 |

#### 分级子基金基金分红

- **方法**：`fundc_jf_fzfh()`
- **路径**：`/js/jf/fzfh/kfsjj_fjgs_wjzqx/{licence}`
- **更新频率**：每日21:30
- **说明**：根据【基金分类参数】（见下方“【基金分类参数】说明”）获取不同分类下的分级子基金的基金分红，根据最新派息日倒序。

| 参数 | 说明 |
|------|------|
| `kfsjj_fjgs_wjzqx` | 分级子基金-分级固收-稳健债券型 |
| `kfsjj_fjgs_ybgpx` | 分级子基金-分级固收-一级股票型 |
| `kfsjj_fjgs_zsx` | 分级子基金-分级固收-指数型 |
| `kfsjj_fjgs_czzqx` | 分级子基金-分级固收-纯债债券型 |
| `kfsjj_fjgs_jjzqx` | 分级子基金-分级固收-激进债券型 |
| `kfsjj_fjgg_wjzqx` | 分级子基金-分级杠杆-稳健债券型 |
| `kfsjj_fjgg_ybgpx` | 分级子基金-分级杠杆-一级股票型 |
| `kfsjj_fjgg_zsx` | 分级子基金-分级杠杆-指数型 |
| `kfsjj_fjgg_czzqx` | 分级子基金-分级杠杆-纯债债券型 |
| `kfsjj_fjgg_jjzqx` | 分级子基金-分级杠杆-激进债券型 |

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001（华夏成长混合） |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `zxcxr` | `string` | 最新除息日 |
| `zxpxr` | `string` | 最新派息日 |
| `zxdwfh` | `number` | 最新单位分红 |
| `clrq` | `string` | 成立日期 |
| `qjfhcs` | `number` | 期间分红次数 |
| `qjljfh` | `number` | 期间累计分红 |

### 基金规模

#### 开放式基金基金规模

- **方法**：`fundc_gm_kfgm()`
- **路径**：`/js/gm/kfgm/kfsjj_gpxjj_zsx/{licence}`
- **更新频率**：每日21:30
- **说明**：根据【基金分类参数】（见下方“【基金分类参数】说明”）获取不同分类下的开放式基金的基金规模，根据总募集规模（万份）倒序。

| 参数 | 说明 |
|------|------|
| `kfsjj_gpxjj_zsx` | 开放式基金-股票型基金-指数型 |
| `kfsjj_gpxjj_ybgpx` | 开放式基金-股票型基金-一般股票型 |
| `kfsjj_hhxjj_wjhhx` | 开放式基金-混合型基金-稳健混合型 |
| `kfsjj_hhxjj_jjhhx` | 开放式基金-混合型基金-激进混合型 |
| `kfsjj_hhxjj_bbx` | 开放式基金-混合型基金-保本型 |
| `kfsjj_hbxjj_hba` | 开放式基金-货币型基金-货币A |
| `kfsjj_hbxjj_hbb` | 开放式基金-货币型基金-货币B |
| `kfsjj_zqxjj_wjzqx` | 开放式基金-债券型基金-稳健债券型 |
| `kfsjj_zqxjj_jjzqx` | 开放式基金-债券型基金-激进债券型 |
| `kfsjj_zqxjj_cjzqx` | 开放式基金-债券型基金-纯债债券型 |
| `kfsjj_qdiijj_qt` | 开放式基金-QDII基金-其他 |
| `kfsjj_qdiijj_qyl` | 开放式基金-QDII基金-权益类 |
| `kfsjj_qdiijj_gdsyl` | 开放式基金-QDII基金-固定收益类 |

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001（华夏成长混合） |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `dwjz` | `number` | 单位净值（元） |
| `zmjgm` | `number` | 总募集规模（万份） |
| `zjzfe` | `number` | 最近总份额（万份） |
| `clrq` | `string` | 成立日期 |
| `jjjl` | `string` | 基金经理 |

#### 封闭式基金基金规模

- **方法**：`fundc_gm_fbgm()`
- **路径**：`/js/gm/fbgm/kfsjj_fbqy_ctfj/{licence}`
- **更新频率**：每日21:30
- **说明**：根据【基金分类参数】（见下方“【基金分类参数】说明”）获取不同分类下的封闭式基金的基金规模，根据总募集规模（万份）倒序。

| 参数 | 说明 |
|------|------|
| `kfsjj_fbqy_ctfj` | 封闭式基金-封闭权益-传统封基 |
| `kfsjj_fbqy_cxfj` | 封闭式基金-封闭权益-创新封基 |
| `kfsjj_fbz_wjzqx` | 封闭式基金-封闭债-稳健债券型 |
| `kfsjj_fbz_jjzqx` | 封闭式基金-封闭债-激进债券型 |
| `kfsjj_fbz_czzqx` | 封闭式基金-封闭债-纯债债券型 |

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001（华夏成长混合） |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `dwjz` | `number` | 单位净值（元） |
| `zmjgm` | `number` | 总募集规模（万份） |
| `zjzfe` | `number` | 最近总份额（万份） |
| `clrq` | `string` | 成立日期 |
| `jjjl` | `string` | 基金经理 |

#### 分级子基金基金规模

- **方法**：`fundc_gm_fzgm()`
- **路径**：`/js/gm/fzgm/kfsjj_fjgs_wjzqx/{licence}`
- **更新频率**：每日21:30
- **说明**：根据【基金分类参数】（见下方“【基金分类参数】说明”）获取不同分类下的分级子基金的基金规模，根据总募集规模（万份）倒序。

| 参数 | 说明 |
|------|------|
| `kfsjj_fjgs_wjzqx` | 分级子基金-分级固收-稳健债券型 |
| `kfsjj_fjgs_ybgpx` | 分级子基金-分级固收-一级股票型 |
| `kfsjj_fjgs_zsx` | 分级子基金-分级固收-指数型 |
| `kfsjj_fjgs_czzqx` | 分级子基金-分级固收-纯债债券型 |
| `kfsjj_fjgs_jjzqx` | 分级子基金-分级固收-激进债券型 |
| `kfsjj_fjgg_wjzqx` | 分级子基金-分级杠杆-稳健债券型 |
| `kfsjj_fjgg_ybgpx` | 分级子基金-分级杠杆-一级股票型 |
| `kfsjj_fjgg_zsx` | 分级子基金-分级杠杆-指数型 |
| `kfsjj_fjgg_czzqx` | 分级子基金-分级杠杆-纯债债券型 |
| `kfsjj_fjgg_jjzqx` | 分级子基金-分级杠杆-激进债券型 |

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001（华夏成长混合） |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `dwjz` | `number` | 单位净值（元） |
| `zmjgm` | `number` | 总募集规模（万份） |
| `zjzfe` | `number` | 最近总份额（万份） |
| `clrq` | `string` | 成立日期 |
| `jjjl` | `string` | 基金经理 |

## 基金行情档案

### 净值回报

#### 历史净值（官网文档页可能尚未展示）

- **方法**：`fundf10_lsjz(code)`
- **路径**：`/jj/lsjz/{code}/{licence}`
- **更新频率**：每周六13:00
- **说明**：根据《所有基金列表》得到的基金代码作为参数得到该基金的历史净值，按净值日期降序。

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码 |
| `mc` | `string` | 基金名称 |
| `t` | `string` | 净值日期 |
| `dwjz` | `string` | 单位净值 |
| `ljjz` | `string` | 累计净值 |
| `zzl` | `string` | 日增长率 |
| `sgzt` | `string` | 申购状态 |
| `shzt` | `string` | 赎回状态 |
| `fhsp` | `string` | 分红送配 |

#### 分红送配（官网文档页可能尚未展示）

- **方法**：`fundf10_fhps(code)`
- **路径**：`/jj/fhps/{code}/{licence}`
- **更新频率**：每周六13:00
- **说明**：根据《所有基金列表》得到的基金代码作为参数得到该基金的历史分红送配，按权益登记日降序。

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码 |
| `mc` | `string` | 基金名称 |
| `nf` | `string` | 年份 |
| `djr` | `string` | 权益登记日 |
| `cxr` | `string` | 除息日 |
| `mffh` | `string` | 每份分红 |
| `ffr` | `string` | 分红发放日 |

#### 阶段统计（官网文档页可能尚未展示）

- **方法**：`fundf10_jdtj(code)`
- **路径**：`/jj/jdtj/{code}/{licence}`
- **更新频率**：每周六13:00
- **说明**：根据《所有基金列表》得到的基金代码作为参数得到不同维度（参看下方的“统计维度说明”）的阶段统计。

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `jjjdzf` | `阶段涨幅` |  |
| `jjjdtlpj` | `阶段同类平均涨幅` |  |
| `jjjdtlpm` | `阶段涨幅同类排名` |  |
| `jjjdtlpmbd` | `阶段涨幅同类排名变动` |  |
| `jjjdsfwpm` | `阶段涨幅四分位排名` |  |

#### 季度涨幅明细（官网文档页可能尚未展示）

- **方法**：`fundf10_jdzfmx(code)`
- **路径**：`/jj/jdzfmx/{code}/{licence}`
- **更新频率**：每周六13:00
- **说明**：根据《所有基金列表》得到的基金代码作为参数得到该基金的季度涨幅明细，按年份降序。

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `y` | `string` | 年份 |
| `zf1` | `string` | 1季度涨幅 |
| `zf2` | `string` | 2季度涨幅 |
| `zf3` | `string` | 3季度涨幅 |
| `zf4` | `string` | 4季度涨幅 |

### 基本资料

#### 基金概况（官网文档页可能尚未展示）

- **方法**：`fundf10_jjgk(code)`
- **路径**：`/jj/jjgk/{code}/{licence}`
- **更新频率**：每周六13:00
- **说明**：根据《所有基金列表》得到的基金代码作为参数得到基金的基本介绍。

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码 |
| `qc` | `string` | 基金全称 |
| `jc` | `string` | 基金简称 |
| `lx` | `string` | 基金类型 |
| `pub` | `string` | 发行日期 |
| `gm` | `string` | 成立日期/规模 |
| `zcgm` | `string` | 资产规模 |
| `fegm` | `string` | 份额规模 |
| `glr` | `string` | 基金管理人 |
| `tgr` | `string` | 基金托管人 |
| `jlr` | `string` | 基金经理人 |
| `ljfh` | `string` | 成立以来分红 |
| `glfv` | `string` | 管理费率 |
| `tgfl` | `string` | 托管费率 |
| `xsfl` | `string` | 销售服务费率 |
| `rgfl` | `string` | 最高认购费率 |
| `sgfl` | `string` | 最高申购费率 |
| `shfl` | `string` | 最高赎回费率 |
| `bjjz` | `string` | 业绩比较基准 |
| `gzbd` | `string` | 跟踪标的 |
| `tzmb` | `string` | 投资目标 |
| `tzln` | `string` | 投资理念 |
| `tzfw` | `string` | 投资范围 |
| `tzcl` | `string` | 投资策略 |
| `fhzc` | `string` | 分红政策 |
| `fxsytz` | `string` | 风险收益特征 |

### 基金业绩、分红、规模

#### 基金业绩（官网文档页可能尚未展示）

- **方法**：`fundf10_jjyj(code)`
- **路径**：`/jj/jjyj/{code}/{licence}`
- **更新频率**：每日21:00
- **说明**：获取单只基金业绩。根据《所有基金列表》的代码作为参数传入。

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001（华夏成长混合） |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `dwjz` | `number` | 单位净值 |
| `ljjz` | `number` | 累计净值 |
| `jsgy` | `number` | 近三个月(%) |
| `jlgy` | `number` | 近六个月(%) |
| `jyn` | `number` | 近一年(%) |
| `jnyl` | `number` | 今年以来(%) |
| `clyl` | `number` | 成立以来(%) |

#### 基金分红（官网文档页可能尚未展示）

- **方法**：`fundf10_jjfh(code)`
- **路径**：`/jj/jjfh/{code}/{licence}`
- **更新频率**：每日21:00
- **说明**：获取单只基金分红。根据《所有基金列表》的代码作为参数传入。

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001（华夏成长混合） |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `zxcxr` | `string` | 最新除息日 |
| `zxpxr` | `string` | 最新派息日 |
| `zxdwfh` | `number` | 最新单位分红 |
| `clrq` | `string` | 成立日期 |
| `qjfhcs` | `number` | 期间分红次数 |
| `qjljfh` | `number` | 期间累计分红 |

#### 基金规模（官网文档页可能尚未展示）

- **方法**：`fundf10_jjgm(code)`
- **路径**：`/jj/jjgm/{code}/{licence}`
- **更新频率**：每日21:00
- **说明**：获取单只基金规模。根据《所有基金列表》的代码作为参数传入。

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001（华夏成长混合） |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `dwjz` | `number` | 单位净值（元） |
| `zmjgm` | `number` | 总募集规模（万份） |
| `zjzfe` | `number` | 最近总份额（万份） |
| `clrq` | `string` | 成立日期 |
| `jjjl` | `string` | 基金经理 |

### 基金估值

#### 估值基金列表（官网文档页可能尚未展示）

- **方法**：`fundf10_gzlb()`
- **路径**：`/jj/gzlb/{licence}`
- **更新频率**：每日16:00
- **说明**：获取基金的代码和名称，用于《盘中最新估值》接口的参数传入。

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001 |
| `mc` | `string` | 基金名称，如：华夏成长混合 |

#### 盘中最新估值（官网文档页可能尚未展示）

- **方法**：`fundf10_pzzzgz(code)`
- **路径**：`/jj/pzzzgz/{code}/{licence}`
- **更新频率**：交易时间段每10分钟
- **说明**：根据《估值基金列表》得到的基金代码作为参数获取基金的盘中最新估值。

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001 |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `zxgz` | `number` | 盘中最新估值 |
| `zxjz` | `number` | 最新净值 |
| `ljjz` | `number` | 累计净值 |
| `gxsj` | `string` | 更新时间yyyy-MM-ddHH:mm:ss |

### 基金净值

#### 开放式基金净值（官网文档页可能尚未展示）

- **方法**：`fundf10_hqzksjz(code)`
- **路径**：`/jj/hqzksjz/{code}/{licence}`
- **更新频率**：每日21:00
- **说明**：获取单只基金净值。根据《所有基金列表》中类型为开放式基金（tp=1）的代码作为参数传入。

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001（华夏成长混合） |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `dwjz` | `number` | 单位净值 |
| `ljjz` | `number` | 累计净值 |
| `qyrjz` | `number` | 前一日净值 |
| `zde` | `number` | 涨跌额 |
| `zzl` | `number` | 增长率（%） |
| `sgzt` | `string` | 申购状态 |
| `jzrq` | `string` | 净值日期 |
| `glr` | `string` | 基金管理人 |
| `jjlx` | `string` | 基金类型 |

### 基金列表

#### 所有基金列表（官网文档页可能尚未展示）

- **方法**：`fundf10_all()`
- **路径**：`/jj/all/{licence}`
- **更新频率**：每日21:00
- **说明**：获取所有基金（包括开放式基金，封闭式基金、分级子基金）的代码和名称，主要用于“基金档案”、“基金行情”、“基金业绩”、“基金分红”、“基金规模”等接口的参数传入，请根据具体数据接口的描述引导使用。

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：000001 |
| `mc` | `string` | 基金名称，如：华夏成长混合 |
| `tp` | `number` | 基金类型。1：开放式基金，2：封闭式基金，3：分级子基金 |

### 基金经理

#### 在任基金经理列表（官网文档页可能尚未展示）

- **方法**：`fundf10_zrjl()`
- **路径**：`/jj/zrjl/{licence}`
- **更新频率**：每周六13:00
- **说明**：获取所有在任的基金经理。

| 字段 | 类型 | 说明 |
|------|------|------|
| `mz` | `string` | 基金经理名字 |
| `jlid` | `string` | 基金经理代码 |

### 基金行情

#### 封闭式基金列表（官网文档页可能尚未展示）

- **方法**：`fundf10_fbs()`
- **路径**：`/jj/fbs/{licence}`
- **更新频率**：每日16:00
- **说明**：获取封闭式基金的代码和名称，用于下方接口的参数传入。

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：sz180801 |
| `mc` | `string` | 基金名称，如：首钢绿能 |

#### ETF基金列表（官网文档页可能尚未展示）

- **方法**：`fundf10_etf()`
- **路径**：`/jj/etf/{licence}`
- **更新频率**：每日16:00
- **说明**：获取ETF基金的代码和名称，用于下方接口的参数传入。

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：sz159999 |
| `mc` | `string` | 基金名称，如：永赢中证500ETF |

#### LOF基金列表（官网文档页可能尚未展示）

- **方法**：`fundf10_lof()`
- **路径**：`/jj/lof/{licence}`
- **更新频率**：每日16:00
- **说明**：获取LOF基金的代码和名称，用于下方接口的参数传入。

| 字段 | 类型 | 说明 |
|------|------|------|
| `dm` | `string` | 基金代码，如：sz169201 |
| `mc` | `string` | 基金名称，如：浙商鼎盈LOF |

### 投资组合

#### 股票持仓（官网文档页可能尚未展示）

- **方法**：`fundf10_gpcc(code)`
- **路径**：`/jj/gpcc/{code}/{licence}`
- **更新频率**：每周六13:00
- **说明**：根据《所有基金列表》得到的基金代码作为参数得到该基金的历年投资股票组合，按截止时间降序。

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `jd` | `string` | 季度 |
| `t` | `string` | 截止时间 |
| `dm` | `string` | 股票代码 |
| `mc` | `string` | 股票名称 |
| `jzbl` | `string` | 占净值比例 |
| `cgs` | `string` | 持股数（万股） |
| `ccsz` | `string` | 持仓市值（万元） |

#### 债券持仓（官网文档页可能尚未展示）

- **方法**：`fundf10_zqcc(code)`
- **路径**：`/jj/zqcc/{code}/{licence}`
- **更新频率**：每周六13:00
- **说明**：根据《所有基金列表》得到的基金代码作为参数得到该基金的历年投资债券持仓，按截止时间降序。

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `jd` | `string` | 季度 |
| `t` | `string` | 截止时间 |
| `dm` | `string` | 债券代码 |
| `mc` | `string` | 债券名称 |
| `jzbl` | `string` | 占净值比例 |
| `ccsz` | `string` | 持仓市值（万元） |

#### 行业配置（官网文档页可能尚未展示）

- **方法**：`fundf10_hypz(code)`
- **路径**：`/jj/hypz/{code}/{licence}`
- **更新频率**：每周六13:00
- **说明**：根据《所有基金列表》得到的基金代码作为参数得到该基金的历年行业配置情况，按截止时间降序。

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `jd` | `string` | 季度 |
| `t` | `string` | 截止时间 |
| `hy` | `string` | 行业类别 |
| `jzbl` | `string` | 占净值比例 |
| `ccsz` | `string` | 持仓市值（万元） |

#### 资产配置（官网文档页可能尚未展示）

- **方法**：`fundf10_zcpz(code)`
- **路径**：`/jj/zcpz/{code}/{licence}`
- **更新频率**：每周六13:00
- **说明**：根据《所有基金列表》得到的基金代码作为参数得到该基金的历年资产配置情况，按报告期降序。

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 报告期 |
| `gpzjb` | `string` | 股票占净比 |
| `zqzjb` | `string` | 债券占净比 |
| `xjzjb` | `string` | 现金占净比 |
| `jzc` | `string` | 净资产（亿元） |

### 规模份额

#### 规模变动（官网文档页可能尚未展示）

- **方法**：`fundf10_gmbd(code)`
- **路径**：`/jj/gmbd/{code}/{licence}`
- **更新频率**：每周六13:00
- **说明**：根据《所有基金列表》得到的基金代码作为参数得到该基金的历年的规模变动，按日期降序。

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 日期 |
| `qjsg` | `string` | 期间申购（亿份） |
| `qjsh` | `string` | 期间赎回（亿份） |
| `qmzfe` | `string` | 期末总份额（亿份） |
| `qmjzc` | `string` | 期末净资产（亿元） |
| `zcbdl` | `string` | 净资产变动率 |

#### 持有人结构（官网文档页可能尚未展示）

- **方法**：`fundf10_cyrjg(code)`
- **路径**：`/jj/cyrjg/{code}/{licence}`
- **更新频率**：每周六13:00
- **说明**：根据《所有基金列表》得到的基金代码作为参数得到该基金的历年的持有人结构变化，按公告日期降序。

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | `string` | 公告日期 |
| `jgbl` | `string` | 机构持有比例 |
| `grbl` | `string` | 个人持有比例 |
| `nbbl` | `string` | 内部持有比例 |
| `zfe` | `string` | 总份额（亿份） |

## 量化因子

### 主题因子

#### 估值因子

- **方法**：`factor_valuation(code)`
- **路径**：`/factor/valuation/{code}/{licence}`
- **更新频率**：每个交易日 16:30 后；财务随财报更新
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。返回单只股票估值类因子（贵不贵），用于价值比较与筛选。

| 参数 | 说明 |
|------|------|
| `code` | 股票代码，如 600519 |
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | `string` | 股票代码，如 600519 |
| `name` | `string` | 股票名称 |
| `trade_date` | `string` | 因子交易日，YYYYMMDD |
| `update_time` | `string` | 服务端计算完成时间，YYYY-MM-DD HH:mm:ss |
| `report_period` | `string` | 财务类可选，如 2026Q2 |
| `calc_version` | `string` | 口径版本，如 1.0 |
| `pe_ttm` | `number/null` | 市盈率(TTM)，倍 |
| `pe_ttm_rank` | `int/null` | pe_ttm 全市场升序排名（越小越便宜） |
| `pb` | `number/null` | 市净率，倍 |
| `pb_rank` | `int/null` | pb 升序排名 |
| `ps_ttm` | `number/null` | 市销率(TTM)，倍 |
| `ps_ttm_rank` | `int/null` | ps_ttm 升序排名 |
| `pcf_ttm` | `number/null` | 市现率(TTM)，倍 |
| `pcf_ttm_rank` | `int/null` | pcf_ttm 升序排名 |
| `ev_ebitda` | `number/null` | 企业价值倍数（第三步） |
| `ev_ebitda_rank` | `int/null` | ev_ebitda 升序排名（第三步） |
| `peg` | `number/null` | 市盈增长比 |
| `peg_rank` | `int/null` | peg 升序排名 |
| `graham_value` | `number/null` | 格雷厄姆内在价值，元 |
| `price_vs_graham` | `number/null` | 相对格雷厄姆偏离，% |
| `graham_rank` | `int/null` | price_vs_graham 升序排名 |

#### 质量因子

- **方法**：`factor_quality(code)`
- **路径**：`/factor/quality/{code}/{licence}`
- **更新频率**：财报披露后更新；每个交易日校验最新报告期
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。返回盈利能力、资产效率与财务健康度指标。

| 参数 | 说明 |
|------|------|
| `code` | 股票代码，如 600519 |
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | `string` | 股票代码，如 600519 |
| `name` | `string` | 股票名称 |
| `trade_date` | `string` | 因子交易日，YYYYMMDD |
| `update_time` | `string` | 服务端计算完成时间，YYYY-MM-DD HH:mm:ss |
| `report_period` | `string` | 财务类可选，如 2026Q2 |
| `calc_version` | `string` | 口径版本，如 1.0 |
| `roe_ttm` | `number/null` | 净资产收益率(TTM)，% |
| `roe_ttm_rank` | `int/null` | 降序排名 |
| `roa_ttm` | `number/null` | 总资产收益率(TTM)，% |
| `roa_ttm_rank` | `int/null` | 降序排名 |
| `gross_margin` | `number/null` | 毛利率，% |
| `gross_margin_rank` | `int/null` | 降序排名 |
| `net_margin` | `number/null` | 净利率，% |
| `net_margin_rank` | `int/null` | 降序排名 |
| `debt_ratio` | `number/null` | 资产负债率，% |
| `debt_ratio_rank` | `int/null` | 升序排名 |
| `current_ratio` | `number/null` | 流动比率 |
| `current_ratio_rank` | `int/null` | 降序排名 |
| `asset_turnover` | `number/null` | 总资产周转率，次 |
| `asset_turnover_rank` | `int/null` | 降序排名 |
| `accrual_ratio` | `number/null` | 应计项比率 |
| `accrual_ratio_rank` | `int/null` | 升序排名（越低利润质量通常越好） |

#### 成长因子

- **方法**：`factor_growth(code)`
- **路径**：`/factor/growth/{code}/{licence}`
- **更新频率**：财报披露后更新
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。返回营收/利润/EPS 同比与 3 年复合增速。

| 参数 | 说明 |
|------|------|
| `code` | 股票代码，如 600519 |
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | `string` | 股票代码，如 600519 |
| `name` | `string` | 股票名称 |
| `trade_date` | `string` | 因子交易日，YYYYMMDD |
| `update_time` | `string` | 服务端计算完成时间，YYYY-MM-DD HH:mm:ss |
| `report_period` | `string` | 财务类可选，如 2026Q2 |
| `calc_version` | `string` | 口径版本，如 1.0 |
| `rev_yoy` | `number/null` | 营收同比，% |
| `rev_yoy_rank` | `int/null` | 降序排名 |
| `rev_cagr_3y` | `number/null` | 营收 3 年复合增速，% |
| `rev_cagr_3y_rank` | `int/null` | 降序排名 |
| `profit_yoy` | `number/null` | 归母净利润同比，% |
| `profit_yoy_rank` | `int/null` | 降序排名 |
| `profit_cagr_3y` | `number/null` | 利润 3 年复合增速，% |
| `profit_cagr_3y_rank` | `int/null` | 降序排名 |
| `eps_yoy` | `number/null` | EPS 同比，% |
| `eps_yoy_rank` | `int/null` | 降序排名 |
| `eps_cagr_3y` | `number/null` | EPS 3 年复合增速，% |
| `eps_cagr_3y_rank` | `int/null` | 降序排名 |
| `rev_profit_scissors` | `number/null` | 营收利润剪刀差 = rev_yoy - profit_yoy |

#### 动量因子

- **方法**：`factor_momentum(code)`
- **路径**：`/factor/momentum/{code}/{licence}`
- **更新频率**：每个交易日 16:30 后
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。返回价格动量、相对强弱与距 52 周高点距离。

| 参数 | 说明 |
|------|------|
| `code` | 股票代码，如 600519 |
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | `string` | 股票代码，如 600519 |
| `name` | `string` | 股票名称 |
| `trade_date` | `string` | 因子交易日，YYYYMMDD |
| `update_time` | `string` | 服务端计算完成时间，YYYY-MM-DD HH:mm:ss |
| `report_period` | `string` | 财务类可选，如 2026Q2 |
| `calc_version` | `string` | 口径版本，如 1.0 |
| `momentum_5d` | `number/null` | 5 日收益率，% |
| `momentum_20d` | `number/null` | 20 日收益率，% |
| `momentum_60d` | `number/null` | 60 日收益率，% |
| `momentum_120d` | `number/null` | 120 日收益率，% |
| `momentum_20d_rank` | `int/null` | momentum_20d 降序排名 |
| `rs_20d` | `number/null` | 20 日相对强度（相对沪深300） |
| `rs_20d_rank` | `int/null` | 降序排名 |
| `high52_distance` | `number/null` | 距 52 周高点，% |
| `high52_distance_rank` | `int/null` | 降序排名 |
| `ma_deviation` | `number/null` | 相对 MA250 偏离，% |

#### 资金面因子

- **方法**：`factor_capital(code)`
- **路径**：`/factor/capital/{code}/{licence}`
- **更新频率**：每个交易日 16:30 后（北向依赖原料到位时间）
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。返回主力资金与北向资金相关因子。

| 参数 | 说明 |
|------|------|
| `code` | 股票代码，如 600519 |
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | `string` | 股票代码，如 600519 |
| `name` | `string` | 股票名称 |
| `trade_date` | `string` | 因子交易日，YYYYMMDD |
| `update_time` | `string` | 服务端计算完成时间，YYYY-MM-DD HH:mm:ss |
| `report_period` | `string` | 财务类可选，如 2026Q2 |
| `calc_version` | `string` | 口径版本，如 1.0 |
| `north_5d_net` | `number/null` | 北向 5 日净买入，元；数据源待接入，当前按设计返回空（赠品合理范围） |
| `north_20d_net` | `number/null` | 北向 20 日净买入，元；数据源待接入，当前按设计返回空（赠品合理范围） |
| `north_holding_ratio` | `number/null` | 北向持股占流通股，%；数据源待接入，当前按设计返回空（赠品合理范围） |
| `main_5d_net` | `number/null` | 主力 5 日净流入，元 |
| `main_20d_net` | `number/null` | 主力 20 日净流入，元 |
| `flow_5d_ratio` | `number/null` | 5 日资金流向比 |
| `flow_20d_ratio` | `number/null` | 20 日资金流向比 |
| `big_order_net_5d` | `number/null` | 5 日特大单净额，元 |

#### 技术信号因子

- **方法**：`factor_signal(code)`
- **路径**：`/factor/signal/{code}/{licence}`
- **更新频率**：每个交易日 16:30 后
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。返回 MACD/均线/KDJ/BOLL 等定性信号与量比、RSI，便于直接筛选。

| 参数 | 说明 |
|------|------|
| `code` | 股票代码，如 600519 |
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | `string` | 股票代码，如 600519 |
| `name` | `string` | 股票名称 |
| `trade_date` | `string` | 因子交易日，YYYYMMDD |
| `update_time` | `string` | 服务端计算完成时间，YYYY-MM-DD HH:mm:ss |
| `report_period` | `string` | 财务类可选，如 2026Q2 |
| `calc_version` | `string` | 口径版本，如 1.0 |
| `macd_signal` | `string` | golden_cross / death_cross / bull_divergence / bear_divergence / none |
| `ma5_ma20_cross` | `string` | golden / death / long / short |
| `ma20_ma60_cross` | `string` | golden / death / long / short |
| `kdj_signal` | `string` | oversold / overbought / golden_cross / death_cross / none |
| `boll_position` | `string` | upper / middle / lower / breakout_upper / breakout_lower |
| `volume_ratio` | `number/null` | 量比 |
| `rsi_14` | `number/null` | 14 日 RSI |
| `ma_trend` | `string` | up / down / consolidation |
| `boll_squeeze` | `bool` | 布林收口 |
| `volume_price_divergence` | `string` | bull_divergence / bear_divergence / none |

#### 风险因子

- **方法**：`factor_risk(code)`
- **路径**：`/factor/risk/{code}/{licence}`
- **更新频率**：每个交易日 16:30 后
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。返回 Beta、波动率、夏普、最大回撤、VaR 等风险指标。

| 参数 | 说明 |
|------|------|
| `code` | 股票代码，如 600519 |
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | `string` | 股票代码，如 600519 |
| `name` | `string` | 股票名称 |
| `trade_date` | `string` | 因子交易日，YYYYMMDD |
| `update_time` | `string` | 服务端计算完成时间，YYYY-MM-DD HH:mm:ss |
| `report_period` | `string` | 财务类可选，如 2026Q2 |
| `calc_version` | `string` | 口径版本，如 1.0 |
| `beta_252d` | `number/null` | 252 日 Beta（对沪深300） |
| `beta_rank` | `int/null` | 升序排名 |
| `volatility_20d` | `number/null` | 20 日年化波动率，% |
| `volatility_60d` | `number/null` | 60 日年化波动率，% |
| `sharpe_252d` | `number/null` | 252 日夏普 |
| `sharpe_rank` | `int/null` | 降序排名 |
| `max_drawdown_252d` | `number/null` | 252 日最大回撤，% |
| `max_drawdown_rank` | `int/null` | 降序排名（越接近 0 越好） |
| `var_95` | `number/null` | 95% VaR（年化表述见公式） |

#### 分红因子

- **方法**：`factor_dividend(code)`
- **路径**：`/factor/dividend/{code}/{licence}`
- **更新频率**：分红方案落地后更新；股息率随股价日更
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。返回股息率、支付率、连续分红年数等。第一步为 F10 试用口径（source=hscp_jnfh），第三步升为事件表正式口径。

| 参数 | 说明 |
|------|------|
| `code` | 股票代码，如 600519 |
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | `string` | 股票代码，如 600519 |
| `name` | `string` | 股票名称 |
| `trade_date` | `string` | 因子交易日，YYYYMMDD |
| `update_time` | `string` | 服务端计算完成时间，YYYY-MM-DD HH:mm:ss |
| `report_period` | `string` | 财务类可选，如 2026Q2 |
| `calc_version` | `string` | 口径版本，如 1.0 |
| `dividend_yield` | `number/null` | 股息率，%（第一步试用/第三步正式） |
| `dividend_yield_rank` | `int/null` | 降序排名 |
| `payout_ratio` | `number/null` | 股利支付率，%（第一步试用/第三步正式） |
| `payout_ratio_rank` | `int/null` | 降序排名 |
| `dividend_continuous_years` | `int/null` | 连续分红年数（第一步试用/第三步正式） |
| `dividend_growth_3y` | `number/null` | 3 年分红复合增速，%（第一步试用/第三步正式） |
| `dividend_avg_3y` | `number/null` | 3 年平均股息率，%（第一步试用/第三步正式） |

#### 规模流动性因子

- **方法**：`factor_scale(code)`
- **路径**：`/factor/scale/{code}/{licence}`
- **更新频率**：每个交易日 16:30 后
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。返回市值规模与流动性指标。

| 参数 | 说明 |
|------|------|
| `code` | 股票代码，如 600519 |
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | `string` | 股票代码，如 600519 |
| `name` | `string` | 股票名称 |
| `trade_date` | `string` | 因子交易日，YYYYMMDD |
| `update_time` | `string` | 服务端计算完成时间，YYYY-MM-DD HH:mm:ss |
| `report_period` | `string` | 财务类可选，如 2026Q2 |
| `calc_version` | `string` | 口径版本，如 1.0 |
| `total_market_cap` | `number/null` | 总市值，元 |
| `float_market_cap` | `number/null` | 流通市值，元 |
| `cap_rank` | `int/null` | 总市值降序排名 |
| `float_ratio` | `number/null` | 流通比例，% |
| `turnover_20d_avg` | `number/null` | 20 日平均换手率，% |
| `amihud_20d` | `number/null` | Amihud 流动性 |
| `cap_scale` | `string` | 超大盘/大盘/中盘/小盘/微盘 |

#### 情绪事件因子

- **方法**：`factor_sentiment(code)`
- **路径**：`/factor/sentiment/{code}/{licence}`
- **更新频率**：涨跌停每日批算；关注度/事件依原料更新频率
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。返回涨跌停热度、关注度与近期重要事件。

| 参数 | 说明 |
|------|------|
| `code` | 股票代码，如 600519 |
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | `string` | 股票代码，如 600519 |
| `name` | `string` | 股票名称 |
| `trade_date` | `string` | 因子交易日，YYYYMMDD |
| `update_time` | `string` | 服务端计算完成时间，YYYY-MM-DD HH:mm:ss |
| `report_period` | `string` | 财务类可选，如 2026Q2 |
| `calc_version` | `string` | 口径版本，如 1.0 |
| `limit_up_count_20d` | `int/null` | 近 20 日涨停次数 |
| `limit_down_count_20d` | `int/null` | 近 20 日跌停次数 |
| `attention_score` | `int/null` | 关注度 0–100；数据源待接入，当前按设计返回空（赠品合理范围） |
| `attention_rank` | `int/null` | 关注度降序排名（第三步） |
| `recent_event` | `string/null` | 近期重要事件类型或 none（第三步） |
| `event_date` | `string/null` | 事件日 YYYYMMDD（第三步） |
| `event_impact` | `string/null` | positive / negative / neutral（第三步） |

#### 单股全因子

- **方法**：`factor_all(code)`
- **路径**：`/factor/all/{code}/{licence}`
- **更新频率**：同各主题日终批算
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。一次返回该股各主题因子（按主题分组）。未上线字段为 null 或不出现。

| 参数 | 说明 |
|------|------|
| `code` | 股票代码，如 600519 |
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |
| `fields` | 否；逗号分隔字段白名单；不传返回已开通全部 |
| `exclude_rank` | 否；1=去掉 *_rank 字段 |

路径参数：
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | `string` | 股票代码，如 600519 |
| `name` | `string` | 股票名称 |
| `trade_date` | `string` | 因子交易日，YYYYMMDD |
| `update_time` | `string` | 服务端计算完成时间，YYYY-MM-DD HH:mm:ss |
| `report_period` | `string` | 财务类可选，如 2026Q2 |
| `calc_version` | `string` | 口径版本，如 1.0 |
| `valuation` | `object` | 估值主题字段，同估值因子接口 |
| `quality` | `object` | 质量主题字段，同质量因子接口 |
| `growth` | `object` | 成长主题字段，同成长因子接口 |
| `momentum` | `object` | 动量主题字段，同动量因子接口 |
| `capital` | `object` | 资金面主题字段，同资金面因子接口 |
| `signal` | `object` | 技术信号主题字段，同技术信号因子接口 |
| `risk` | `object` | 风险主题字段，同风险因子接口 |
| `dividend` | `object` | 分红主题字段，同分红因子接口 |
| `scale` | `object` | 规模流动性主题字段，同规模流动性因子接口 |
| `sentiment` | `object` | 情绪事件主题字段，同情绪事件因子接口 |

### 元数据

#### 因子列表

- **方法**：`factor_list()`
- **路径**：`/factor/list/{licence}`
- **更新频率**：因子元数据变更时更新（非行情日更）
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。返回平台全部因子元数据，供 SDK / 前端初始化、筛选器配置。

| 参数 | 说明 |
|------|------|
| `category` | 否；valuation/quality/growth/momentum/capital/signal/risk/dividend/scale/sentiment |
| `tier` | 否；free / plus / pro |
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |

| 字段 | 类型 | 说明 |
|------|------|------|
| `factor_id` | `string` | 因子唯一 ID，如 pe_ttm |
| `name` | `string` | 中文名 |
| `category` | `string` | 主题英文标识 |
| `category_name` | `string` | 主题中文名 |
| `unit` | `string` | 单位 |
| `tier` | `string` | 最低套餐 |
| `direction` | `string` | lower_better / higher_better / neutral |
| `description` | `string` | 一句话说明 |
| `operators` | `array` | 筛选运算符 |
| `typical_range` | `string` | A 股典型范围 |
| `update_freq` | `string` | daily / weekly / quarterly / realtime |
| `calc_version` | `string` | 当前计算方法版本 |

#### 因子分类树

- **方法**：`factor_categories()`
- **路径**：`/factor/categories/{licence}`
- **更新频率**：元数据变更时更新
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。返回十大主题及因子数量，用于文档导航与智选分类。

| 参数 | 说明 |
|------|------|
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |

| 字段 | 类型 | 说明 |
|------|------|------|
| `category` | `string` | 主题 ID |
| `name` | `string` | 主题中文名 |
| `count` | `int` | 该主题因子数 |

### 排名与历史

#### 因子排名

- **方法**：`factor_rank(factor_id)`
- **路径**：`/factor/rank/{factor_id}/{licence}`
- **更新频率**：每个交易日日终预计算
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。全市场（或板块）按单因子排序分页。

| 参数 | 说明 |
|------|------|
| `factor_id` | 因子 ID，如 roe_ttm |
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |
| `order` | 否；desc\|asc |
| `page` | 否；页码 |
| `page_size` | 否；默认 50，最大 200 |
| `board` | 否；main\|star\|gem\|bj\|all |

路径参数：
- `factor_id`

| 字段 | 类型 | 说明 |
|------|------|------|
| `rank` | `int` | 名次 |
| `code` | `string` | 代码 |
| `name` | `string` | 名称 |
| `value` | `number/null` | 因子值 |

#### 因子 Top N

- **方法**：`factor_top(factor_id, arg)`
- **路径**：`/factor/top/{factor_id}/{arg}/{licence}`
- **更新频率**：同排名预计算
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。返回该因子前 N 名（N 建议 ≤200）。

| 参数 | 说明 |
|------|------|
| `factor_id` | 因子 ID，如 roe_ttm |
| `n` | 返回条数，建议 ≤200 |
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |

路径参数：
- `factor_id`
- `arg`

| 字段 | 类型 | 说明 |
|------|------|------|
| `rank` | `int` | 名次 |
| `code` | `string` | 代码 |
| `name` | `string` | 名称 |
| `value` | `number/null` | 因子值 |

#### 因子历史序列

- **方法**：`factor_history(factor_id, code)`
- **路径**：`/factor/history/{factor_id}/{code}/{licence}`
- **更新频率**：历史表随日终追加
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。返回单股单因子历史点列，用于画图与回测。

| 参数 | 说明 |
|------|------|
| `factor_id` | 因子 ID，如 pe_ttm |
| `code` | 股票代码，如 600519 |
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |
| `st` | 否；开始日 YYYYMMDD |
| `et` | 否；结束日 YYYYMMDD |
| `limit` | 否；返回点数上限 |

路径参数：
- `factor_id`
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `trade_date` | `string` | YYYYMMDD |
| `value` | `number/null` | 当日因子值 |

#### 因子分位数

- **方法**：`factor_percentile(factor_id, code)`
- **路径**：`/factor/percentile/{factor_id}/{code}/{licence}`
- **更新频率**：基于历史序列现算或预计算
- **说明**：【调用条件】须已加购「Quant Pro 增强包」或「麦蕊因子包」；仅购买基础证书未加购上述模块时调用将返回 403。Quant Pro 已含全部因子权益（因子为随包赠品）。68 因子中 north_5d_net / north_20d_net / north_holding_ratio / attention_score 因数据源待接入按设计可为空，属赠品合理范围，不影响其余 64 个字段。当前值在自身历史窗口中的分位及统计量。

| 参数 | 说明 |
|------|------|
| `factor_id` | 因子 ID，如 pe_ttm |
| `code` | 股票代码，如 600519 |
| `licence` | 用户证书码（路径参数）。须已加购「Quant Pro 增强包」或「麦蕊因子包」，仅基础证书不可用 |
| `period` | 否；窗口天数，默认 252 |

路径参数：
- `factor_id`
- `code`

| 字段 | 类型 | 说明 |
|------|------|------|
| `current_value` | `number/null` | 当前值 |
| `period` | `int` | 窗口天数 |
| `percentile` | `number/null` | 0–100 历史分位 |
| `description` | `string` | 白话说明 |
| `history_min` | `number/null` | 窗口最小值 |
| `history_max` | `number/null` | 窗口最大值 |
| `history_median` | `number/null` | 窗口中位数 |
| `history_mean` | `number/null` | 窗口均值 |
