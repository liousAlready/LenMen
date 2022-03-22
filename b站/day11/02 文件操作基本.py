# -*- coding: utf-8 -*-
# @Time : 2022/3/22 9:43
# @Author : Limusen
# @File : 02 文件操作基本


# 1.打开文件

# windows路径分隔符问题
# open('C:\a\nb\d.txt')
# 解决方案一:推荐使用
# open(r'C:\a\nb\d.txt')
# 解决方案二:
# open('C:/a/nb/d.txt')

# # 根据当前文件夹查找

f = open('b.txt', mode='rt', encoding='utf-8')  # f的值是一种变量
# print(f)
# 2.操作文件：读、写文件,应用程序对文件的读写请求都是在向操作系统发送
# 系统调用,然后由操作系统控制硬盘完成底层的读写
res = f.read()
print(res)
# 3.关闭文件

f.close()  # 回收操作系统资源

# del f  # 回收应用程序资源
