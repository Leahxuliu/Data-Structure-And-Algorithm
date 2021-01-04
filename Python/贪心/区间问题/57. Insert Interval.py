#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/21


# 同56
# 时间复杂度 O(nlogn)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x:x[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            temp = res[-1][1]
            if start <= temp:
                res[-1][1] = max(end, temp)
            else:
                res.append([start, end])
        return res


'''
优化 区间的排序部分

greedy
1. 在区间 newInterval 之前开始的区间全部添加到输出中
2. 将 newInterval 添加到输出中
3. 然后一个个添加后续的区间，如果重合则合并它们。


'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []:
            return [newInterval]
        
        res = []
        n = 0
        # 把start小于newstart的interval放入到res里
        for i, (s, e) in enumerate(intervals):
            if s < newInterval[0]:
                res.append([s, e])
            else:
                n = i
                break
        
        # 插入newInterval
        if not res or res[-1][1] < newInterval[0]:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1], newInterval[1])
        
        # 插入剩下的intervals
        for i, (s, e) in enumerate(intervals[n:]):
            pre_e = res[-1][1]
            if s <= pre_e:
                res[-1][1] = max(pre_e, e)
            else:
                res.append([s, e])
        
        return res