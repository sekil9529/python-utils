# coding: utf-8

from __future__ import annotations

from importlib import import_module
import_module("_add_path")

from data_type_utils.error_code import ECData, BaseECEnum


if __name__ == '__main__':
    try:
        class ECEnum(BaseECEnum):
            ServerError = ECData(code="500", message="服务器异常")
            MethodNotAllowed = ECData(code="500", message="非法的请求方式")
    except Exception as e:
        # print(e)
        assert isinstance(e, ValueError)


    class ECEnum(BaseECEnum):
        ServerError = ECData(code="500", message="服务器异常")
        MethodNotAllowed = ECData(code="405", message="非法的请求方式")

    assert ECEnum.ServerError.code == "500"
    assert ECEnum.MethodNotAllowed.code == "405"
