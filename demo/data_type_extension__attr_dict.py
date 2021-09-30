# coding: utf-8

from __future__ import annotations

from importlib import import_module
import_module("_add_path")

import json

from data_type_extension.attr_dict import AttrDict


if __name__ == '__main__':
    dic = AttrDict(a=3, b=4)
    dic.update(a=100, c=200)
    dic.t1 = "asd"
    print(dic.c)
    print(isinstance(dic, dict))
    print(json.dumps(dic))
