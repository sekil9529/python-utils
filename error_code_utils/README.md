# error_code_utils

错误码工具

### 1.error_code

- NamedTuple + Enum 实现错误码的数据结构

- demo

```
from __future__ import annotations

from error_code_utils.error_code import ECData, BaseECEnum


class ECEnum(BaseECEnum):
    """错误码枚举类"""
    ServerError = ECData(code="500", message="服务器异常")
    MethodNotAllowed = ECData(code="405", message="非法的请求方式")
```
