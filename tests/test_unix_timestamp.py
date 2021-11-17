# coding: utf-8

from __future__ import annotations

from datetime import datetime

from utils.datetime_utils.unix_timestamp import from_unix_timestamp, to_unix_timestamp


def test_unix_timestamp() -> None:
    unix_ts: float = -1.0
    dt: datetime = from_unix_timestamp(unix_ts)
    print(dt)
    assert to_unix_timestamp(dt) == unix_ts
