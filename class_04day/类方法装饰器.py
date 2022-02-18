# -*- coding: utf-8 -*-
# @Time : 2022/2/18 13:30
# @Author : Limusen
# @File : 类方法装饰器


def outer(obj):
    def inner(self):
        print("hello inner")
        obj(self)

    return inner


class Zoo:
    def __init__(self):
        pass

    @outer  # ==> zoo = outer(zoo)
    def zoo(self):
        print("hello zoo")


zoo = Zoo()
print(zoo.zoo.__name__)
zoo.zoo()
