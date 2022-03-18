# encoding: utf-8
# Author    : limusen
# Datetime  : 2022/3/16 8:49 上午
# File      : 03 函数基本使用.py
# explain   : 文件说明


# 1.先定义函数
# 定义的语法


"""

def 函数名(参数1，参数2...):
    '''文档描述'''
    函数体
    return 值

"""


# # 形式一： 无参函数
# def func():
#     print("hhahah")
#
#
# func()
#
# # 定义函数发生的事情
# # 1.申请内存空间保存函数体代码
# # 2.将上述内存地址绑定函数名
# # 3.定义函数不会执行函数体代码，但是会监测函数体语法
#
# # 调用函数发生的事情
#
# # 1.通过函数名找到函数的内存地址
# # 2.然后加括号就是在触发函数代码的执行
# print(func)
# func()

# # 示范1
# x = 111
#
# def bar(): # bar = 函数的内存地址
#     print("from bar")
#
# def foo():
#     # print(x)
#     bar()
#     print("from foo")
#
#
# foo()

# # 示范2
# # 先定义后使用
#
# def foo():
#     # print(x)
#     bar()
#     print("from foo")
#
#
# def bar():  # bar = 函数的内存地址
#     print("from bar")
#
#
# foo()


# # 示范3
# # 先定义后使用
#
# def foo():
#     # print(x)
#     bar()
#     print("from foo")
#
#
# foo()
#
# def bar():  # bar = 函数的内存地址
#     print("from bar")

# # 形式二：有参函数
#
# def func(x, y):
#     print(x, y)
#
#
# func(1, 2)

# # 形式三： 空函数 ， 函数体代码为pass
#
# def func(x, y):
#     pass


# 三种定义方式各用在何处
# # 1.无参函数的应用场景
# def intercotr():
#     name = input("username>>>:")
#     age = input("age>>>:")
#     msg = '名字：{} 年龄：{}'.format(name,age)
#     print(msg)
#
# intercotr()

# # 2.有参函数的应用场景
# def func(x, y):
#     res = x + y
#     return res
# print(func(3,4))


# 3.空函数的应用场景

def user_name():
    """用户名输入"""
    pass


def upload_file():
    """上传文件"""
    pass


# 二、调用函数
# 1.语句的形式 : 只调用函数，只加括号调用函数
# func()
# add(1,2)

# # 2.表达式形式：
# def add(x, y):
#     return x + y
#
#
# # 赋值表达式
# res = add(1, 2)
# print(res)
# # 数学表达式
# res = add(1, 2) * 10
# print(res)
#
# # 3.函数调用可以当做参数
# res = add(add(1, 2), 10)
# print(res)


# 三、函数返回值

# return 是函数结束的标志，即函数体代码一旦运行到return
# 会立刻终止函数的运行，并且会将return后的值当做本次运行的结果返回

# 1.返回None： 函数体内没有return或者return none
# 2.返回一个值： return 值
def func():
    return 10


res = func()
print(res)


# 3.返回多个值： return 值，值，值
def func():
    return 10, 'aa', [1, 2]


res = func()
print(res, type(res))
