#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/28  
# @Author  : XU Liu
# @FileName: 845.Longest Mountain in Array.py

'''
1. 题目要求：
把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”
找到最长的山脉
B.length >= 3
存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

[2,1,4,7,3,2,5]  --> 最长的 “山脉” 是 [1,4,7,3,2]，长度为 5
[2,2,2] --> 不含 “山脉”

Can you solve it using only one pass?
Can you solve it in O(1) space?

2. 理解：


3. 输出输入以及边界条件：
input: list[int]
output: the length of the longest Mountain, int
corner case: len(A) < 3 --> 0, 

4. 解题思路
two pointers 对开指针

1. 先找到peak; A[i - 1] < A[i] and A[i + 1] < A[i]
2.然后用左右两个对开指针，寻找最长左山脉和最长右山脉,计算最长的length
    
    
5. 空间时间复杂度
Time: O(2n) = O(n)
Space: O(1)
'''

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        
        if n < 3:
            return 0
        res = 0
        for i in range(1, n - 1):
            if A[i - 1] < A[i] and A[i] > A[i + 1]:
                i, j = i - 1, i + 1
                while i >= 1:
                    if A[i] > A[i - 1]:
                        i -= 1
                    else:
                        break
                while j <= n - 2:
                    if A[j] > A[j + 1]:
                        j += 1
                    else:
                        break
                res = max(res, (j - i + 1))
        return res
