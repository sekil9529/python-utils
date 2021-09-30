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
