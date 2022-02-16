# -*- coding: utf-8 -*-
# @Time : 2022/2/16 10:47
# @Author : Limusen
# @File : test_demo01

import pytest

"""

    源码
    :arg params: an optional list of parameters which will cause multiple
                invocations of the fixture function and all of the tests
                using it.
                The current parameter is available in ``request.param``.

    fixture的可选形参列表,支持列表传入,默认None,每个param的值,fixture都会去调用执行一次,类型for循环
    可与参数IDS一起使用,作为每个参数的标识
    被fixture装饰的函数要调用是采用: request.parma 固定写法
     
"""


@pytest.fixture(params=[1, 2, {'a': 1, 'b': 2}, {4, 5, 6}],ids=['one','two','three','four'])
def demo(request):
    return request.param


def test_90(demo):
    print("值: {}".format(demo))


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
