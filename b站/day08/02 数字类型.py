# -*- coding: utf-8 -*-
# @Time : 2022/3/7 17:16
# @Author : Limusen
# @File : 02 数字类型


# 一: int类型

# 1.作用:
# 2.定义：
age = 10
ages = int(10)

# # 名字(参数)
# print("hello", "world")

# # 2.类型转换
# # 2.1 纯数字的字符串转成int
# res=int('1000111') # 纯数字的字符串转成int
# print(res,type(res))


# # 2.2 了解
#
# # 10 -> 二进制 除2取余
# print(bin(11))  # 0b1011 0b开头代表二进制
#
# # 10进制 --> 八进制
# print(oct(11)) #　0o13　　0o开头代表八进制
#
# # 10禁止 --》十六禁止
# print(hex(11))
#
# # 2.2.2 其他进制转成十进制
# # 二进制--》10禁止
# print(int("0b1011",2))
#
# # 二进制--》16禁止
# print(int("0xb",16))

# 3.使用


# 二、float类型
# 1.作用
# 2.定义
salary = 3.1  # salary = float(3.1)

# 3.类型转换
res = float("3.1")
print(res, type(res))

# 4. 使用

# int 与float没有需要掌握的内置方法
# 他们的使用就是数学运算+比较运算
