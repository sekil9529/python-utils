# coding: utf-8

from __future__ import annotations

from utils.data_type_utils.error_code import ECData, BaseECEnum


def test_error_code() -> None:
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
    assert ECEnum.ServerError.message == "服务器异常"
    assert ECEnum.ServerError.error == "ServerError"
    assert ECEnum.MethodNotAllowed.code == "405"
    try:
        ECEnum.ServerError.value == 1
    except Exception as e:
        assert isinstance(e, NotImplementedError)
