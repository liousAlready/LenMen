# -*- coding: utf-8 -*-
# @Time : 2022/2/18 15:55
# @Author : Limusen
# @File : 带参数的装饰器02


url_mapping = {}


def route(url):
    def decorator(func):
        url_mapping[url] = func
        return func

    return decorator


@route("/home")
def home():
    pass


@route("/index")
def index():
    pass


print()
