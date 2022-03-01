# -*- coding: utf-8 -*-
# @Time : 2022/3/1 19:33
# @Author : Limusen
# @File : 02 与用户交互


# 1.接收用户的输入
# 在Python3: input会将用户输入的所有内容都存成字符串类型
# username = input("请输入您的账号: ")  # "egon"
# print(username, type(username))

# 2.格式化输出

# # %号
# # 值按照位置与%s 一一对应,少一个不行,多一个不行
# res = "my name is %s ,my age is %s" % ("egon", "18")
# res1 = "my name is %s ,my age is %s" % ("18", "en")
# print(res)
# print(res1)

# res = "我的名字是 %(name)s 我的年龄是 %(age)s" %{"age":"18","name":"sss"}
# print(res)

# # %s 可以接受任意类型
# print("my age is %s" % 18)
# print("my age is %s" % [1,23])
# print("my age is %s" % {"aeg":"333"})
#
# # %d 只能接收int
# print("my age is %d" % 15)


# # 2.2 str.format: 兼容性好

# 按照key value传值
# res = '我的名字是{}, 我的年龄是{}'.format("sx","18")
# print(res)

# 按照位置取值
# res1 = '我的名字是{0}{0}{0}, 我的年龄是{1}{1}'.format("sx","18")
# print(res1)

# res2 = '我的名字是{name}, 我的年龄是{age}'.format(age="sx", name="18")
# print(res2)

# 2.3 f python3.5之后才推出
x = input("your name:")
y = input("your age:")
res = f'我的名字是{x},我的年龄是{y}'
print(res)
