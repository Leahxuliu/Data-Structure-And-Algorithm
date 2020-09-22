# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/25

'''
Method - Greedy
Steps:
    1. sort intervals based on start time (在担心下午的会议之前，先担心的是上午的会议，和日常思维模式一样，按start排序)
    2. use stack to store Meeting end time of the meeting now
    3. compare intervals[i][0] with endings of stack (本meeting开始点与前一个状态下正在开会的endings做比较
)
        if start < endings from stack, temp.append(end)
        temp.append(intervals[i][1])
    4. renew res, res = max(res, len(temp))
       renew stack, stack = temp
Time: O(NlogN)
Space:O(N)  
'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if intervals == [] or intervals == [[]]:
            return 0

        intervals.sort(key = lambda x:x[0])
        res = 0
        stack = []
        temp = []

        for start, end in intervals:
            temp.append(end)
            for i in stack:
                if start < i:
                    temp.append(i)
            res = max(res, len(temp))
            stack = temp
            temp = []
        return res