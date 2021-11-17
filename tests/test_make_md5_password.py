# coding: utf-8

from __future__ import annotations

from collections.abc import Callable
from functools import partial

from utils.password_utils.make_password import make_md5_password as base_make_md5_password

# 项目名称
PROJECT_NAME: str = "tests"

# 制作md5密码函数
make_md5_password: Callable = partial(base_make_md5_password, prefix=PROJECT_NAME)


def test_make_md5_password() -> None:
    base_pwd: str = "123456"
    password1: str = make_md5_password(base_pwd)
    password2: str = make_md5_password(base_pwd)
    assert password1 == password2
