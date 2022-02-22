#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 12:02
# @Author  : limusem
# @File    : 装饰器_04.py
# @Software: PyCharm
# @Description:


# 开放封闭原则

def login(func):
    def fun():
        username = "python"
        password = "le"
        user = input("请输入账号：")
        pw = input("请输入密码：")
        if username == user and password == pw:
            func()
        else:
            print("账号或者密码错误")

    return fun


@login
def index():
    print("这个是网站首页")

#
# index = login(index)
#
# index()

# # index --> fun
# print(index)
#
# # 传入的index  在closure属性单重
# print(index.__closure__)
