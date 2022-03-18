# -*- coding: utf-8 -*-
# @Time : 2022/3/18 14:18
# @Author : Limusen
# @File : 03 字典

# 1.作用

# 2.定义： 在{} 内用逗号分割开多个key:value
# 其中value可以使用任意类型，但是key必须为不可变类型,且不能重复
# d = {"k1": 111, "k2": 122, 18: 23, (11): 22}
# print(d['k1'])
# print(d[(11)]) # d = dict(...)

# print(type(d))

# # d = {}  # 默认定义出来的是空字典
# d = dict(x=1,y=3,z=3)
# print(d, type(d))

# # 3.数据类型转换
# info = [
#     ['name', 'egon'],
#     ('age', 18),
#     ['gender', 'male']
# ]
# d = {}

# for item in info:
#     d[item[0]] = item[1]
# print(d)

# for k,v in info:
#     d[k] = v
# print(d)
#
# res = dict(info)  # 一行代码搞定上述for循环
# print(res)

# # 造字典的方式 : 快速初始化一个字典
keys = ['name', 'age', 'gender']

# d = {}
# for k in keys:
#     d[k] = None
# print(d)
#
# d = {}.fromkeys(keys, None)
# print(d)

# 4.内置方法

# 优先掌握

# # 1.key存取值:客村可取
# d = {"k1": 111}
# # 针对赋值操作: key存在,则修改
# d["k1"] = 222
# print(d)
#
# # 针对赋值操作: key不存在,则创建新值
# d["k2"] = 333
# print(d)

# # 2.长度len
# d = {"k1": 111,"k2":222,"k1": 323,"k1": 222}
# print(d)
# print(len(d))

# # 3. in 和 not it
# d = {"k1": 111,"k2":222}
# print('k1' in d)
# print(111 in d)

# 4.删除
d = {"k1": 111, "k2": 222}
# # 4.1 通用删除
# del d['k1']
# print(d )

# # 4.2  pop 删除:根据key删除 返回删除key的value
# res = d.pop('k1')
# print(res) # 返回删除key的value
# # print(d)

# # 4.3 popitem 随机删除 返回元组（删除的key，删除的value）
# res = d.popitem()
# # print(d)
# print(res)

# 5. 键 keys() 值 values() 键值对items() ==> 在python3中得到的是老母鸡
#
# d = {"k1": 111, "k2": 222}
#
# # 6. for 循环
# for k in d.keys():
#     print(k)
#
# for v in d.values():
#     print(v)
#
# for k,v in d.items():
#     print(k,v)
#
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))


# 需要掌握的内置方法

# # 1.清空字典
# d.clear()
# print(d)

# 2.更新字典 新字典更新老字典,一切以新字典为主
# dic = {"k2": 222, "k3": 333, "k1": 1111111111}
# d.update(dic)
# print(d)

# 3.获取key取值

# print(dic['k4']) # key不存在则报错
# print(d.get("k3"))  # key不存在不报错，返回none

# 4.1 设置默认值
# d.setdefault()
# 如果值不存在,则插入,如果存在则不进行操作
info = {"name": "egon"}
info.setdefault("age", 19)
print(info)

# 4.2 如果存在则不插入
info = {"name": "egon"}
info.setdefault("name", "xls")  # 没有改变
print(info)
