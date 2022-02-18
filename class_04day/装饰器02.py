# -*- coding: utf-8 -*-
# @Time : 2022/2/18 11:04
# @Author : Limusen
# @File : 装饰器02


# 最简单的装饰器
def work(obj):
    return obj


# 使用语法糖调用该装饰器
@work  # 等价于 foo = work(foo)
def foo():
    print("hello world!")


foo()
