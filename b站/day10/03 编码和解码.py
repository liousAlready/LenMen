# -*- coding: utf-8 -*-
# @Time : 2022/3/21 20:03
# @Author : Limusen
# @File : 03 编码和解码

x = '上'

res = x.encode('gbk')  # unicode-->gbk
# print(res)


print(res.decode('gbk'))