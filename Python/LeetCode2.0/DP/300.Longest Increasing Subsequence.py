#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/09

'''
input: nums: list[int]; the number of nums is from 0 to inf
output: int, the number of LIS
corner case: nums == [] → 0

Method - DP 
dp[i]: the most number of LIS from nums[0] to nums[i]
Steps:
    1. build dp list, the dp size is n, the n is the length of nums
    2. scan dp list, return max(dp)
        Traversing direction： 
         for i in range(1, n):
            for j in range(r):
    3. compare nums[i] and nums[j]
        dp[i] = max(dp[i], dp[j] + 1), nums[i] > nums[j]

        base case: 
        dp[0] = 1

Time complexity : O(n**2)
Space complexity : O(n)
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        