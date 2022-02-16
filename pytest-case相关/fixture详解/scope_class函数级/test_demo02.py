# -*- coding: utf-8 -*-
# @Time : 2022/2/15 17:24
# @Author : Limusen
# @File : test_demo02


"""

@pytest.fixture或者@pytest.fixture(scope="function")

fixture作用域class
"""

import pytest


@pytest.fixture(scope='class')
def login():
    print("scope为class")


class TestLogin:

    def test_01(self):
        print("001")

    def test_02(self, login):
        print("002")

    def test_03(self, login):
        print("003")


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
