# encoding: utf-8
# Author    : limusen
# Datetime  : 2022/1/15 2:51 下午
# Project   : LenMen
# File      : ck01_02day_1.py
# explain   : 文件说明


# # 推导式  快速创建列表、字典
#
# # url = ['page1','page2']
#
# urls = []
# for i in range(1, 100):
#     url = "page{}".format(i)
#     urls.append(url)
# print(urls)
#
# # 列表推导式 []
# # for 循环将值放入i
# urls1 = ["page{}".format(i) for i in range(1, 100)]
#
# print(urls1)
#
# # 字典推导式 {}
# dit1 = {i: i + 1 for i in range(10)}
# print(dit1)
#
# # 将以下字符串用字典推导式改成字典类型数据
# cook_str = "asdasd=asdasdqwe;pstm=154564651465;NAIDUID=kalsjdkajskldjas23;sutkskaq=0;___ckaskldla=alskdqweqwe"
#
# cook_dict = {i.split("=")[0]: i.split("=")[1] for i in cook_str.split(";")}
# print(cook_dict)
#
# # 生成器表达式  () 降低内存空间 提高代码性能
# # <generator object <genexpr> at 0x107b245d0>
tu = (i for i in range(1, 10))  # 生成器对象
# print(tu)
#
# # # 通过list转换生成器
# # lt = list(tu)
# # print(lt)
#
# a = next(tu)
# print(a)
# print(next(tu))

# # 通过 yield定义生成器
# def gen_fun():
#     yield 100
#     print("hello")
#     yield 1000
#
#     yield 1000100001100
#
#
# res = gen_fun()  # 返回生成器对象 返回yield的返回对象
# print(next(res))
# print(next(res))
# print(next(res))


# 迭代器

# 可迭代对象，可以for循环遍历的都是可迭代对象
# 内部只实现了 __iter__
# 列表
list1 = [1, 2, 3, 4]
li1 = iter(list1)  # 触发 iter() __iter__


# 将迭代对象放进去可以变成可迭代对象

# # 迭代器内部实现了 __iter__ 之外，还实现了__next__
# print(next(li1))  # 触发 __next__ 方法
# print(next(li1))
# print(next(li1))
# print(type(li1))


# 生成器是迭代器的一种

# 生成器相比迭代多了几种方法   send
# tu.send()  # 与生成器进行交互  可以将数据传输到生成器里面

def gen():
    for i in range(1, 5):
        se = yield i  # send 的值会在yield执行之后存储到变量 可以输出
        print("se的值: %s" % se)


g = gen()

print(next(g))

print(g.send(100)) # 设置se的值

print(next(g)) # 第三次，因为没有设置se的值，所以返回为空
