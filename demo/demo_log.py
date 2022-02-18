# -*- coding: utf-8 -*-
# @Time : 2022/2/18 16:14
# @Author : Limusen
# @File : demo_log


import logging
import time
import datetime


def log(func):
    """
    日志装饰器
    :param func:
    :return:
    """

    def inner(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        res = func(*args, **kwargs)
        print(f"[{timestamp} ({func.__name__}) {args} -> {res}]")
        return res

    return inner


@log
def pluser(a, b):
    return a + b


pluser(1, 3)