# coding: utf-8

from __future__ import annotations

from typing import Optional, Any
from configparser import RawConfigParser


class Config:
    """配置文件解析"""

    __slots__ = ('_cnf',)

    def __init__(self, file_path: str, encoding: str = 'utf-8') -> None:
        self._cnf = RawConfigParser()
        self._cnf.read(file_path, encoding=encoding)

    def to_dict(self, section: Optional[str] = None) -> dict[str, Any]:
        """转字典"""
        if section is None:
            return {section: dict(self._cnf.items(section)) for section in self._cnf.sections()}
        else:
            return dict(self._cnf.items(section))
