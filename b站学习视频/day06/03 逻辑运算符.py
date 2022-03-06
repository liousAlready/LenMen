# encoding: utf-8
# Author    : limusen
# Datetime  : 2022/3/5 9:56 下午
# File      : 03 逻辑运算符.py
# explain   : 文件说明

# 一、基本使用

# # not ： 把紧跟其后的条件结果取反
# # ps： not与紧跟其后的那个条件是一个不可分割的整体
# print(not 16 > 13)
# print(not True)
# print(not False)

# # and: 逻辑与 什么跟什么都满足，用来连接左右条件，两个条件同时为true，才为真
# print(True and 10 > 3)
# print(True and 10 > 3 and 10 and 0)  # 条件全为真，最终结果才为True

print(0 and 10 > 3 and 0 and 1 > 3 and 4 == 4 and 3 != 3)  # 偷懒原则
print(1 > 0 and 10 > 3 or 0 and 1 > 3 and 4 == 4 and 3 != 3)  # 偷懒原则

# # or 逻辑或 用来连接左右条件的，只要其中一个条件满足为真，最终结果就为真
# # 两个条件都为false的情况下，最终结果就是假
# print(3 > 2 or 0)
#
# print(10 or 3 != 2 or 3 > 2 or True) # 偷懒原则


# 二、not 、and 、or 优先级
# ps：如果单独就只是一串and连接，或者只是一串or连接，会按照从左到右的顺序依次运算即可（偷懒原则
# 如果是混用则需要考虑优先级 优先级是先not 再按照 and  再按照 or

res = 3 > 4 and not 4 > 3 or 1 == 3 and "x" == "x" or 3 > 3
print(res)
# 分清楚运算方式
res = (3 > 4 and (not 4 > 3)) or (1 == 3 and "x" == "x") or 3 > 3
print(res)
