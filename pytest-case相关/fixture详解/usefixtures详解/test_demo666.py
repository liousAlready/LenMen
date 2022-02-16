# -*- coding: utf-8 -*-
# @Time : 2022/2/16 14:12
# @Author : Limusen
# @File : test_demo666


"""

@pytest.mark.usefixtures是pytest调用fixture的方法之一,与直接传入fixture不同的是,
他无法获取到fixture装饰的函数的返回值.

@pytest.mark.usefixtures的使用场景是被测试函数需要多个fixture做前后置工作时使用

用法:
@pytest.mark.usefixtures(self,*fixturenames)
def test_1():
    pass

*fixturenames: fixture的名字,传入的是@pytest.fixture(name)里的name值,可以传多个
"""

#
import pytest

#
# # 场景一: 传入单个fixture
# @pytest.fixture()
# def one():
#     print("我是一个fixture函数")
#
#
# @pytest.mark.usefixtures("one")
# def test_one_fixture():
#     print("测试用例一")
#     assert 1 == 1


# # 场景二: 传入多个fixture
# @pytest.fixture()
# def one():
#     print("我是第一个fixture函数")
#
#
# @pytest.fixture()
# def two():
#     print("我是第二个fixture函数")
#
#
# @pytest.mark.usefixtures("one", "two")
# def test_one_fixture():
#     print("测试用例一")
#     assert 1 == 1

# 场景三:叠加使用
"""
从下往上执行
"""


@pytest.fixture()
def one():
    print("我是第一个fixture函数")


@pytest.fixture()
def two():
    print("我是第二个fixture函数")


@pytest.mark.usefixtures("two")
@pytest.mark.usefixtures("one")
def test_one_fixture():
    print("测试用例一")
    assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-s', '-v'])

"""

总结:
    1.单个fixture:在被测试函数之前执行
    2.多个fixture:按传值先后顺序执行
    3.叠加fixture:自下至上执行,离测试函数越近的先被执行

"""