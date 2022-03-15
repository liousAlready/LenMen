# encoding: utf-8
# Author    : limusen
# Datetime  : 2022/3/15 10:26 下午
# File      : 04 生成器.py
# explain   : 文件说明

"""

如何得到自定义的迭代器：
在函数内一旦存在yield关键字，调用函数并不会执行函数体代码
会返回一个生成器对象，生成器即迭代器对象

"""


def func():
    print("第一次")
    yield 1
    print("第二次")
    yield 2
    print("第三次")
    yield 3
    print("第四次")


g = func()


# print(next(g))

# # 生成器就是迭代器
# g.__iter__()
# g.__next__()

# # # next方法会触发函数体代码的运行，遇到yield停下来，将yield后的值
# # # 当做本次调用的结果返回
# res1 = g.__next__()
# print(res1)
#
# res2 = g.__next__()
# print(res2)
#
# res3 = g.__next__()
# print(res3)


# 生成器应用

def my_range(start, stop, step=1):
    print("start...")
    while start < stop:
        yield start
        start += step

    print("end...")


# res = my_range(1, 5, 2)
# print(next(res))
# print(next(res))
# print(next(res))

for n in my_range(1, 7, 2):
    print(n)
