# data_type_extension

数据类型扩展

### 1.attr_dict

- 扩展字典，实现 __setattr__ 和 __getattr__
- demo

```
from data_type_extension.attr_dict import AttrDict


dic = AttrDict()
dic.a = 100
dic.b = "200"
```
