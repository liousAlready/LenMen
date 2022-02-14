#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/14 20:21
# @Author  : limusem
# @File    : ck01_03day_2.py
# @Software: PyCharm
# @Description:


# def func():
#     print("999")
#     func()
#
# func()

a = 100


def fun(n):
    if n == 1:  # 递归临界点：不再调用自身函数的条件
        return 1
    else:
        return n * fun(n - 1)


# 不管在什么时候调用 传入的参数相同  返回的结果就一定是一样的

print(fun(4))
