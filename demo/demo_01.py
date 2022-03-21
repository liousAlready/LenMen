# -*- coding: utf-8 -*-
# @Time : 2022/3/21 9:40
# @Author : Limusen
# @File : demo_01


arr = [8,3,2,5,6,9,1]
for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1-i):
        if arr[j] >= arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)