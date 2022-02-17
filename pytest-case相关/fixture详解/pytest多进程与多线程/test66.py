# -*- coding: utf-8 -*-
# @Time : 2022/2/16 16:50
# @Author : Limusen
# @File : test66


"""

进程: 工厂
线程: 工人

打开微信,开启一个进程,在微信界面操作查看朋友圈,搜啊一扫,抖一抖,这么多操作就是线程
进程是包含线程,线程是进程的一个子集

一. 安装
pip install pytest-xdist
pip install pytest-parallel

二. 对比说明
    pytest-parallel比pytest-xdist相对好用,功能支持的多
    pytest-xdist

    多进程: linux或者mac windows不起作用永远是1
    多线程: linux mac windows 平台都支持

三. pytest-xdist常用配置命令
    -n :  进程数,而是cpu个数   n越多进程越多 执行越快
    示例:
    pytest -s test_1.py -n=2

四. pytest-parallel常用配置命令
    --workers * : 多进程运行需要加载此参数  [*] 是进程数 默认为1
    --test-per-worker * : 多线程运行, [*]是每个worker运行的最大并发线程数,默认是1
    示例:
    pytest test.py --workers 3    # 指的是3个进程运行
    pytest test.py --test-per-worker 4 # 指的是4个进程运行
    pytest

"""

import pytest
import time


def testcase_01():
    time.sleep(2)
    print("这里是testcase_01")


def testcase_02():
    time.sleep(2)
    print("这里是testcase_02")


def testcase_03():
    time.sleep(2)
    print("这里是testcase_03")


# #pytest-xdist 运行方式
# if __name__ == '__main__':
#     pytest.main(['-s', __file__, '-n=4'])

# pytest-xdist 跟 pytest-parallel 一起使用

if __name__ == '__main__':
    # pytest.main(['-s',  '--workers=2', '--tests-per-worker=4', __file__])
    pytest.main(['-s', '--workers=1', '--tests-per-worker=1', __file__])