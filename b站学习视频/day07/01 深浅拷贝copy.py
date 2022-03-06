# encoding: utf-8
# Author    : limusen
# Datetime  : 2022/3/6 11:25 上午
# File      : 01 深浅拷贝copy.py
# explain   : 文件说明

# list1 = ['egon',
#          'lxx',
#          [1, 2]]

# # 二者分割不开，list改list2页跟着改，因为指向的就是l1的内存地址
# list2 = list1  # 这不叫拷贝
# list1[0] = "EGON"
# print(list2)


print("=============================")

# 需求：
# 1.拷贝一下原列表并产生一个新的列表
# 2.想让两个列表完全独立开，针对的是改操作，而不是读操作

# # # 3.如何copy列表
# # 3.1 如何叫浅拷贝
# # 是把原列表第一层内存地址，不加区分完全copy一份给新列表
#
# list1 = ['egon',
#          'lxx',
#          [1, 2]]
# list3 = list1.copy()
#
# # print(id(list1))
# # print(id(list2))
#
# # print(id(list1[0]), id(list1[1]), id(list1[2]))
# # print(id(list3[0]), id(list3[1]), id(list3[2]))
#
# list1[0] = "EGON"
# list1[1] = "LXX"
# list1[2][0] = 111
# list1[2][1] = 2222
# # list1[2].append("sss")
# # list1.append("sdasd")
#
# print(list1)
# print(list3)
#
# print("=============================")


# # 实验二：对于可变类型，我们可以改变可变类型中包含的值，但是内存地址不变
# # 原列表的索引仍指向原来的内存地址，于是新列表也跟着一起受影响
# # 如下
# list1[2][0] = 111
# list1[2][1] = 222
# print(list1)
# print(list2)

# 深拷贝

import copy

list1 = ['egon',
         'lxx',
         [1, 2]]

list3 = copy.deepcopy(list1)
# print(id(list1))
# print(id(list3))
# print(list3)


# #       不可变类型      不可变类型    可变类型
# print(id(list1[0]), id(list1[1]), id(list1[2]))
# print(id(list3[0]), id(list3[1]), id(list3[2]))

"""
4395210736 4395210992 4396726224
4395210736 4395210992 4396474768
"""

# print(list3)
# print(id(list1[2][0]),id(list1[2][1]))
# print(id(list3[2][0]),id(list3[2][1]))

list1[0] = "EGON"
list1[1] = "LXX"
list1[2][0] = 111
list1[2][1] = 222

print(list1)
print(list3)
