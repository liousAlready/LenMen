# -*- coding: utf-8 -*-
# @Time : 2022/2/16 19:52
# @Author : Limusen
# @File : test_demo211


"""

测试用例失败重试:
    测试用例失败后要重新运行n次,要在重新运行之间添加延迟时间,间隔n秒再运行

安装:
    pip install pytest-rerunfailures

语法:
    pytest -v --reruns 3 --reruns-delay 2 # 运行三次每次等待两秒

"""

import pytest


def test_a():
    assert (1, 2, 3) == (1, 2, 3)

@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_failing():
    assert (1, 2, 3) == (4, 5, 6)

if __name__ == '__main__':
    # pytest.main(["--reruns=3","--reruns-delay=2",__file__])
    pytest.main([__file__])