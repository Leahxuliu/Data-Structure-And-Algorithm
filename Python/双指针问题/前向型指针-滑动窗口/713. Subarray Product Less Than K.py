#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/07/02

'''
sliding window

1. set i, j start at 0, 0 and create a res(int) to count the subarray
2. caluculate K,   K *= nums[j]
3. if K < k, res += j - i + 1
   if K >= k, K / nums[i] and move i 

10, 5, 2, 6
i
       j
'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if nums == []:
            return 0
        
        i = 0
        res = 0
        K = 1
        for j in range(len(nums)):
            K *= nums[j]
            
            while K >= k and i <= j:
                K /= nums[i]
                i += 1
            
            res += j - i + 1
        return res