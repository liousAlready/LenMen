# -*- coding: utf-8 -*-
# @Time : 2022/2/17 9:39
# @Author : Limusen
# @File : conftest

import pytest
import time


@pytest.fixture()
def login():
    print("登陆前清理环境")
    print("*" * 50)
    print("执行登录用例")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    print('*' * 50)
    # 获取钩子方法的调用结果
    out = yield
    print('用例执行结果', out)
    # 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    # 通过 when 来区分 setup,call,teardown 这三个阶段
    if report.when == "call":
        print('测试报告：{}'.format(report))
        print('步骤：{}'.format(report.when))
        print('nodeid：{}'.format(report.nodeid))
        print('description:{}'.format(str(item.function.__doc__)))
        print(('运行结果: {}'.format(report.outcome)))
        print('*' * 50)


# conftest.py
# 收集测试结果
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    print("收集测试结果开始:")
    print("*"*30)
    print(terminalreporter.stats)
    print("total:", terminalreporter._numcollected)
    print('passed:', len(terminalreporter.stats.get('passed', [])))
    print('failed:', len(terminalreporter.stats.get('failed', [])))
    print('error:', len(terminalreporter.stats.get('error', [])))
    print('skipped:', len(terminalreporter.stats.get('skipped', [])))
    # terminalreporter._sessionstarttime 会话开始时间
    duration = time.time() - terminalreporter._sessionstarttime
    print('total times:', duration, 's')
    print("收集测试结果结束:")
    print("*" * 30)