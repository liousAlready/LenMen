# -*- coding: utf-8 -*-
# @Time : 2022/2/15 17:53
# @Author : Limusen
# @File : conftest

import pytest


@pytest.fixture()
def account():
    a = "account"
    print("第一层fixture")
    return a


@pytest.fixture()
def login(account):
    print("第二层fixture")
