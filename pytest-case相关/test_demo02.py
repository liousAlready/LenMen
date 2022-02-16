# -*- coding: utf-8 -*-
# @Time : 2022/2/15 13:53
# @Author : Limusen
# @File : test_demo02


"""

测试用例执行顺序

场景:未考虑按自然顺序执行时,或是想要变更执行顺序,比如增加数据的用例要先执行,再进行删除的用例
第三方库: pip install pytest-ordering
用法:在测试方法上面加装饰器

@pytest.mark.last 最后一个执行
@pytest.mark.run(order = x) x等于第几个执行该用例

pytest是默认按照字母顺序执行
"""

import pytest
import pytest_ordering


@pytest.mark.run(order=1)
def test_01():
    print("test01")

@pytest.mark.run(order=2)
def test_02():
    print("test02")

@pytest.mark.last
def test_06():
    print("test05")

def test_04():
    print("test04")

def test_05():
    print("test05")

@pytest.mark.run(order=3)
def test_03():
    print("test03")


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_demo02.py'])
