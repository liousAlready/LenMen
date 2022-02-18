2  # -*- coding: utf-8 -*-


# @Time : 2022/2/18 9:16
# @Author : Limusen
# @File : demo


# 　闭包

def who(name):
    def do(do_it):
        print(name, "say:", do_it)

    return do


res = who("xia")
res("shabi")
