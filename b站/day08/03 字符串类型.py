# -*- coding: utf-8 -*-
# @Time : 2022/3/7 19:32
# @Author : Limusen
# @File : 03 字符串类型


# # 1.作用
# # 2.定义
#
# msg = "hello"  # msg =
# print(type(msg))
#
# # 3.类型转换
# # str可以把任意其他类型都转成字符串
# res = str({"a":1})
# print(res,type(res))

# 4.使用：内置方法
# 4.1优先掌握
# 4.1.1 按索引取值(正向/反向取):只能取

# msg = "hello world"
# # 正向取
# print(msg[0])
# print(msg[5])
# # 反向取
# print(msg[-1])

# # 4.1.2 切片(顾头不顾尾,步长) 索引的拓展应用
# res = msg[0:5]
# print(res)  # 顾头不顾尾
# print(msg)
#
# # 步长
# res = msg[0:5:2] # 0 2 4
# print(res) # hlo

# 反向步长
# res = msg[5:0:-1]
# print(res)  # " olle"

# # [:] 取所有
# res = msg[:]
# print(res)
#
# # 把字符串倒过来
# res = msg[::-1]
# print(res)


# # 4.1.3 长度len
# print(len(msg))

# # 4.1.4 成员运算in 和 not in
# # 判断一个子字符串是否存在于一个大字符串中
# print("alex" in 'alex is sb' )
# print( "alex" not in 'alex is sb' )

# # 4.1.5 移除字符串左右两侧的符号strip
#
# msg1 = "           egon      "
# print(msg1.strip())  # 默认去除的是空格 不会改变原值

# # 去掉*
# msg="*********egno1*************"
# print(msg.strip("*"))

# # 了解:strip 只取两边 不去中间
# msg="**********e*****gon********"
# print(msg.strip("*"))
#
# msg="**/*-***egon**-02()"
# print(msg.strip("*/=()-02"))

# # 应用 去除用户名跟密码的空格
# inp_user = input("you name>>>: ").strip()
# inp_pwd = input("you password>>>: ").strip()
# if inp_user == "egon" and inp_pwd == "123":
#     print("登录成功")
# else:
#     print("密码错误")

# 4.1.6 切分split : 把一个字符串按照某种分隔符进行切分,得到一个列表
# 　默认分割
# info = "egon 18 male"
# res = info.split()  # 默认分隔符是空格
# print(res)

# # 指定参数分割
# info = "egon:18:male"
# res = info.split(":")  # 默认分隔符是空格
# print(res)
#
# # 指定分割次数(了解)
# info = "egon:18:male"
# res = info.split(":", 1)  # 默认分隔符是空格
# print(res)
#
# # 4.1.7 循环
# info = "egon:18:male"
# for x in info:
#     print(x)

# 4.2 需要掌握

# # 4.2.1 strip,lstrip,rstrip  ： 将字符串切成列表
#
# msg = "****egon****"
# # print(msg.strip("*"))
# # print(msg.lstrip("*"))
# # print(msg.rstrip("*"))
#
# # 4.2.2 lower,upper
# msg1 = "AbCCCC"
# print(msg1.lower())  # 全部小写  产生新的字符串
# print(msg1)
# print(msg1.upper())  # 全部大写
#
# # 4.2.3 startswith,endswith
# msg2 = "alex is sb"
#
# print(msg2.startswith("alex"))
# print(msg2.endswith("sb"))

# 4.2.4  format

# 4.2.5 split，rsplit
import random
import os

# info = "egon:18:male"
# print(info.split(":", 1))  # ["egon","18:male"]
# print(info.rsplit(":", 1))  # ["egon:18","male"]

# 4.2.6 join 把列表拼接成字符串

# info = ['egon', '18', 'male']
# res = ":".join(info)  # 相当于for循环 按照某个分隔符号，把元素全为字符串的列表拼接成一个字符串
# print(res)


# # 生成手机号
# phone = ['138', '137', '136', '155']
# res = random.choice(phone)
# number = random.randrange(1, 123456789)
# phone_number = os.path.join(res + str(number))
# print(phone_number)

# # 4.2.7 replace
# msg = "you can you up no can no bb"
# print(msg.replace("can","CAN"))
# print(msg.replace("can","CAN",1)) # 只改第一个


# # 4.2.8 isdigit
# # 判断字符串是否有数字组成
# print('123'.isdigit())
# print("1.23".isdigit())
#
# age = input("请输入你的年龄：").strip()
# if age.isdigit():
#     age = int(age)  # int("abdba")
#     if age > 18:
#         print("猜大了")
#     elif age < 18:
#         print("猜小了")
#     else:
#         print("最小")
# else:
#     print("请输入数字！")

# 4.3 需要了解

# 4.3.1 find，rfind，index，rindex，count
# msg = "hello egon hahaha"
# print(msg.find("e"))  # 返回要查找的字符串在源字符串中的起始索引
# print(msg.find("egon"))
# print(msg.index("e"))
# print(msg.index("egon"))

# msg = "hello egon hahaha egon ，egon"
# print(msg.count("egon"))

# # 4.3.2 center ljust
# print("egon".center(50, "*"))  # 左右边界用标识符隔开
# print("egon".ljust(50, "*"))  # 左边界
# print("egon".rjust(50, "*"))  # 右边界
# print("egon".zfill(50))  # 用0隔开

# # 4.3.3 expandtabs  设置制表符代表的空格数
# msg = "hello\tworld"
# print(msg.expandtabs(10))

# # 4.3.4 captalize、swapacse，title
# print("hello world egon".capitalize()) # 字符串首字母大写
# print("Hello World EGON".swapcase())

# print("hello world egon".title()) # 每个单词的首字母大写

# # 4.3.5 is数字系列
# # 4.3.6 is其他
# print("abc".islower())
# print("ABC".isupper())
# print("Hello World".istitle())
# print("123adb".isalnum())  # 判断是否有字母或数字组成
# print("abc".isalpha()) # 必须有字母组成 结果返回为true
# print("   ".isspace()) # 字符串由空格组成 如果是返回true
# print("print".isidentifier())  # 判断名字是否合法


num1 = b'4'  # bytes
num2 = u'4'  # unicode，python3中无需加u
num3 = "四"  # 中文数字
num4 = "IV"  # 罗马数字

# isdigit 只能识别num1、num2

# print(num1.isdigit()) # True
# print(num2.isdigit()) # True
# print(num3.isdigit()) # False
# print(num4.isdigit()) # False


# isnumeric 可以识别 num2 num3 num4
print(num2.isnumeric())
print(num3.isnumeric())
print(num4.isnumeric())
