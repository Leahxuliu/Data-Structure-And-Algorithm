# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
1. 题目类型：
    DP

2. 题目要求：
    给定一个正整数s, 判断一个数组arr中，是否有一组数字加起来等于s
    都是正整数

'''

# 方案1
# 递归
    
arr = [1,2,4,1,7,8,3]
def rec_opt(arr, i):
    if i == 0:
        return arr[0]
    if i == 1:
        return max(arr[0], arr[1])
    
    return max(rec_opt(arr, i-2) + arr[i], rec_opt(arr, i-1))

print(rec_opt(arr, len(arr)-1))


# 方案2
# DP

def dp_opt(arr):
    opt = [0] * len(arr)

    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        opt[i] = max(opt[i-2]+arr[i], opt[i-1])
    
    return opt[len(arr) - 1]

print(dp_opt(arr))