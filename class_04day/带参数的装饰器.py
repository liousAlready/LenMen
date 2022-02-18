# -*- coding: utf-8 -*-
# @Time : 2022/2/18 15:10
# @Author : Limusen
# @File : 带参数的装饰器


def outer(func):
    def inner(*args, **kwargs):
        print("hello inner!")
        return func(*args, **kwargs)

    return inner


@outer
def add(x, y,z):
    return x * y *z


print(add(2, 3,6))
