#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 10:05
# @Author  : limusem
# @File    : 05 流程控制if判断.py
# @Software: PyCharm
# @Description:


"""

语法1：

if 条件：
    代码1
    代码2
    代码3

"""
## 如果值大于判断条件则不会输出语句
# age = 18
# is_beautiful = True
# star = "摩羯座"
#
# if age > 16 and age < 20 and is_beautiful and star == "摩羯座":
#     print("我喜欢你")
#
# print("其他代码。。。。")


"""

语法2：

if 条件：
    代码1
    代码2
    代码3
else：
    代码

"""
#
# age = 99
# is_beautiful = True
# star = "摩羯座"
#
# if age > 16 and age < 20 and is_beautiful and star == "摩羯座":
#     print("我喜欢你")
# else:
#     print("不好意思，我们不合适")
#
# print("其他代码。。。。")


"""

语法3：

if 条件1：
    代码1
    代码2
    代码3
elif 条件2：
    代码1
    代码2
    代码3
elif 条件3：
    代码1
    代码2
    代码3

"""
# score = input("请输入您的成绩: ")
# score = int(score)
# if score >= 90:
#     print("优秀")
# elif score >= 80:
#     print("优良")
# elif score >= 70:
#     print("普通")


"""

语法4：

if 条件1：
    代码1
    代码2
    代码3
elif 条件2：
    代码1
    代码2
    代码3
elif 条件3：
    代码1
    代码2
    代码3
else：
    代码块

"""

# score = input("请输入您的成绩: ")
# score = int(score)
# if score >= 90:
#     print("优秀")
# elif score >= 80:
#     print("优良")
# elif score >= 70:
#     print("普通")
# else:
#     print("你就是个垃圾")
#
# print("========")

"""
if 嵌套if
"""

age = 17
is_beautiful = True
star = "摩羯座"

if 16 < age < 20 and is_beautiful and star == "摩羯座":
    print("开始表白")
    is_success = True
    if is_success:
        print("两个人开始了没羞没早的生活")
else:
    print("不好意思，我们不合适")

print("其他代码。。。。")