# coding: utf-8

"""
兼容windows环境
win下，如果unix时间戳是负数，互转时会出现 QSError 异常
"""

import calendar
from datetime import datetime, timedelta


def from_unix_timestamp(secs: float) -> datetime:
    """时间戳转datetime"""
    try:
        dt = datetime.fromtimestamp(secs)
    except OSError:
        dt = datetime(1970, 1, 1, 8) + timedelta(seconds=secs)
    return dt


def to_unix_timestamp(dt: datetime) -> float:
    """datetime转时间戳"""
    try:
        secs = dt.timestamp()
    except OSError:
        # 只能保留到整数位
        secs = float(calendar.timegm((dt + timedelta(hours=-8)).timetuple()))
    return secs
