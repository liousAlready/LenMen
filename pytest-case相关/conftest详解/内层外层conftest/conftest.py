# -*- coding: utf-8 -*-
# @Time : 2022/2/16 13:40
# @Author : Limusen
# @File : conftest

import pytest

@pytest.fixture(scope='session')
def login():
    print("外层fixture")