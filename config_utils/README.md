# config_utils

配置工具

### 1.config

- 配置类
    - 提供配置文件（类似my.cnf的格式）转换成字典
- demo

```
from __future__ import annotations

from config_utils.config import Config

# 配置信息
CONFIG_INFO: dict[str, str] = Config("config.ini").to_dict()
```
