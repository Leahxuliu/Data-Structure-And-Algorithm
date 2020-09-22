# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
1. 题目类型：
    DP

2. 题目要求：
    给定一个正整数s, 判断一个数组arr中，是否有一组数字加起来等于s
    都是正整数

'''

# 递归
arr = [3, 34, 4, 12, 5, 2]
def rec_subset(arr, i, s):
    if i == 0:  
        return arr[0] == s
    '''
    if i == 0:  
        return arr[0] == s
    错误
    因为后面还有i-1
    '''
    if arr[i] > s:
        return rec_subset(arr, i-1, s)
    if s == 0:
        return True
    
    return rec_subset(arr, i-1, s-arr[i]) or rec_subset(arr, i-1, s)

print(rec_subset(arr, len(arr)-1, 13))
print(rec_subset(arr, len(arr)-1, 9))


# DP
# 不用numpy0
def dp_subset(arr, S):
    subset = [[False] * (S+1) for _ in range(len(arr))]
    
    for i in range(len(arr)):
        for s in range(S+1):
            if arr[i] == s:
                subset[i][s] = True
            elif arr[i] > s:
                subset[i][s] = subset[i-1][s]
                # print(subset[i][s])
            else:
                subset[i][s] = subset[i-1][s] or subset[i-1][s-arr[i]]
                # print(subset[i][s])

    return subset[len(arr)-1][S]

print(dp_subset(arr, 9))
print(dp_subset(arr, 12))
print(dp_subset(arr, 13))


# 用numpy
import numpy as np
def dp_subset(arr, S):
    subset = np.zeros((len(arr), S+1), dtype=bool)
    # subset = [[False] * (s+1) for _ in range(len(arr))]
    subset[:, 0] = True  # 第n行第1列都是Ture
    subset[0, :] = False # 第一行都是False
    subset[0, arr[0]] = True
    for i in range(1, len(arr)):
        for j in range(1, S+1):
            if arr[i] > j:
                subset[i, j] = subset[i-1, j]
            else:
                A = subset[i-1, j - arr[i]]
                B = subset[i-1, j]
                subset[i,j] = A or B
    #print(subset)
    return subset[len(arr)-1, S]
                
print(dp_subset([3, 34, 4, 12, 5, 2], 9))
print(dp_subset([3, 34, 4, 12, 5, 2], 13))