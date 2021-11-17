# invite_code_utils

邀请码工具

### 1.invite_code

- 根据用户id（int）生成邀请码（str）；根据邀请码解析用户id

- demo

```
from invite_code_utils.invite_code import InviteCode


user_id: int = 10
ic: InviteCode = InviteCode()
code: str = ic.encode(user_id, digit=6)
```
