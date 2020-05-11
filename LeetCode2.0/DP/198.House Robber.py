#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/11
'''
198
maximum sum of non-adjacent numbers


Method - DP
DP[i]: the maximum sum for nums[0:i+1]
Steps:
    1. build a dp list, the dp size is equal to the number of nums(n) 
    2. scan dp list from 0 to n-1
        dp[i] = max(choose this one, not)
               =max(dp[i-2] + nums[i], dp[i - 1])
        base case:
            dp[0] = nums[0]
            initial value is 0

'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        n = len(nums)
        dp = [0] * n
        
        for i in range(n):
            if i == 0:
                dp[0] = nums[0]
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[n - 1]