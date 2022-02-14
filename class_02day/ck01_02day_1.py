# encoding: utf-8
# Author    : limusen
# Datetime  : 2022/1/15 2:51 下午
# Project   : LenMen
# File      : ck01_02day_1.py
# explain   : 文件说明


import timeit

# def func():
#     for i in range(10):
#         print(i)
#
#
# # res = timeit.Timer(func).timeit(100)
# # print(res)
#
# res2 = timeit.timeit('[1,2,3]')
# print(res2)
#
# # res3 = timeit.timeit(func)
# # print(res3)
#
# # 命名元祖
#
# # 可以像字典一样取值
# from collections import namedtuple
#
# tu = ("musen", 18, 'name')
#
# s = namedtuple("infotuple", ['name', 'age', 'gender'])
# # 创建命名元祖
# tuples = s(1, 2, 3)
# print(tuples)
# # 定义
# tuples2 = s("musen", 18, 'name')
# print(tuples2)
#
# # 取键值 注意是要定义好的变量去取值
# print(tuples2.name)
#
# print(type(tuples2))
# print(type(s))

# 字典和集合

list_1 = [1, 1, 1, 2, 2, 3, 3, 4]

se = set()  # 空集合
set1 = {1, 1, 1, 2, 2, 3, 3, 4}  # 有数据的集合，只有值没有键 不会存在重复元素
print(set1)
# 取出重复元素
li2 = list(set(list_1))
print(li2)

# 向集合添加数据 集合是无序的
# 集合是可变的
se.add("sss")
se.add("bbb")
print(se)

# 删除集合中的数据
se.remove("sss")
print(se)

# 更新元素
se.update("111", "222", "333")  # 等同于列表的extend
print(se)
# 情况
se.clear()
print(se)
# 复制
se.copy()

dic = {}  # 空字典

# 可变和不可变 ： 可变元素不可hash  不可变元素可hash

set3 = {1, 2, 3}
