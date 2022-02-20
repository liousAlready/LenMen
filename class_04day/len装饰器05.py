#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 12:41
# @Author  : limusem
# @File    : len装饰器05.py
# @Software: PyCharm
# @Description:

# ----------------------------------------
#
# # 打印两个数相加
# def add_num(a, b):
#     print("相加：", a + b)
#
#
# add_num(11, 22)

# ----------------------------------------

# # 新增需求：如何在不改变add_num方法的前提下新增减乘除功能
# def add(func):  # z最外层本质上就是接受一个函数
#     def fun(x, y):
#         print("相乘", x * y)
#         print("相除", x / y)
#         print("相减", x - y)
#         func(x, y)
#
#     return fun
#
#
# # 打印两个数相加
# @add
# def add_num(a, b):
#     print("相加：", a + b)


# add_num(11, 22)


# ----------------------------------------

# 新增需求： 创建一个通用装饰器 有参数跟无参数的函数都可以调用这个装饰器

def add(func):  # z最外层本质上就是接受一个函数
    def fun(*args, **kwargs):
        print("装饰器的功能代码： 登录")
        # 不定长参数
        func(*args, **kwargs)

    return fun


@add
def index():
    print("打开网站首页")


@add
def goods_list(num, iex):
    print("商品列表页面：第{}页，查询{}条".format(num, iex))


index()
print("----------------")
goods_list(5,20)
