# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/05  
# @Author  : XU Liu
# @FileName: 253.Meeting Rooms II.py

'''
1. 题目要求：
至少需要几个会议室

2. 理解：
区间问题

3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
Greedy
    1. sort the list by the elements[0] (meeting start)
    2. 当前区间下，需要几个room
    3. 本meeting开始点与前一个状态下正在开会的endings做比较

    
5. 空间时间复杂度

'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if intervals == [[]] or intervals == []:
            return 0
        
        intervals.sort(key = lambda x:x[0])
        temp = []  # 目前正在开会的endings，含本meeting
        stack = []  # 这个meeting之前，在开会的ending
        res = 0
        
        for start, end in intervals:
            temp.append(end)
            for i in stack:
                if start < i:
                    temp.append(i)
            res = max(len(temp), res)
            stack = temp
            temp = []
        
        return res


# heap + greedy
# heap里面放现在正在使用的会议室的结束时间
# 新会议开始的时候，是否有老的会议已经结束
from heapq import heappop, heappush
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return len(intervals)
        
        intervals = sorted(intervals, key = lambda x:x[0])
        heap = [intervals[0][1]]
        res = 1
        for start, end in intervals[1:]:
 
            while heap and heap[0] <= start:  # 要=
                heappop(heap)
            heappush(heap, end)       

            res = max(res, len(heap))
        return res
