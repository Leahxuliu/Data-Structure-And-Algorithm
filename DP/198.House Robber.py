# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/10  
# @Author  : XU Liu
# @FileName: 198.House Robber.py

'''
dp[i]: i个数字时， 最大和

# 状态转移方程
dp[i] = max(choose nums[i],  not choose nums[i])
      = max(dp[i-2] + nums[i], dp[i-1])
      
# basecase
dp[0] = 0
dp[1] = nums[0]
dp[2] = nums[1]  # 错误！！！
订正：
dp[2] = max(nums[0], nums[1])

'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == None:
            return 0
        
        n = len(nums)
        dp = [0] * (n + 1)
        
        for i in range(1, n+1):
            if i == 1:
                dp[i] = nums[i-1]
            elif i == 2:
                dp[i] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
        return dp[n]


'''
减成1维
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        n = len(nums)
        dp_i = nums[0]
        dp_i2 = nums[0]
        
        for i in range(1, n):
            if i == 1:
                dp_i = max(nums[0], nums[1])
            else:
                temp = dp_i
                dp_i = max(dp_i2 + nums[i], dp_i)
                dp_i2 = temp
        return dp_i