# coding: utf-8

from __future__ import annotations

from importlib import import_module
import_module("_add_path")

from collections.abc import Callable
from functools import partial

from password_utils.make_password import make_md5_password as base_make_md5_password

# 项目名称
PROJECT_NAME: str = "test"

# 制作md5密码函数
make_md5_password: Callable = partial(base_make_md5_password, prefix=PROJECT_NAME)


if __name__ == '__main__':
    base_pwd: str = "123456"
    password1: str = make_md5_password(base_pwd)
    password2: str = make_md5_password(base_pwd)
    assert password1 == password2
