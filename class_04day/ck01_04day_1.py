# -*- coding: utf-8 -*-
# @Time : 2022/2/17 16:44
# @Author : Limusen
# @File : ck01_04day_1


# 闭包

a = 100  # 全局变量


# 闭包条件:
# 条件一: 函数中嵌套函数
# 条件二: 外层函数返回内层嵌套函数名
# 条件三: 内层嵌套函数有引用外层的一个非全局变量

# 闭包不带参数
def func(num):
    # num = 100 # 非全局变量
    print("-----func被调用------")

    def count_book():
        print(num)
        print("这个是计算买书方式的函数")

    # 将方法return出去
    return count_book


print(func.__closure__)

res = func(12)
print(res.__closure__)
