#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/23

'''
Method - Greedy
Steps:
    1. sort g and s
    2. set i, j start at 0, 0
    3. if g[i] <= s[j], res += 1, i += 1, j += 1
        else, j += 1

Time: O(N)
Space: O(1)
'''


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if s == []:
            return 0
        
        g.sort()
        s.sort()

        n, m = len(g), len(s)
        i, j = 0, 0
        res = 0

        while i < n and j < m:
            if g[i] <= s[j]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        return res
