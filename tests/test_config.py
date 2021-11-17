# coding: utf-8

from __future__ import annotations

from utils.config_utils.config import Config


def test_config() -> None:
    config: Config = Config("tests/config.ini")
    config_info: dict[str, str] = config.to_dict()
    print(config_info)
    db_info: dict[str, str] = config.to_dict(section="db")
    print(db_info)
    assert isinstance(config_info, dict)
    assert isinstance(db_info, dict)
