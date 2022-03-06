# encoding: utf-8
# Author    : limusen
# Datetime  : 2022/3/5 9:23 下午
# File      : 01 可变不可变类型.py
# explain   : 文件说明


# 1、可变不可变类型

# 可变类型： 值改变 id不变 证明改的是原汁机 证明原值是可以被改变的
# 不可变类型：值改变 id也变了，证明是产生新的值，压根没有改变原值，证明原值是不可以被修改的


# # 2、验证
# # 2.1 int是不可变类型
# x = 10
# print(id(x))
# x = 11
# print(id(x))
#
# # 2.2 float是不可类型
# x = 3.1
# print(id(x))
# x = 3.2
# print(id(x))
#
# # 2.3 str
# x="abd"
# print(id(x))
# x = "asd"
# print(id(x))

# # 2.4 列表是可变类型 ， 列表修改值只是修改元素的内存地址
# l = ['aaa', 'bbbb']
# print(id(l))
# l1 = ['xxx', 'yy']
# print(id(l1))

# 小结： int、float、str 都被设计成了不可分割的整体，不能够被改变的

# # 2.5 字典与列表一样
# dic = {'kw': 111, "k2": 222}
# print(id(dic))
# dic['kw'] = 32
# print(id(dic))


# 2.6 bool不可变


# 关于字典的补充
# 定义： {}内用逗号分隔开多个key:value
#       其中value可以是任意类型
#       但是key必须是不可变类型


# dic = {'k1': 111, 'k2': 3.1, 'k3': [333], 'k4': {"name": "sda"}}
