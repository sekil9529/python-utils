# coding: utf-8

from __future__ import annotations

import json
import pytest

from utils.data_type_utils.attr_dict import AttrDict


def test_attr_dict() -> None:
    dic = AttrDict(a=3, b=4)
    dic.update(a=100, c=200)
    dic.t1 = "asd"
    assert dic.c
    assert isinstance(dic, dict)
    assert json.dumps(dic)
    try:
        dic.aaa
    except Exception as e:
        assert isinstance(e, AttributeError)
