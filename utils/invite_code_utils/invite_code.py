# coding: utf-8

from __future__ import annotations

import random


class InviteCode:
    """邀请码

    生成公式:

    import string
    import random
    import re

    lst = list(string.digits + string.ascii_letters)  # 数字+大小写字母，共62个
    random.shuffle(lst)  # 乱序
    prefix_str = "".join(random.sample(lst, k=15))  # 随机筛选15个不重复的字符作为保留字符串
    source_str = re.sub("[" + prefix_str + "]", "",  "".join(lst))  # 剔除保留字符串

    # user_id上限计算公式
    len(source_str) ** digit -1
    # (62-15) ** 8 - 1 = 23811286661760
    """

    source_str = "6WopUze50t1QYHqMwAlfGPbJgaFZnvDT3d9ruVcjRKSEhCX"  # 源字符串
    prefix_str = "m2yB7xLk48isNIO"  # 保留字符串

    def encode(self, uid: int, digit: int = 8) -> str:
        """用户id生成激活码

        :param uid: 用户id
        :param digit: 位数上限
        """
        length: int = len(self.source_str)
        num: int = uid
        code: str = ""
        while num > 0:
            mod = num % length
            num = (num - mod) // length
            code += self.source_str[mod]
        if len(code) < digit:
            # 不足的从保留字符串中取值填充
            # 有放回的随机取k次值，作为前缀填充
            prefix_str = "".join(random.choices(self.prefix_str, k=digit - len(code)))
            code = prefix_str + code
        elif len(code) > digit:
            raise ValueError('激活码达到上限')
        return code

    def decode(self, code: str) -> int:
        """邀请码反解析uid

        code: 邀请码
        """
        # 移除前缀的保留字符
        code = code.lstrip(self.prefix_str)
        length: int = len(self.source_str)
        num: int = 0
        for i in range(len(code)):
            n = self.source_str.index(code[i]) * pow(length, i)
            num += n
        return num

