# -*- coding: utf-8 -*-
# @Time : 2022/2/18 11:04
# @Author : Limusen
# @File : 装饰器02


# 修改对象的装饰器
def work(obj):
    obj.name = "python"
    return obj


@work
class Bar:
    def __init__(self):
        pass


print(Bar.name)


# 使用语法糖调用该装饰器
@work  # 等价于 foo = work(foo)
def foo():
    pass


print(foo.name)
