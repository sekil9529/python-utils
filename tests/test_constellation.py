# coding: utf-8

from __future__ import annotations

from datetime import date, datetime, timedelta

from utils.datetime_utils.constellation import datetime_to_constellation


def test_t() -> None:
    month_date_constellation_map: dict[str, tuple[str, str]] = {
        "白羊座": ("3.21", "4.19"),
        "金牛座": ("4.20", "5.20"),
        "双子座": ("5.21", "6.21"),
        "巨蟹座": ("6.22", "7.22"),
        "狮子座": ("7.23", "8.22"),
        "处女座": ("8.23", "9.22"),
        "天秤座": ("9.23", "10.23"),
        "天蝎座": ("10.24", "11.22"),
        "射手座": ("11.23", "12.21"),
        "摩羯座": ("12.22", "1.19"),
        "水瓶座": ("1.20", "2.18"),
        "双鱼座": ("2.19", "3.20"),
    }

    today: date = date.today()
    for k, v_tuple in month_date_constellation_map.items():
        v1, v2 = v_tuple
        start_dt: datetime = datetime(today.year, *(int(i) for i in v1.split(".")))
        end_dt: datetime = datetime(today.year, *(int(i) for i in v2.split(".")))
        if end_dt < start_dt:
            end_dt = end_dt.replace(year=end_dt.year + 1)
        mid_dt: datetime = start_dt + timedelta(days=(end_dt - start_dt).days // 2)
        assert datetime_to_constellation(start_dt) == k
        assert datetime_to_constellation(end_dt) == k
        assert datetime_to_constellation(mid_dt) == k
