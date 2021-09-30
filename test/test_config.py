# coding: utf-8

from __future__ import annotations

from importlib import import_module
import_module("_add_path")

from config_utils.config import Config


if __name__ == '__main__':
    config: Config = Config("config.ini")
    config_info: dict[str, str] = config.to_dict()
    print(config_info)
    db_info: dict[str, str] = config.to_dict(section="db")
    print(db_info)
    assert isinstance(config_info, dict)
    assert isinstance(db_info, dict)
