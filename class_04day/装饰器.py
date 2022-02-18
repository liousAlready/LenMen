# -*- coding: utf-8 -*-
# @Time : 2022/2/17 19:21
# @Author : Limusen
# @File : 装饰器

# # 　开放封闭原则
#
# def index():
#     print("这个是网站的首页")
#
# index()


# 需要添加新功能  打开网站之前要先登录
# 输入账号，密码，检查账号密码是否正确，正确才能访问

username = 'admin'
password = 'ceshi'


# 登录功能
def login(func):
    def fun():
        user = input("请输入账号:")
        pw = input("请输入密码:")
        if user == username and pw == password:
            func()
        else:
            print("账号或者密码错误")

    return fun


@login # @login: 语法糖 --> index = login(index)
def index():
    print("这个是网站的首页")


index()
