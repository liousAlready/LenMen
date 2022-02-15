# -*- coding: utf-8 -*-
# @Time : 2022/2/15 10:53
# @Author : Limusen
# @File : shengchengqi


def func():
    a = yield 1
    print(a)
    b = yield 2
    print(b)

g = func()
print(g.send(None))   # send  -- 发送
print(g.send("alex"))   # send  -- 发送
# print(g.send("宝元"))   # send  -- 发送
