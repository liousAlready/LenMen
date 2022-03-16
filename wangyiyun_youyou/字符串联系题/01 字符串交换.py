# -*- coding: utf-8 -*-
# @Time : 2022/3/15 14:52
# @Author : Limusen
# @File : 字符串交换


"""

已知 a的值为"hello"，b的值为"world"，如何交换a和b的值？
得到a的值为"world"，b的值为"hello

"""

# 方法一  中间变量
a = "hello"
b = "world"

temp = a

a = b
b = temp

print(a, b)

# 方法二 python写法

a = "hello"
b = "world"

a,b = b,a
print(a,b)
