#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/25

'''
Method
Steps:
    1. sort intervals based on interval[0]
    2. append intervals[0] into res
    3. traverse intervals[1:] (start, end)
    4. compare start with res[-1][1]
        if start <= res[-1][1], res[-1][1] = max(end, res[-1][1])  包括相等
        else, append [start, end] into res
    5. return res
Time: O(nlogn)
Space: O(n)
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == [] or intervals == [[]]:
            return []

        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            pre_end = res[-1][1]
            if start <= pre_end:
                res[-1][1] = max(pre_end, end)
            else:
                res.append([start, end])
        
        return res