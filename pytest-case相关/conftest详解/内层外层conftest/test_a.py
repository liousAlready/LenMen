# -*- coding: utf-8 -*-
# @Time : 2022/2/16 13:43
# @Author : Limusen
# @File : test_a

import pytest


class TestLogin():

    def test_01(self, login2):
        print("外层用例001")

    def test_02(self, login):
        print("外层用例002")


if __name__ == '__main__':
    pytest.main(['-s', '-v'])

"""

    conftest.py的作用域与python变量作用域先沟通
    注意:
    1.上级调用下级的fixture会报错,找不到这个fixture
    
    2.只能是下级调用上级的fixture,因为conftest会从当前目录查找如果找不到fixture,
    就会查找上一级目录,知道查找到为止
    
    内层包的conftest.py不允许被其他包的测试类或方法使用,相当于本地变量
    外层的conftest.py可被内层测试类和方法使用,相当于全局变量
"""