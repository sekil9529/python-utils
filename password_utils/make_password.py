# coding: utf-8

import _hashlib
import hashlib

# 默认盐值
# 生成方式: import string; import random; ''.join(random.choices(string.printable, k=20))
DEFAULT_SALT: str = "^cc%\\w-cK%Nt -p}+n1'"


def make_md5_password(password: str, prefix: str) -> str:
    """制作md5密码

    :param password: 原始密码
    :param prefix: 前缀（一般为项目名）
    """
    salt: str = f"{prefix}{DEFAULT_SALT}"
    obj: _hashlib.HASH = hashlib.md5(f"{password}{salt}".encode("utf-8"))
    return obj.hexdigest()
