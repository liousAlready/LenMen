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


"""

注意:

    1.即使fixture之前支持相互调用,但是普通函数直接使用fixture是不支持的,一定是在测试函数内调用才会逐级调用生效
    2.有多层fixture调用时,最先执行的是最后一层fixture,而不是先执行传入测试函数的fixture
    3.上层fixture的值不会自动return,这里就类似互相调用函数一样的逻辑

"""

if __name__ == '__main__':
    pytest.main(['-s', '-v'])

"""
执行顺序

test_demo02.py::TestLogin::test_01 第一层fixture
第二层fixture
直接使用第二层fixture,返回值为None
PASSED
test_demo02.py::TestLogin::test_02 第一层fixture
只调用account fixture,返回值为account
PASSED

"""