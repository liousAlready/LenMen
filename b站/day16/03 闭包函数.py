# -*- coding: utf-8 -*-
# @Time : 2022/3/18 17:46
# @Author : Limusen
# @File : 03 闭包函数


# 一：大前提
# 闭包函数=名称空间与作用域+函数嵌套+函数对象
#   核心点:名字查找是以函数定义阶段为准


# 　二：什么是闭包函数
# '闭'函数指的是该函数是内嵌函数
# '包'函数指的是该函数包含对外层函数(不是对全局作用域)作用域名字的引用
def f1():
    x = 333333

    def f2():
        print(x)

    f2()

x=1111
def foo():
    x = 222
    f1()

foo()
