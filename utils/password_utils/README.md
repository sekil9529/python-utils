# password_utils

密码工具

### 1. make_password

- 制作密码
    - 制作md5密码
- demo
 
```python
from __future__ import annotations

from collections.abc import Callable
from functools import partial

from utils.password_utils.make_password import make_md5_password as base_make_md5_password

# 项目名称
PROJECT_NAME: str = "tests"

# 制作md5密码函数
make_md5_password: Callable = partial(base_make_md5_password, prefix=PROJECT_NAME)


make_md5_password("123456")
```
