# -*- coding: utf-8 -*-
# @Time : 2022/2/18 9:24
# @Author : Limusen
# @File : demo3

import logging


def log_header(logger_name):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(name)s] %(levelname)s  %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(logger_name)

    def _logging(something, level):
        if level == 'debug':
            logger.debug(something)
        elif level == 'warning':
            logger.warning(something)
        elif level == 'error':
            logger.error(something)
        else:
            raise Exception("I dont know what you want to do?")

    return _logging


project_1_logging = log_header('project_1')

project_2_logging = log_header('project_2')


def project_1():
    # do something
    project_1_logging('this is a debug info', 'debug')
    # do something
    project_1_logging('this is a warning info', 'warning')
    # do something
    project_1_logging('this is a error info', 'error')


def project_2():
    # do something
    project_2_logging('this is a debug info', 'debug')
    # do something
    project_2_logging('this is a warning info', 'warning')
    # do something
    project_2_logging('this is a critical info', 'error')


# project_1()
# project_2()


def adder(x):
    def wrapper(y):
        return x + y

    return wrapper  # 注意，这里返回的是wrapper,不是wrapper()


adder5 = adder(5)  # 这里的adder5是不是变量，它是函数的对象，print(adder5) 输出<function wrapper at 0x10fcaf0c8>。
# 输出 15
print(adder5(10))  # 所以10就是adder5这个函数对象的参数。
# 输出 11     # 注意⚠️函数对象！！！面向对象编程思想
print(adder5(6))

# 这就是闭包的特点，adder(10)(20)的结果是30，闭包允许函数关联的参数与内部的参数关联，这正是它的特色
print(adder(10)(20))