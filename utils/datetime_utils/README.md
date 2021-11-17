# datetime_utils

日期工具

### 1.unix_timestamp

- 日期与时间戳互相转换
- windows环境下，负数unix时间戳与datetime转化时，会出现OSError，反之亦然
- demo

```
from datetime import datetime

from datetime_utils.unix_timestamp import from_unix_timestamp, to_unix_timestamp

# unix时间戳转datetime
unix_ts: float = -1.0
dt: datetime = from_unix_timestamp(unix_ts)

# datetime转unix时间戳
now: datetime = datetime.now()
unix_ts: float = to_unix_timestamp(now)
```

### 2.constellation/datetime_to_constellation

- 日期转换成星座
