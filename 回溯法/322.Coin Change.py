# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/04  
# @Author  : XU Liu
# @FileName: 322.Coin Change.py

'''
1. 题目类型：


2. 题目要求与理解：


3. 解题思路：


4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    

'''


def dp_opt(arr):
    #opt = np.zeros(len(arr))  # 指定一个里面都是0，大小为len(arr)的数组, memo
    #print(opt)
    opt = [0] * len(arr)
    print(opt)
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        A = opt[i-2] + arr[i]
        B = opt[i-1]
        opt[i] = max(A, B)
    print(opt)
    
    return opt[-1]

arr = [1,2,4,1,7,8,3]
print(dp_opt(arr))
