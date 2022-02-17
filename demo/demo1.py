# -*- coding: utf-8 -*-
# @Time : 2022/2/17 10:07
# @Author : Limusen
# @File : demo1


"""

字符串消消乐，将字符串中相邻相同的字符一起消掉，最后输出消除完成的字符串

示例：abcccbxezzzrf7788fn
输出：axern

说明：从左住右消除，第一趟消除相邻相同的“ccc”、“zzz”、“77”、“88”，
得到abbxerffn，第二趟消除相邻相同的“bb”、“ff”，得到axern，
不存在相邻相同字符，消除结束。


题目
输入："abbaca"
输出："ca"
"""

S = "abbaca"
st = []

for i in S:
    if len(st)==0:
        st.append(i)
    elif i == st[-1]:
        st.pop()
    else:
        st.append(i)
print(st)








