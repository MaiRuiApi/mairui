# 麦蕊 SDK 全接口调阅 Demo（Python）

版本对齐 SDK **1.2.1**。串行调用本语言 SDK 的全部公开方法，打印 `OK|SKIP|FAIL`、耗时与数据摘要。

## 准备

1. 申请证书：https://www.mairuiapi.com （获取 licence UUID）
2. 安装依赖：

```text
pip install -U mairui==1.2.1
```

3. 设置环境变量（**勿把证书写进代码**）：

```powershell
$env:MAIRUI_LICENCE = "你的证书UUID"
```

```bash
export MAIRUI_LICENCE='你的证书UUID'
```

## 运行

```text
python run_demo.py
```

可选：`$env:MAIRUI_DEMO_QUIET=1` 只输出汇总。

## 结果说明

- **OK**：调用成功（后附截断预览）
- **SKIP**：预期可跳过（如主站无 VIP 权限的 `stock_vip_history` 返回 404）
- **FAIL**：异常；进程以退出码 2 结束
- 偶发 **429** 请稍后重跑

## 注意

全量约 200+ 次请求，耗时数分钟，请注意证书限流。示例参数仅为演示（如 `000001.SZ`、`lt=1`）。
