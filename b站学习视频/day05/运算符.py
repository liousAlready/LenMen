# -*- coding: utf-8 -*-
# @Time : 2022/3/1 20:11
# @Author : Limusen
# @File : 运算符

## 1.算数运算符

# print(10 + 3.1)
# print(10 /3 ) # 结果带小数
# print(10 // 3)  # 结果带小数 只保留证书部分
# print(10 % 3 ) # 取模/取余数
# print(10 % 3 ) # 取模/取余数

## 2.比较运算符: >/>=/</<=/==/!=

# print(10>3)
# print(10 == 10)
# print(10>=10)
# print(10<=10)
# name = input('your name :')
# print(name == "es")

## 3.赋值运算符
# 3.1 =:变量的赋值
# name = "li"
# print(name)

# # 3.2 增量赋值：
# age = 19
# # 可以看作 age = age+1
# age += 1
# print(age)

## 3.3 链式赋值

# x = 10
# y = x
# z =y
z = y = x = 10  # 链式赋值
print(x, y, z)
print(id(x), id(y), id(z))

## 3.4 交叉赋值

# m = 10
# n = 20  # 交换两个的值
# # # 加一个临时变量
# # temp = m
# # m = n
# # n = temp
#
# # 交叉赋值
# m, n = n, m  # 把n给了m ,把m给了n
# print(m, n)

## 4.解压赋值

salaries = [111, 222, 333, 444, 555]
# # 取出五个月的工资
# mon0 = salaries[0]
# mon1 = salaries[1]
# mon2 = salaries[2]
# mon3 = salaries[3]
# mon4 = salaries[4]

# # 解压赋值
# # 对应的变量名多一个不行 少一个也不行
# mon0,mon1,mon2,mon3,mon4 = salaries
# print(mon0)
# print(mon1)
# print(mon2)
# print(mon3)
# print(mon4)


# 只想取三个值或者只想取后两个值
x, y,z, *_ = salaries = [111, 222, 333, 444, 555]
print(x,y,z)