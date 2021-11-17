# coding: utf-8

from __future__ import annotations

from random import sample

from utils.invite_code_utils.invite_code import InviteCode


def test_invite_code() -> None:
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
    try:
        ic.encode(max_uid+1, digit=k)
    except Exception as e:
        assert isinstance(e, ValueError)