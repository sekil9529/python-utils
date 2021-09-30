# coding: utf-8

from __future__ import annotations

from importlib import import_module
import_module("_add_path")

from typing import Any
import logging.config

from log_utils.logger_proxy import LoggerProxy

# 定义logger
logger: LoggerProxy = LoggerProxy(__name__)
# logger: logging.Logger = logging.getLogger(__name__)


if __name__ == '__main__':
    # logging配置
    logging_config: dict[str, Any] = {
        'version': 1,
        'loggers': {
            '': {
                'level': 'INFO',
                'handlers': ['console'],
                'propagate': False
            },
        },
        'formatters': {
            'default': {
                'format': '[%(asctime)s.%(msecs).3d] - [%(pathname)s] - [%(levelname)s] - [%(name)s:%(lineno)d] - [%(message)s]',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'default',
            },
        },
    }
    # 应用配置晚于logger定义
    logging.config.dictConfig(logging_config)

    logger.info("log_utils proxy info.")
