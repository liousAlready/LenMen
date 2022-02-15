# -*- coding: utf-8 -*-
# @Time : 2022/2/15 9:05
# @Author : Limusen
# @File : ckhomework01

# 兔子

def fun(i):
    if (i == 1 or i == 2):
        return 1
    else:
        return fun(i - 1) + fun(i - 2)


result = fun(4)

print(result)
