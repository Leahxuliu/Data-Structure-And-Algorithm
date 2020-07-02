# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/05  
# @Author  : XU Liu
# @FileName: 435.Non-overlapping Intervals.py

'''
1. 题目要求：
Given a collection of intervals, 
find the minimum number of intervals you need to 
remove to make the rest of the intervals non-overlapping.

2. 理解：
移除几个list，使得剩下的list区间内没有overlap
尽可能移除少
比如[[1,2],[2,3],[3,4],[1,3]]
1-2 2-3 3-4 1-3
1-3 overlap

3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    
5. 空间时间复杂度

'''

'''
Greedy - sort and compare the first end with other start to delete
    Method:
        1. corner case
        2. based on the second value to sort the input in increasing order
            [1,2], [1,3], [2,3], [3,4]
        3. choose the first elem of list, compare its second value with other interval first value, 
            if first > the second value, count the number and renew index
            choose [1, 2]
                take 2, compare it with next 1 of [1,3], 2 > 1, so count = 1, index = 1
                take 2, compare it with next 2 of [2, 3], 2 == 2,so count = 1, index = 2
            choose interval[index = 2] = [2,3]
                take 3 compare it with next 3 o f[3, 4], 3 == 3, so count = 1, index = 3
            index = len(interval) - 1, return count
        4. repeat 3, until index out of list range
        5. return counted number
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if intervals == [] or intervals == []:
            return 0
        
        n = len(intervals)
        intervals.sort(key = lambda x : x[1])  # 为什么用end排序？？？
        pre_ending = intervals[0][1]
        
        count = 1
        
        for start, end in intervals[1:]:
            if start >= pre_ending:
                count += 1
                pre_ending = end
        return n - count

# 类似merge的写法
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if intervals == [[]] or intervals == []:
            return 0
        
        intervals.sort(key = lambda x:x[1])
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            pre_end = res[-1][1]
            if start < pre_end:
                pass
            else:
                res.append([start, end])
        return len(intervals) - len(res)