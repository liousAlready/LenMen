# -*- coding: utf-8 -*-
# @Time : 2022/2/18 14:46
# @Author : Limusen
# @File : 类方法


class Student(object):
    school = 'szu'

    @classmethod
    def printmassage(cls):
        print(cls.school)


s1 = Student()
Student.printmassage()  # szu
s1.printmassage()  # szu


