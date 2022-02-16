# -*- coding: utf-8 -*-
# @Time : 2022/2/15 15:31
# @Author : Limusen
# @File : conftest

import pytest


@pytest.fixture()
def login():
    print("输入账号密码")
    yield
    print("清理数据完成")


@pytest.fixture()
def loginout():
    print("退出登录")
