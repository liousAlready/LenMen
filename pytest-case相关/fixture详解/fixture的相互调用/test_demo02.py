# -*- coding: utf-8 -*-
# @Time : 2022/2/15 17:53
# @Author : Limusen
# @File : test_demo02


import pytest


@pytest.fixture()
def account():
    a = "account"
    print("第一层fixture")
    return a


@pytest.fixture()
def login(account):
    print("第二层fixture")


class TestLogin():

    # 传入loginfixture
    def test_01(self, login):
        print("直接使用第二层fixture,返回值为{}".format(login))

    def test_02(self, account):
        print("只调用account fixture,返回值为{}".format(account))


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
