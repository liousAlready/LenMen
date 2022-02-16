# -*- coding: utf-8 -*-
# @Time : 2022/2/15 16:39
# @Author : Limusen
# @File : test_demo01


"""

1.前言
    fixture是pytest的核心功能,也是亮点功能,属于装饰器(在不改变装饰器函数的前提下对函数进行功能增强),用户在测试用例之前进行前后置工作处理
    与setup/teardown类型,但更加强大灵活

2.fixture简介


3.fixture工作原理
    @pytest.fixture() 装饰器用于声明函数是一个fixture.如果测试函数的参数列表中包含了fixture装饰的函数名
    那么pytest就会检测到,然后在测试函数运行之前执行该fixture
    如果fixture装饰的函数有返回值,那么fixture在完成任务后,将数据再返回给测试函数(相当于传参)

4.pytest搜索fixture的顺序
    测试用例的参数列表中包含一个fixture名,pytest会用该名称搜索fixture
    优先搜索测试所在的模块
    然后再搜索模块统一路径下的conftest.py
    找不到再上一层的conftest.py

5.fixture参数详解以及使用

    scope
         scope = "function" 每一个函数或方法都会调用
         scope = "class"  每一个测试类只运行一次
         scope = "module" 与class相同
         scope = "session"  每次会话只需要运行一次

    params
    ids
    autouse
    name
"""