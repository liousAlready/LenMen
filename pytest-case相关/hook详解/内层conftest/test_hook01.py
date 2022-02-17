# -*- coding: utf-8 -*-
# @Time : 2022/2/17 9:40
# @Author : Limusen
# @File : test_hook01


import pytest


class TestHook:

    def test_hook1(self, login):
        print("这里是test_hook1")

    def test_hook2(self):
        print("这里是test_hook2")

    def test_hook3(self):
        print("这里是test_hook3")


if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])
