# coding: utf-8

from __future__ import annotations

from datetime import datetime


def datetime_to_constellation(dt: datetime) -> str:
    """日期转星座"""
    dates: tuple[int, ...] = (
        20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 22)
    constellations: tuple[str, ...] = (
        "摩羯座", "水瓶座", "双鱼座", "白羊座", "金牛座", "双子座", "巨蟹座",
        "狮子座", "处女座", "天秤座", "天蝎座", "射手座", "摩羯座")
    if dt.day < dates[dt.month - 1]:
        return constellations[dt.month - 1]
    else:
        return constellations[dt.month]
