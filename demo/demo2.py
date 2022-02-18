# -*- coding: utf-8 -*-
# @Time : 2022/2/18 9:12
# @Author : Limusen
# @File : demo2

def who(name):
    def do(what):
        print(name, 'say:', what)

    return do


lucy = who('lucy')
john = who('john')

lucy('i want drink!')
lucy('i want eat !')
lucy('i want play !')

john('i want play basketball')
john('i want to sleep with U,do U?')

lucy("you just like a fool, but i got you!")