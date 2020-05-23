#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/20

'''
Method
1. Sort intervals by start (ascending)
2. append first interval into res
3. scan intervals[1:]
   compare this interval's start with the last interval's end in res
   if curr start < last end, to find max end, then renew end
   eles, append into res
4. return res

Time: O(nlogn + n)
Space:O(1)
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == [] or intervals == [[]]:
            return []
        
        intervals.sort(key = lambda x:x[0])
        res = []
        res.append(intervals[0])
        
        for start, end in intervals[1:]:
            last = res[-1][1]
            
            if start <= last:
                res[-1][1] = max(last, end)
            
            else:
                res.append([start, end])
        return res
            