# -*- coding: utf-8 -*-
# @Time : 2022/2/16 13:24
# @Author : Limusen
# @File : test_demo8


import pytest

"""

调用的方法: 

@pytest.mark.usefixtures('fixture1','fixture2')

"""


@pytest.fixture(name="new_fixture")
def test_name():
    pass


# 使用name参数后,传入重命名函数,执行成功
def test_1(new_fixture):
    print("使用name参数后,传入重命名函数,执行成功")


def test_2(test_name):
    print("使用原函数名,会失败")


if __name__ == '__main__':
    pytest.main(['-s','-v'])