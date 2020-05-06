# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/06  
# @Author  : XU Liu
# @FileName: 452.Minimum Number of Arrows to Burst Balloons.py

'''
1. 题目要求：
射气球

2. 理解：
求有几个区间


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
greedy
    1. sort start
    2. start > pre_ending  --> pre_ending = end, count += 1
    
5. 空间时间复杂度

'''

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if points == [[]] or points == []:
            return 0
        
        points.sort(key = lambda x : x[1])
        pre_ending = points[0][1]
        count = 1
        
        for start, end in points[1:]:
            if start > pre_ending:
                count += 1
                pre_ending = end
        return count