# coding: utf-8

from __future__ import annotations

from importlib import import_module
import_module("_add_path")

import time
import threading

from singleton_utils.singleton_type import SingletonType


class Test(metaclass=SingletonType):
    """测试类"""

    def __init__(self, x):
        self.x = x
        time.sleep(1)


def task(arg, lst: list[Test]) -> None:
    # cls()时，优先执行cls的元类的 __call__()方法
    t = Test(arg)
    lst.append(t)
    return None


if __name__ == '__main__':
    num: int = 20
    test_list: list[Test] = []
    thread_list: list[threading.Thread] = []
    for i in range(num):
        thread = threading.Thread(target=task, args=(i, test_list))
        thread_list.append(thread)
    # 启动线程
    for thread in thread_list:
        thread.start()
    # 等待线程结束
    for thread in thread_list:
        thread.join()
    # 校验单例
    for j in range(1, len(test_list)):
        # print(test_list[j])
        assert test_list[j] is test_list[0]
        assert test_list[j].x == test_list[0].x
