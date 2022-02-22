#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 14:01
# @Author  : limusem
# @File    : 鉴权校验.py
# @Software: PyCharm
# @Description:

# 从txt当中读取文件
with open('./user.txt') as f:
    user = eval(f.read())


# print(user)


def check_token(func):
    def token():
        if not user['token']:
            name = input("请输入用户名：")
            pw = input("请输入密码：")
            if user['user_name'] == name and user['password'] == pw:
                user['token'] = True
                func()
            else:
                print("*" * 20)
                print("账号或密码错误，请重新输入")
                print("*" * 20)
        else:
            func()

    return token


@check_token
def index():
    print("打開網站")


@check_token
def goods_list():
    print("打开商品列表")


@check_token
def buys():
    print("打开购物车")


if __name__ == '__main__':
    index()
    goods_list()
    buys()
