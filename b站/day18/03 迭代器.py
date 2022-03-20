# encoding: utf-8
# Author    : limusen
# Datetime  : 2022/3/15 9:40 下午
# File      : 03 迭代器.py
# explain   : 文件说明


"""

1.什么是迭代器
迭代器指的是迭代取值的工具，迭代是一个重复的过程，每次重复都是基于上一次的结果而继续的，单纯的重复并不是迭代

2.为何要有迭代器

    迭代器是用来迭代取值的工具，而涉及到把多个值循环取出来的类型哟：
    列表、字符串、元祖、字典、day10、文件

l = ['egon', 'liu', 'aliex']

i = 0
while i < len(l):
    print(l[i])
    i += 1

    上述迭代取值的方式只适用于有索引的数据类型：列表、字符串、字典
    为了解决基于索引迭代器取值的局限性
    python必须提供一种能够不依赖与索引的取值方式，就是迭代器


3.如何使用迭代器


"""

# 可迭代的对象： 但凡有 __iter__ 方法的都称之为可迭代对象
s1 = ''
s1.__iter__()

l = []
l.__iter__()

t = (1,)
t.__iter__()

d = {"a": 1}
d.__iter__()

set1 = {1, 2, 3}
set1.__iter__()

with open("a.txt", mode="w") as f:
    # f.__iter__()
    pass


# # 调用可迭代对象的__iter__方法会将其转换成迭代器对象
# d = {"a": 1, "b": 2, "c": 3}
# res = d.__iter__()
# print(res)
# print(res.__next__())


# while True:
#     try:
#         print(res.__next__())
#     except StopIteration:
#         break
#
# print("=====>>>>")  # 在一个迭代器取值取干净的情况下，再对其取值取不到
# while True:
#     try:
#         print(res.__next__())
#     except StopIteration:
#         break


# 3. 可迭代对象与迭代器对象详解
# 可迭代对象（"可以转换成迭代器的对象"）： 内置有__iter__方法对象
#           可迭代对象.__iter__() 得到迭代器对象

# 可迭代对象：字符串、列表、元祖、字典、day10、文件对象
# 迭代器对象：文件对象

# # 迭代器对象： 内置有__next__方法并且内置有__iter__方法的对象
# #           迭代器对象.__next__() 得到迭代器的下个值
# #           迭代器对象.__iter__() 得到迭代器的本身，说白了调了跟没调一样
# dic = {"a": 1, "b": 2, "c": 3}
# dic_iter = dic.__iter__()
# dic_iter.__iter__()
# print(dic_iter is dic_iter.__iter__())

# 5.for 循环的工作原理 : for循环可以成为迭代器循环

# 1. d.__iter__() 得到一个迭代器对象
# 2. 迭代器对象.__next__() 拿到一个返回值，然后将该返回值复制给k
# 3. 循环往复步骤2，知道抛出StopIteration异常 捕捉异常然后结束循环
dic = {"a": 1, "b": 2, "c": 3}

for k in dic:
    print(k)

# with open('a.txt', 'rt', encoding="utf-8") as f:
#     for line in f: # f.__iter__() 调用的是它本身
#         print(line)


# 6.迭代器优缺点总结

# 优点
# 1.针对有索引跟没有索引的都可以取值
# 2.更节省内存占用

# 缺点
# 1.生命周期
