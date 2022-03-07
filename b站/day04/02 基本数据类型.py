# -*- coding: utf-8 -*-
# @Time : 2022/2/23 19:43
# @Author : Limusen
# @File : 02 基本数据类型


# 1.数据类型
# 1.1 整形int
# 作用：记录年龄、个数等等
# 定义：
age = 19
# print(type(age))

# 1.2浮点型float
# 作用：记录薪资、身高、体重
# 定义
salary = 3.3
height = 1.87
weight = 80.3
# print(type(height))

# 数字类型的其他使用
level = 1
level = level + 1
# print(level)

# print(10 + 11.2)  # int 与float之间是可以相加的

# 2.字符串类型 str
# 作用: 记录描述性质的状态,名字/一段话
# 定义: 在引号内 ('',"",''' ''',""" """,) 包含的一串字符串
info = '''
爱酸酸的啊少的可怜就阿萨德
'''
# print(type(info))
# name ="egon"
# print(egon)

# 字符串之间可以相加，但仅限于str与str之间进行。
# 代表字符串的拼接，了解即可，不推荐使用，因为str之前的相加效率极低

# print('my name is ' + 'egon')
# print("=" * 20)
# print('hello world')
# print("=" * 20)


# 3. 列表：索引对应值，索引从0开始，0代表第一个
# 作用：按照位置记录到多个值（同一个人的多个爱好、同一班级的所有学生名字），并且可以按照索引取指定位置的值

# hobbies = 'read music play' # 想取出字符串中的指定值
# print(hobbies) # 字符串是做不到的

# 定义：在[]内用逗号分隔多个任意类型的值，一个值称之为一个元素

l = [10, 3, 'aa', ['bb', 'cc'], 'dd']
print(l)

print(l[1])  # 通过下标取值

print(l[3][1])  # 嵌套取值

# 取列表的最后一个值
print(l[-1])

# 需求改造
# hobbies = 'read music play' # 想取出字符串中的指定值
# print(hobbies) # 字符串是做不到的

# hobbies = ['read', 'music' ,'play']
# print(hobbies[1])


# 其他用途：
students_info = [
    ['tony', 18, ['jack']],
    ['jason', 18, ['play', 'sleep']]
]

# 取出第一个学生的爱好
print(students_info[0][2][0])

# 索引反应的顺序、位置，对值是没有任何关系的
# 4.字典 ： key对应值，其中key通常为字符串类型，所以key对值可以有描述性功能
# 作用：用来存储多个值，每个值都有唯一一个key与其对应，key对值有对应
# 定义：在{}内用逗号分开，key:value的形式

# d = {"a": 17, "b": "xnd"}
# print(type(d))
# print(d['a'])

info = {
    "name": "egon",
    "age": 18,
    "gender": "male",
    "salary": 19
}
print(info['salary'])

# 嵌套取值
students = [
    {"name": "tony", "age": 18, "hobbies": ['sa', 'bi']},
    {"name": "jack", "age": 20, "hobbies": ['sha', 'bi']},
    {"name": "tom", "age": 30, "hobbies": ['bi', 'bi']}
]
# 取出第一个学生的第一个爱好
print(students[0]['hobbies'][0])

# 5. 布尔bool
# 作用： 用来记录真假的这两种状态
# 定义： True False

is_ok = True
is_off = False
print(type(is_off))

x = 1
y = 0

# 5.3使用
# 通常用来当做判断的条件，我们将在if判断中用到它
