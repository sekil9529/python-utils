# data_type_utils

数据类型工具

### 1.attr_dict

- 扩展字典，实现 __setattr__ 和 __getattr__
- demo

```
from data_type_utils.attr_dict import AttrDict


dic = AttrDict()
dic.a = 100
dic.b = "200"
```

### 2.error_code

- NamedTuple + Enum 实现错误码的数据结构

- demo

```
from __future__ import annotations

from data_type_utils.error_code import ECData, BaseECEnum


class ECEnum(BaseECEnum):
    """错误码枚举类"""
    ServerError = ECData(code="500", message="服务器异常")
    MethodNotAllowed = ECData(code="405", message="非法的请求方式")
```