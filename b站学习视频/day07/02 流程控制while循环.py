# encoding: utf-8
# Author    : limusen
# Datetime  : 2022/3/6 4:10 下午
# File      : 02 流程控制while循环.py
# explain   : 文件说明


# 1.循环的语法与基本使用

"""
条件一直成立，那么就会一直循环
直到条件不满足 则退出循环
print(1)
while 条件：
      代码1
      代码2
      代码3
print(3)
"""
#
# count = 0
# while count < 5:
#     print(count)
#     count += 1
#
# print("====顶级代码====")

# # 2.死循环与效率问题
# # 如果说条件为真，没有结束的条件，那么就会造成死循环
# count = 0
# while count  < 5:
#     print(count)

# while True:
#     name = input("you name >>>>")
#     print(name)

# # 效率问题
# while True:
#     1+1

# 3.循环的应用

# 两个问题
# 1.重复运行代码
# 2.输对了还需要输入

# username = "egon"
# password = "123"
# name = input("请输入你的账号:")
# pwd = input("请输入你的密码:")
#
# if name == username and pwd == password:
#     print("登录成功")
# else:
#     print("账号或密码错误")

# 循环次数

# count = 0
# username = "egon"
# password = "123"
# while count < 3:
#     name = input("请输入你的账号:")
#     pwd = input("请输入你的密码:")
#
#     if name == username and pwd == password:
#         print("登录成功")
#     else:
#         print("账号或密码错误")
#         count += 1

# 4.退出循环的两种方式
# 方式一: 将条件改为false,等到下一次循环判断条件时才会神效

tag = True
username = "egon"
password = "123"
# while tag:
#     name = input("请输入你的账号:")
#     pwd = input("请输入你的密码:")
#     if name == username and pwd == password:
#         print("登录成功")
#         tag = False
#     else:
#         print("账号或密码错误")

# # 方式二：break 只要运行到break就会立刻终止本次循环
# while True:
#     name = input("请输入你的账号:")
#     pwd = input("请输入你的密码:")
#     if name == username and pwd == password:
#         print("登录成功")
#         break  # 立刻终止
#     else:
#         print("账号或密码错误")
#     print("===end===")


# 7.while 循环嵌套
"""
while True:
    while True:
        while True:
            break
        break
    break
    
"""

# while True:
#     name = input("请输入你的账号:")
#     pwd = input("请输入你的密码:")
#     if name == username and pwd == password:
#         print("登录成功")
#         while True:
#             cmd = input("输入命令的编号>: ")
#             print("命令{x}正在运行...".format(x=cmd))
#             if cmd == "q":
#                 print("当前操作已跳过")
#                 break
#         break  # 立刻终止
#     else:
#         print("账号或密码错误")
#     print("===end===")

while tag:
    name = input("请输入你的账号:")
    pwd = input("请输入你的密码:")
    if name == username and pwd == password:
        print("登录成功")
        while tag:
            cmd = input("输入命令的编号>: ")
            if cmd == "q":
                tag = False
                print("当前正在结束操作")
            else:
                print("命令{x}正在运行...".format(x=cmd))
    else:
        print("账号或密码错误")

# 8. while + continue 结束本次循环，直接进入下一次
