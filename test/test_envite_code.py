# coding: utf-8

from __future__ import annotations

from importlib import import_module
import_module("_add_path")

from random import sample

from invite_code_utils.invite_code import InviteCode


if __name__ == '__main__':
    k: int = 6
    max_uid: int = len(InviteCode.source_str) ** k - 1
    ic: InviteCode = InviteCode()
    for _ in range(10):
        uid: int = 999
        code: str = ic.encode(uid, digit=k)
        # print(uid, code, ic.decode(code))
        assert uid == ic.decode(code)
    for uid in sample(range(1, max_uid+1), k=min(100, max_uid)):
        code: str = ic.encode(uid, digit=k)
        # print(uid, code, ic.decode(code))
        assert uid == ic.decode(code)
