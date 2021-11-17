# python-utils

实用工具类、函数

# 环境

- Python-3.7

# 模块功能说明

- tests: 其他功能模块的测试代码
- utils/log_utils: 日志工具
    - logger_proxy: logger代理器
- utils/data_type_utils: 数据类型工具
    - attr_dict: Attr字典
    - error_code: 提供基于 NamedTuple + Enum 的错误码数据结构
- utils/datetime_utils: 日期工具
    - unix_timestamp: 提供unix时间戳与datetime互相转换的函数
    - constellation: 提供日期转换星座的函数
- utils/config_utils: 配置工具
    - config: 配置类，支持配置文件转字典
- utils/singleton_utils: 单例工具
    - singleton_type: 单例类（元类）
- utils/password_utils: 密码工具
    - make_password: 生成密码方法
- utils/django_utils: django工具
    - mysql_session: 提供执行原生SQL的方法
- utils/invite_code_utils: 邀请码工具
    - invite_code: 根据用户id（int）生成邀请码；根据邀请码解析用户id

# 单元测试
python -m pytest
