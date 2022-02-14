#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/14 20:04
# @Author  : limusem
# @File    : ck01_01day_1.py
# @Software: PyCharm
# @Description:


# 生成器的三个方法 send close throw


def gen():
    for i in range(5):
        j = yield  i
        print(j)

# send 与生成器进行交互
g = gen()


print(next(g))
print(next(g))
