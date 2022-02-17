# -*- coding: utf-8 -*-
# @Time : 2022/2/16 19:01
# @Author : Limusen
# @File : test_demo01


"""

pytest运行用户自定义自己的用例标签,用于将用例进行分组,以便运行用例时选出你想要运行的用例

@pytest.mark.自定义标签的使用:

    1. 可以标记测试方法/测试类,标记名可以自定义,最好起有意义的名字
    2. 同一个类/方法,可以拥有多个标记

"""

import pytest


@pytest.mark.smoke1
def test_01():
    print("test01")


@pytest.mark.smoke2
def test_02():
    print("test02")


@pytest.mark.smoke2
@pytest.mark.smoke1
def test_03():
    print("test03")


if __name__ == '__main__':
    pytest.main(['-s', '-v','-m smoke1', __file__])
