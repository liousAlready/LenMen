# -*- coding: utf-8 -*-
# @Time : 2022/2/15 9:05
# @Author : Limusen
# @File : ckhomework01

# 实现斐波那契数列


def fun(i):
    if (i == 0 or i == 1):
        return 1
    else:
        return fun(i - 1) + fun(i - 2)


print([fun(x) for x in range(10)])
