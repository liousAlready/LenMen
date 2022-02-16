# -*- coding: utf-8 -*-
# @Time : 2022/2/15 17:25
# @Author : Limusen
# @File : conftest

import pytest


# fixture函数作为多个参数传入
@pytest.fixture()
def login():
    print("打开浏览器")
    a = "account"
    return a

@pytest.fixture()
def logout():
    print("关闭浏览器")
    a = "account"
    return a

