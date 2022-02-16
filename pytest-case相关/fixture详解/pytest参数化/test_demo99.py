# -*- coding: utf-8 -*-
# @Time : 2022/2/16 15:56
# @Author : Limusen
# @File : test99


"""

背景: pytest的测试用例需要参数化

说明: 在测试中,输入相应值,检查期望值,是常见的测试方法.
     在自动化测试中,一个测试用例对应一个测试点,通畅一组测试数据无法完全覆盖测试范围,所以需要参数化来传递多组参数.

用法:
    @pytest.mark.parametrize(argnames,argvalues)
    argnames: 以逗号分隔的字符串
    argvalues: 参数值列表,若有多个参数,一组参数以元祖形式存在,包含多组参数的所有参数

"""

import pytest


# 参数化值一个参数


@pytest.mark.parametrize("arg_1", [4399, 1994])
def test_1(arg_1):
    # print(arg_1)
    print("测试用例01,参数: [{}]".format(arg_1))


# 参数化之多个参数

@pytest.mark.parametrize("arg_1,arg_2", [(4399, "AAAA"), (1994, "BBNB")])
def test_1(arg_1, arg_2):
    print("测试用例01,参数: [{},{}]".format(arg_1, arg_2))


if __name__ == '__main__':
    pytest.main(['-s', '-v'])


# 比如有两个查询条件,每个条件有三个选项 3*3 =9

@pytest.mark.parametrize("arg_1", [4399,2021,1994])
@pytest.mark.parametrize("arg_2", ['AAAA','BBBB','CCCC'])
def test_66(arg_1,arg_2):
    print('arg_1: {}, arg_2: {}'.format(arg_1,arg_2))


if __name__ == '__main__':
    pytest.main(['-s', '-v'])