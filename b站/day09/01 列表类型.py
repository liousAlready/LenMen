# -*- coding: utf-8 -*-
# @Time : 2022/3/18 10:29
# @Author : Limusen
# @File : 01 列表类型


# # 1. 作用: 按位置存放多个值
#
# # 2. 定义
# l = [1, 2, 3, 4]  # l = list([1, 2, 3, 4])
# # 3. 类型转换: 但凡能被for循环遍历的类型都可以当作参数传给list()转成列表
# res = list("hello")  # 循环字符串
# print(res)
#
# res = list({"k1":111,"k2":222,"k3":333})
# print(res)

# 4. 内置方法

# 优先掌握

# 1.按照索引取值(正向存取+反向存取):可取也可以改
# l = [111, 'egon', 'hello']
# # 正向取
# print(l[0])
# # 反向取
# print(l[-1])
# # 可取也可以改 索引存在则修改对应的值
# l[0] = 222  #
# print(l)

# 无论是取值还是赋值操作: 索引不存在则报错
# l[3]=333

# # 5.往列表中添加值
# 5.1 追加
# l = [111, 'egon', 'hello']
# l.append(333)
# l.append(444)
# print(l)

# # 5.2 插入值
# l = [111, 'egon', 'hello']
# l.insert(1, 'alex')
# print(l)

# new_1 = [1, 2, 3]
# l = [111, 'egon', 'hello']

# # extends 实现列表相加
# l.extend(new_1)
# l.extend("abc")
# print(l)


# 7.删除
# 方式一: del 通用的删除方法,只是单独的删除/没有返回值

# l = [111, 'egon', 'hello']
# del l[1]
# print(l)

# # 方法二: pop 不传入索引,就默认删除最后一个,会返回被删除的值
# l = [111, 'egon', 'hello']
# res = l.pop(0)
# print(res) # 返回被删除的值

# 方式三: l.remove() , 根据元素删除,返回None
# l = [111, 'egon', 'hello']
# l.remove('hello')
# print(l)
#
# res = l.remove("egon")
# print(res)


# 2.切片(顾头不顾尾
# l = [111, 'egon', 'hello', 'a', 'b', 'c', 'd']
# print(l[0:3])
# print(l[0:5:2])  # 0 2 4

# 拷贝
# print(l[0:len(l)])
# print(l[:])
# new_l = l[:]  # 切片等同于拷贝行为,而且相当于浅拷贝


# # 翻转列表
# print(l[::-1])
#
# # 3.长度
# print(len([1, 2, 3]))
#
# # 4.成员运算in和 not in
# print(1 in [1, 2, 3])
# print(1 not in [1, 2, 3])


# #　8.循环
# l = [1,'aaa','bbb']
# for x in l:
#     print(x)


#
# # 需要掌握的操作
#
# l = [1,'aaa','bbb']
# l.count("aaa") # 统计字符串出现多少次
# l.index("bbb") # 查找字符所在的索引位置
# l.clear() # 清除列表中元素
#
# l1 = ['egon','alex','x',1,41]
# print(l1.reverse()) # 不是排序，就是将列表倒过来

# # sort 排序 ： 列表内元素是同种类型才能排序
# l = [12, 5, 6, 2, -3]
# l.sort()  # sort 默认从小到大排
# print(l)
#
# l.sort(reverse=True)  # 降序，从大到小拍排
# print(l)

# 字符串比大小,按照对应位置的字符依次pk
# 根据ascii码值的先后顺序加以区分,表中排在后面的字符余额大于前面的

# l = ['c', 'e', 'a']
# l.sort()
# print(l)

# # 了解: 列表的也可以比大小,原理同字符串一样
# l1 = [1, 'abc', 'zaa']
# l2 = [10, '2', 'a']
# print(l1 < l2)

# # 补充
# # 1.队列: first in first out ,先进先出
# #      F I F O
# # 入队操作
# l = []
# l.append("first")
# l.append("second")
# l.append("third")
#
# print(l)
#
# # 出队列操作 先进先出
# print(l.pop(0))
# print(l.pop(0))
# print(l.pop(0))


# # 2.堆栈: LIFO,后进先出
#
# l = []
# # 入栈操作
# l.append("first")
# l.append("second")
# l.append("third")
#
# print(l)
#
# # 出队列操作 后进先出 先进后出
# print(l.pop())
# print(l.pop())
# print(l.pop())
