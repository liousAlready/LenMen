# -*- coding: utf-8 -*-
# @Time : 2022/2/18 14:08
# @Author : Limusen
# @File : 静态属性


class Student(object):
    school = 'szu'

    @property
    def print_massage(self):
        print('aaaa')


s1 = Student()
s1.print_massage # 将类方法转变成类属性
print(s1.school)