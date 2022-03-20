# encoding: utf-8
# Author    : limusen
# Datetime  : 2022/3/20 12:15 下午
# File      : 01 集合.py
# explain   : 文件说明


"""

集合主要用于：去重、关系运算

"""

# 1.作用

# 1.1 关系运算
# friends1 = ['zeer', 'sda', 'sdaq', 'zxc', 'egon']
# friends2 = ['zeer', 'sda', 'sdaq', 'zxc', 'eessx']

# l=[]
# for x in friends1: # 找到二者共同好友
#     if x in friends2:
#         l.append(x)
# print(l)

# 1.2 去重

# 2.定义
#      在{}内用逗号分割开多个元素，多元素需要满足于以下三个条件
#       1.集合内元素必须为不可变类型
#       2.集合内元素无序
#       3.集合内元素没有重复

# s = {1,2} # s = set({1,2})

# s = {1,[1,2]} # 集合内必须为不可变类型
# s= {1,'a','z','5',15,2} # 集合内元素无序
# s = {1, 1, 1, 1, 1, 2, 5}  # 集合内元素没有重复
# print(s)

# 了解

# # s = {} # 默认是空字典
#
# # 定义空集合
# s = set()
# print(s, type(s))

# 3.类型转换

# set({1,2,3})

# s = set("hellolllll")  # 无序的
# print(s)

# s = set([1,1,1,1,2,3])
# s = set[1,1,1,4,5,[1,2]] # 会报错
# print(s)


# 4.内置方法
friends1 = {'zeer', 'sda', 'sdaq', 'zxc', 'egon'}
friends2 = {'zeer', 'sda', 'eessx'}

# # 4.1 取交集， 去两个共同的好友
# res = friends1 & friends2  # 取交集
# print(res)
# print(friends1.intersection(friends2))  # 交集

# # 4.2 取并集，两者所有的朋友
# res = friends1 | friends2 # 取并集
# print(res)
# print(friends1.union(friends2))  # 合集

# # 4.3 取差集 ，firends1独有的好友
# res = friends1 - friends2
# print(res)
# print(friends1.difference(friends2))  # 差集

#
# # 4.4 取差集 ，firends2独有的好友
#
# res = friends2 - friends1
# print(res)
# print(friends2.difference(friends1))  # 差集

#
# # 4.5 对称差集：求两个用户独有的好友
#
# print(friends1 ^ friends2)
# print(friends1.symmetric_difference(friends2))

# # 4.6 父子集，包含的关系
# s1 = {1, 2, 3}
# s2 = {1, 2}
# print(s1 > s2)  # 当s1大于或等于s2时，才能说s1是s2的爹
# print(s1.issuperset(s2)) # 父级判断
# print(s2.issubset(s2)) # 子级判断

# # s3={1,2,3}
# # s4={1,2,4}
# # # 下面不存在包含关系，所以是false
# # print(s3>s4)
#
# s5 = {1, 2, 3}
# s6 = {1, 2, 3}
# print(s5 == s6)  # 可以说s5跟s6互为父子集
# print(s5.issuperset(s6))
# print(s6.issuperset(s5))

# ================关系运算================


# ================去重================

# 1.只能针对不可变类型去重
# print(set([1,1,1,1,2]))

# # 2.无法保证原来的顺序
# l = [1,'a','b','z',1,1,2]
# l = list(set(l))
# print(l)

# l = [
#     {'name': 'lili', 'age': 18, 'sex': 'male'},
#     {'name': 'jack', 'age': 73, 'sex': 'male'},
#     {'name': 'tom', 'age': 20, 'sex': 'female'},
#     {'name': 'lili', 'age': 18, 'sex': 'male'},
#     {'name': 'lili', 'age': 18, 'sex': 'male'},
# ]
#
#
# new_l =[]
# for dic in l:
#     if dic not in new_l:
#         new_l.append(dic)
#
# print(new_l)

# 其他操作
"""

# 1.长度
>>> s={'a','b','c'}
>>> len(s)
3

# 2.成员运算
>>> 'c' in s
True

# 3.循环
>>> for item in s:
...     print(item)
... 
c
a
b


"""

# 需要掌握的
# ============

# 方法一： discard
# s = {1, 2, 3}
# s.discard(3)  # 如果这个元素不存在，do nothing
# print(s)

# 方法二： update
# s.update({1,3,6}) # 更新并去重
# print(s)

# 方法三：pop
# res = s.pop()
# print(res)

# 方法四：add
# s.add(12)
# print(s)


# ============

# 了解


# s.remove(4) # 删除元素不存在则报错


# s = s.difference({3, 4, 5}) # 差集
# s.difference_update({3, 4, 5})
# print(s)


# res = s.isdisjoint({4, 5, 6})  # 两个集合没有交集则返回true
# print(res)
