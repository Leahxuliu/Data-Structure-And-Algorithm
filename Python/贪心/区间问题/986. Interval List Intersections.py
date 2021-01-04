#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/21

'''
Method - two pointers
Steps:
    1. set i, j  start at A[0], B[0]
    2. find intersection, start1 <= end2 and start2 <= end1
    3. move pointers (难点)
    
Time: O(N)
Space: O(1)
'''


# 分3种情况，一前一后，有交集（pointer移动end在前的），一后一前

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if A == [] or B == []:
            return []
        
        i = 0
        j = 0
        res = []

        while i < len(A) and j < len(B):
            s1, e1 = A[i]
            s2, e2 = B[j]

            # A前 B后 无交集
            if e1 < s2:
                i += 1
            
            # 有交集（pointer移动end在前的）
            elif e1 >= s2 and s1 <= e2:
                res.append([max(s1, s2), min(e1, e2)])
                if e1 < e2:
                    i += 1
                elif e1 > e2:
                    j += 1
                else:
                    i += 1
                    j += 1
            
            # A后 B前 无交集
            else:
                j += 1
        
        return res


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        n = len(A)
        m = len(B)
        
        if n == 0 or m == 0:
            return []
        
        i, j = 0, 0
        res = []
        
        while i < n and j < m:
            a1, a2 = A[i][0], A[i][1]
            b1, b2 = B[j][0], B[j][1]
            
            # find intersection
            if a1 <= b2 and b1 <= a2:
                res.append([max(a1, b1), min(a2, b2)])
            
            # move pointer
            if b2 < a2:  # A[i]与B[j]的头比完，接下来还有B[j]的尾巴还没有比，所以以B[j]尾巴为基准
                j += 1
            else:
                i += 1
        return res
                