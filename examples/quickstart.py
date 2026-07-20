#!/usr/bin/env python3
"""快速示例：把 YOUR-LICENCE 换成真实证书后运行。"""

from __future__ import annotations

import json
import os
import sys

# 允许直接从仓库运行而未 pip install
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mairui import Client, MairuiAPIError


def main() -> None:
    licence = os.environ.get("MAIRUI_LICENCE", "").strip()
    if not licence:
        print("请设置环境变量 MAIRUI_LICENCE=你的证书UUID")
        print("PowerShell 示例: $env:MAIRUI_LICENCE=\"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\"")
        sys.exit(1)

    with Client(licence=licence) as api:
        print("== 股票列表（截取前 2 条）==")
        data = api.stock_list()
        if isinstance(data, list):
            print(json.dumps(data[:2], ensure_ascii=False, indent=2))
        else:
            print(type(data), str(data)[:200])

        print("\n== 平安银行 日线最近 3 根 ==")
        bars = api.stock_history("000001.SZ", "d", "n", lt=3)
        print(json.dumps(bars, ensure_ascii=False, indent=2)[:800])

        print("\n== 批量 3 只股票最新日线 ==")
        batch = api.map(
            api.stock_latest,
            ["000001.SZ", "600519.SH", "000002.SZ"],
            period="d",
            dividend="n",
            lt=1,
            max_workers=3,
        )
        for code, row in zip(["000001.SZ", "600519.SH", "000002.SZ"], batch):
            print(code, "=>", str(row)[:120])


if __name__ == "__main__":
    try:
        main()
    except MairuiAPIError as e:
        print("API 错误:", e)
        sys.exit(2)
