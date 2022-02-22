#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 14:27
# @Author  : limusem
# @File    : 多个装饰器装饰一个函数.py
# @Software: PyCharm
# @Description:


import time

# 从txt当中读取文件
with open('./user.txt') as f:
    user = eval(f.read())


# 多个装饰器装饰一个函数


# 计算函数时间装饰器
def wa(func):
    def time_out(*args, **kwargs):
        print("计算时间装饰器正在调用......")
        start_time = time.time()
        func(*args, **kwargs)
        fun_time = time.time() - start_time
        print("函数调用总耗时为：{:.5f}".format(fun_time))

    return time_out


# 校验登录装饰器
def check_token(func):
    def token(*args, **kwargs):
        print("登录校验装饰器正在被调用......")
        print("------登录页面------")
        if not user['token']:
            name = input("请输入用户名：")
            pw = input("请输入密码：")
            if user['user_name'] == name and user['password'] == pw:
                user['token'] = True
                func(*args, **kwargs)
            else:
                print("*" * 20)
                print("账号或密码错误，请重新输入")
                print("*" * 20)
        else:
            func(*args, **kwargs)

    return token


# 装饰器是从下往上开始装饰
# 装饰器是从上往下开始执行
@check_token  # time_out ==> func = check_token(func) ==> func ==> token
@wa  # func = wa(func)  func ==> time_out 执行完成之后将函数传入下一个装饰器
def func():
    time.sleep(2)
    print("这是需要被装饰的函数")


# func()


class MyTest(object):

    @classmethod  # 被classmethod装饰之后，该方法就是一个类方法
    def add(cls):  # cls 代表的是类本身 类方法是有参数的
        print("add")
        print(cls)

    @staticmethod  # 静态方法  实例和类都可以调用静态方法
    def static():  # 静态方法默认是没有参数的
        print("这个是静态方法")

    @property  # 设定只读属性
    def read_attr(self):
        print("这个装饰器装饰完，该方法可以像属性一样被调用")
        return "18岁 "

    def sub(self):  # self 代表的是实例本身
        print("sub中的self：", self)


my = MyTest()
# my.add()  # 打印出来的是类
# my.sub()  # 实例对象
# MyTest.static()
my.read_attr
