# -*- coding: utf-8 -*-
# @Time : 2022/3/18 15:54
# @Author : Limusen
# @File : 01 函数对象


# 精髓: 可以把函数当成变量取用
# func = 内存地址

def func():
    print("from func")


# 1.可以赋值
# f = func
# print(f,func)
# f()

# # 2.可以当做函数的参数传入
# def foo(x):
#     # print(x)
#     x()
#
#
# foo(func)  # foo(func)

# # 3.可以将函数当作另一个函数的返回值
# def foo(x):
#     return x
#
#
# res = foo(func)
# print(res)
#
# res()

# 4. 可以当做容器类型的一个元素

# 列表
# l = [func,]
# # print(l)
# l[0]()

# # 字典
# dic = {'k1': func}
# dic["k1"]()


def login():
    print("登录功能")


def transfer():
    print("转账功能")


def queryyue():
    print("查询余额")


func_dic = {
    "1": login,
    "2": transfer,
    "3": queryyue
}

# 调用
# func_dic["1"]()


# while True:
#     print("""
#
#     0 退出
#     1 登录
#     2 转账
#     3 查询余额
#
#     """)
#     choice = input("请输入您需要办理的业务编号: ").strip()
#     if not choice.isdigit():
#         print("必须输入编号,傻逼")
#         continue
#     if choice == "0":
#         break
#
#     if choice in func_dic:
#         func_dic[choice]()
#     else:
#         print("输入指令不存在!")

    # if choice == '1':
    #     login()
    # elif choice == '2':
    #     transfer()
    # elif choice == '3':
    #     queryyue()
    # else:
    #     print("输入指令不存在")
