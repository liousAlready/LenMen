# -*- coding: utf-8 -*-
# @Time : 2022/2/15 15:19
# @Author : Limusen
# @File : test_demo03

"""

1.conftest.py是什么
    conftest.py 是fixture函数的一个集合.可以理解为从公共的文件提取出来放在一个文件里.然后供其他模块调用.
    不同于普通被调用的模块

    conftest.py使用时不需要导入,pytest会自动查找

2.conftest使用场景
    如果我们有很多个前置函数,写在各个py文件里面是不是很乱
    我们很多个py文件想要使用同一个前置函数怎么办?这也就是conftest.py的作用

3.conftest使用原则
    conftest.py这个文件名是固定的,不可以更改
    conftest.py与运行用例在同一个包下,并且该包中有__init__.py文件
    不需要导入conftest.py文件

"""

import pytest


class TestLogin():

    def test_1(self, login):
        print("测试用例1 带入了login fixture")

    def test_2(self, loginout):
        print("测试用例2 带入了loginout fixture")

    def test_3(self, login, loginout):
        print("测试用例3 带入了login fixture 跟loginout fixture")

    def test_4(self):
        print("测试用例4 未使用任何fixture")


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_demo03.py'])
