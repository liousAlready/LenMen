# -*- coding: utf-8 -*-
# @Time : 2022/2/25 11:54
# @Author : Limusen
# @File : demo001


def frange(start, stop, iner):
    x = start
    while x < stop:
        yield x
        x += iner


l = list(frange(0, 4, 0.5))
print(min(l), max(l))
