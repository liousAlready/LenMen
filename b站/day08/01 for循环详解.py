# -*- coding: utf-8 -*-
# @Time : 2022/3/7 16:31
# @Author : Limusen
# @File : 01 for循环详解


"""

1. 什么是for循环
    循环就是重复做某件事,for循环是python提供第二种循环机制


2. 为何要有for循环

    理论上for循环能做的事情,while循环都可以做
    之所以要有for循环,是因为for循环在循环取值(遍历取值)比while循环更简洁

3. 如何使用for循环

语法:
for 变量名 in 可迭代对象: # 可迭代对象可以是:列表/字典/字符串/元祖/day10
    代码1
    代码2
    代码3
    ...

"""

# # 案例1:循环取值
# l = ['alex_dsb', 'lss_dsb', 'egon_nb']
# # 简单版
# for x in l:  # x = alex_dsb
#
#     print(x)

# # 复杂版:
# l = ['alex_dsb', 'lss_dsb', 'egon_nb']
# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1

# # 案例2:字典循环取值
# # 简单版
# dic = {"k1":111,"k2":222,"k3":333}
# for x in dic:
#     print(x,dic[x])

# # 案例三:字符串 循环取值
# # 简单
# msg = "you can you up"
# for x in msg:
#     print(x)

# 二、总结for循环与while循环的异同


# 1.相同指出：都是循环，for循环可以干的事情，while循环也可以干
# 2.不同条件：
# while循环称之为条件循环，循环次数取决于条件何时变为假
# for 循环称之为"取值循环"，循环次数屈居in后包含的值的个数

# for x in [1,2,3]:
#     print("===>")
#     print("++++")
#     print("===<")

# # 三：for循环控制循环次数: range()
# # 有局限性
# username = "li"
# password = "123"
# for x in range(3):
#     input_name = input("输入账号：")
#     password_name = input("输入密码：")
#
#     if input_name == username and password_name == password:
#         print("登录成功")
#         break
# else:
#     print("输错账号密码次数过多")

# # 四: for + continue
# for i in range(6):
#     if i == 4:
#         continue
#     print(i)

# # 五: for 循环嵌套:
# 外层循环一次,内层循环需要完整循环完毕
#
# for i in range(3):
#     print("外层循环==> {}".format(i))
#     for j in range(5):
#         print("内层循环==> {}".format(j))



