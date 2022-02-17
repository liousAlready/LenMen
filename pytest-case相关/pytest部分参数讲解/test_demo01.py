# -*- coding: utf-8 -*-
# @Time : 2022/2/15 11:15
# @Author : Limusen
# @File : test01

"""

    参数                  完整命令                说明                              场景

    --collect-only      pytest --collect-only   收集目录下所有用例                  测试运行之前,检查选中的用例是否符合预期
    -k                  pytest -k "筛选条件"     模糊筛选指定的case                  希望只允许特定的用例
    -m                  pytest -m "标记名称"     标记测试并分组,以便快速选中并运行      与@pytest.mark.标签使用
    -x                  pytest -x              遇到错误即停止测试,下面的case不会运行   debug时使用
    --maxfail=num       pytest --maxfail=2     明确指定失败几次后停止运行脚本          批量运行时,错误超过预期次数时,停止运行脚本
    --lf(--last-failed) pytest --lf            脚本运行失败后,仅重试失败的用例         只运行失败的用例,其他状态的用例不会运行
    --ff(--failed-first)pytest --ff            与--lf相似,先运行失败用例,其他用例也会运行  脚本希望从失败用例开始运行,再运行其他

"""

import pytest


def test_a():
    assert (1, 2, 3) == (1, 2, 3)


def test_failing():
    assert (1, 2, 3) == (4, 5, 6)


def test_failing02():
    assert (1, 2, 4) == (2, 41, 2)


def test_b():
    assert (1, 2, 3) == (1, 2, 3)


@pytest.mark.smoke1
def test_c():
    assert (1, 2, 3) == (1, 2, 3)


@pytest.mark.smoke2
def test_d():
    assert (1, 2, 3) == (1, 2, 3)


if __name__ == '__main__':
    pytest.main()