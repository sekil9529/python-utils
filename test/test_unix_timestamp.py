# coding: utf-8

from __future__ import annotations

from importlib import import_module
import_module("_add_path")

from datetime import datetime

from datetime_utils.unix_timestamp import from_unix_timestamp, to_unix_timestamp


if __name__ == '__main__':
    unix_ts: float = -1.0
    dt: datetime = from_unix_timestamp(unix_ts)
    print(dt)
    assert to_unix_timestamp(dt) == unix_ts
