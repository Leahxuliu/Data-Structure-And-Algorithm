# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/05  
# @Author  : XU Liu
# @FileName: 435.Non-overlapping Intervals.py



class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if intervals == [] or intervals == [[]]:
            return 0
        
        intervals = sorted(intervals, key = lambda x:x[1])

        pre_end = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if start < pre_end:
                res += 1
            else:
                pre_end = end
        return res

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