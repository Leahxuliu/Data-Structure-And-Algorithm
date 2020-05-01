#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/01  
# @Author  : XU Liu
# @FileName: 624.Maximum Distance in Arrays.py

'''
1. 题目要求：


2. 理解：


3. 输出输入以及边界条件：
input:  list[list]; length range is 2 to 10000; elements value range is from -1000 to 1000
output: int
corner case: 

4. 解题思路
思路1 报错:
先用merge sort对arrays进行排序,最大Distance等于sorted array中最后一个数减第一个数
错误原因，合并排序的时候，把结果放到原来的array当中时，原来的array是list里面list，所以会出现out of range
    
5. 空间时间复杂度

'''

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minVal = arrays[0][0]
        maxVal = arrays[0][-1]
        res = float('-inf')
        # res = abs(maxVal - minVal) 错误，因为最大距离不能是本array里的最大值减最小值
        
        for i in range(len(arrays)):
 
            res = max(res, abs(arrays[i][-1] - minVal), abs(maxVal - arrays[i][0]))
            minVal = min(arrays[i][0], minVal)
            maxVal = max(arrays[i][-1], maxVal)
        
        return res