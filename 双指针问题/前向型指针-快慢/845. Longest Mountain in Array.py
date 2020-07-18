#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/07/02


'''
two pointer
0. use for loop to scan the A
1. find the peak, A[i - 1] < A[i] < A[i + 1], i is the peak
2. set l, r pointers at i-1 and i+1, and set res = 0
3. if A[l] < A[l+1] move l
   until l < 0 or A[l-1] >= A[l]
4. if A[r] < A[r - 1] move r
   until r = len(A) or A[r] >= A[r+1]
5. mountaion: r - l - 1
6. repeat step1 to step5, find the longest

 0  1  2  3  4  5  6
 2, 1, 4, 7, 3, 2, 5
          i
 l                 r
 
 6 -0-1 = 5
 
 
   0  1  2
   2, 1, 2
 l    i    r
 
3-(-1) -1
'''

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        
        res = 0
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] and A[i] > A[i + 1]:
                l = i - 1
                r = i + 1
                
                while l >= 0 and A[l] < A[l + 1]:
                    l -= 1
                while r < len(A) and A[r] < A[r - 1]:
                    r += 1
                res = max(res, (r - l - 1))
        return res