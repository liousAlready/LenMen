# -*- coding: utf-8 -*-
# @Time : 2022/2/15 17:24
# @Author : Limusen
# @File : test_demo02


"""

@pytest.fixture或者@pytest.fixture(scope="function")

"""

"""场景一:作为参数传入"""

import pytest


class TestLogin:

    # 传入loginfixture
    def test_01(self, login):
        print("001传入login fixture")

    # 传入logoutfixture
    def test_02(self,logout):
        print("002传入logou fixture")

    def test_03(self,login,logout):
        print("003传入两个fixture")

    def test_04(self):
        print("什么都不传")


if __name__ == '__main__':
    pytest.main(['-s','-v'])