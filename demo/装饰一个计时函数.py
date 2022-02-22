#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 13:47
# @Author  : limusem
# @File    : 装饰一个计时函数.py
# @Software: PyCharm
# @Description:


import time


def wa(func):
    def time_out(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        fun_time = time.time() - start_time
        print("函数调用总耗时为：{:.5f}".format(fun_time))

    return time_out


@wa
def login():
    time.sleep(2)
    print("当前正在进行登录操作")


login()
