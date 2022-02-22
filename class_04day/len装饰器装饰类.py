#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 13:17
# @Author  : limusem
# @File    : len装饰器装饰类.py
# @Software: PyCharm
# @Description:


# 装饰器装饰类
def add(func):  # z最外层本质上就是接受一个函数
    def fun(*args, **kwargs):
        print("装饰器的功能代码： 登录")
        # 装饰类的时候一定要讲函数return
        return func(*args, **kwargs)

    return fun


# 用装饰器装饰类的时候需要注意
# 返回值需要返回出来


@add  # Myclass = add(Myclass)
class Myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def age(self):
        print(self.age)


m = Myclass("木", "18")
print("m的值：", m)  # 这里实际返回的是调用的myclass对象
print("打印myclass的类属性:", m.age)
