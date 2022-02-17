# -*- coding: utf-8 -*-
# @Time : 2022/2/17 14:07
# @Author : Limusen
# @File : ck

# #   filter 过滤函数 第一个参数是函数 第二个参数是可迭代对象
# def fun(c):
#     return c < 10
#
#
# li = [1, 2, 3, 5346, 6, 2135, 12, 4124, 523, 56]
# result = filter(fun, li)
# # print(list(result))
#
# # map: 将可迭代对象中的数据迭代出来,每个数据都传到函数中调用,将返回结果放到新的对象当中
#
# res2 = map(fun, li)
# # print(list(res2))
#
# # zip() 输出结果为可迭代对象 减少内存占用
#
# res3 = zip([1, 2, 3], [11, 22, 33])
# # print(list(res3))


# 匿名函数
from functools import partial


def func(a, b):
    c = a + b
    print(c)
    return a + b


# 运算符的优先级


# 匿名函数适用场景: 简单的函数定义(只有一个表达式)

# 调用方法一: (不适用)
res = lambda a, b: a + b
# print(res(11, 22))

# 方法二: (不适用)
res1 = (lambda a, b: a + b)(1, 2)
# print(res1)

f = lambda a: a * 9
# print(f(19))

# fileter跟lambd一起使用
li = [1, 2, 3, 5346, 6, 2135, 12, 4124, 523, 56]
res02 = filter(lambda x: x < 10, li)
# print(list(res02))

# li2 = [(lambda x: x % 5 == 0)(i) for i in range(10)]
# print(li2)


# a = 100
# if a > 100:
#     print("a大于100")
# else:
#     print(222)
#
# # 三目运算符
# print(100) if a > 100 else print(222)

li1 = [1, 2, 3, 11, 22, 33]
li2 = [1, 2, 3, 11, 22, 33]
li3 = [1, 2, 3, 11, 22, 33]
li4 = [1, 2, 3, 11, 22, 33]
li5 = [1, 2, 3, 11, 22, 33]

li = [1, 2, 31, 51, 32, 53, 67, 86, 3, 4, 6, 7, 8]
li02 = [2,3,5,12,4,32]
filter2 = partial(filter, lambda x: x > 5)

res12 = filter2(li)
print(list(res12))

print(list(filter2(li02)))
