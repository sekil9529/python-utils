# django_utils

单例工具

### 1.mysql_session

- 提供执行原生SQL的方法
- 依赖自定义模块
    - singleton_utils.singleton_type.SingletonType
- 依赖库
    - pymysql==1.0.2
    - django==2.2.24
- demo

```
from __future__ import annotations

from typing import Optional

from django_utils.mysql_session import MySQLSession


session: MySQLSession = MySQLSession()

# 1.仅执行语句
sql: str = "select t.id, t.name from t where t.name = %(name)s"
rows: int = session.exec_sql(sql, params={"name": "小明"})

# 2.执行并获取单行数据
sql: str = "select t.id, t.name from t where t.name = %s limit 1"
result: Optional[dict] = session.exec_and_fetchone(sql, params=("小明",))

# 3.执行并获取多行数据
sql: str = "select t.id, t.name from t where t.name != %(name)s limit 10"
results: tuple[dict, ...] = session.exec_and_fetchall(sql, params=("小明",))

# 4.使用原生cursor对象
sql: str = "select t.id, t.name from t where t.name = %(name)s limit 1"
with session.context_cursor() as cur:
    rows: int = cur.execute(sql, params={"name": "小明"})
    result: Optional[dict] = cur.fetchone()
```
