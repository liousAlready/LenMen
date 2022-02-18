# -*- coding: utf-8 -*-
# @Time : 2022/2/18 13:48
# @Author : Limusen
# @File : 类装饰器


def outer(cls):  # 类装饰器
    class Inner(object):
        def __init__(self):
            self.cls = cls()

        def __getattr__(self, attr):
            return getattr(self.cls, attr)

    return Inner


@outer
class Zoo:

    def __init__(self):
        pass

    def say(self):
        print("hello world!")

zoo = Zoo()
print(zoo.__class__)
zoo.say()
