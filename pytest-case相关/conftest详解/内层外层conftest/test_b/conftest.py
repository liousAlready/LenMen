# -*- coding: utf-8 -*-
# @Time : 2022/2/16 13:40
# @Author : Limusen
# @File : conftest


"""

内层conftest


"""

import pytest

@pytest.fixture(scope="session")
def login2():
    print("内层的login-fixture")

