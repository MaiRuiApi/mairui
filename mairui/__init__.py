"""麦蕊智数（api.mairuiapi.com）Python SDK。

覆盖官网公开 API 文档中的接口；绑定 licence 后按函数调用即可。
文档入口：https://mairuiapi.com/hsdata
"""

from mairui.client import Client
from mairui.exceptions import (
    MairuiAPIError,
    MairuiAuthError,
    MairuiHTTPError,
    MairuiTimeoutError,
)

__all__ = [
    "Client",
    "MairuiAPIError",
    "MairuiAuthError",
    "MairuiHTTPError",
    "MairuiTimeoutError",
]

__version__ = "1.2.1"
