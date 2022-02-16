# -*- coding: utf-8 -*-
# @Time : 2022/2/15 17:24
# @Author : Limusen
# @File : test_demo02


"""

@pytest.fixture或者@pytest.fixture(scope="module")

fixture作用域module

module是对当前.py文件生效
session是对多个.py文件生效
session只作用于一个.py文件时,相当于module

只对开始引用的测试方法的类和方法生效
"""

import pytest


@pytest.fixture(scope='module')
def login():
    print("scope为module")


def test_01():
    print("001")


def test_02(login):
    print("002")


class TestLogin:

    def test_1(self):
        print("001")

    def test_2(self):
        print("002")

    def test_3(self):
        print("003")


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
