# -*- coding: utf-8 -*-
# @Time : 2022/2/16 13:41
# @Author : Limusen
# @File : test_b


import pytest


class TestLogin():

    def test_1(self, login2):
        print("test1")

    def test_2(self, login):
        print("test2")

if __name__ == '__main__':
    pytest.main(['-s','-v'])