# -*- coding: utf-8 -*-
# @Time : 2022/2/16 10:03
# @Author : Limusen
# @File : test_demo

"""

默认为False

若为True,每个测试函数都会自动调用该fixture 无需传入fixture函数名

@pytest.fixture(autouse=True)
"""

import pytest


@pytest.fixture(autouse=True)
def login():
    print("登录前预制操作")


class TestLogin:

    def test_01(self):
        print("001")

    def test_2(self):
        print("002")

    def test_3(self):
        print("003")

if __name__ == '__main__':
    pytest.main(['-s','-v'])