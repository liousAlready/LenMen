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

msg = "hello world"
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

# 指定参数分割
info = "egon:18:male"
res = info.split(":")  # 默认分隔符是空格
print(res)

# 指定分割次数(了解)
info = "egon:18:male"
res = info.split(":", 1)  # 默认分隔符是空格
print(res)

# 4.1.7 循环
