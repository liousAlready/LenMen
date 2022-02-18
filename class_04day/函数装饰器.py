# -*- coding: utf-8 -*-
# @Time : 2022/2/18 11:47
# @Author : Limusen
# @File : 函数装饰器


def outer(func):  # 函数装饰器
    def inner():
        func()

    return inner


@outer
def foo():
    print("hello foo!")


# 区分是被调用运行还是自己本身运行
# 被调用则是显示的函数名
print(foo.__name__)
foo()
