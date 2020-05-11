#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/11

'''
Method - DP
dp[i][0 or 1]: the profit in day i; 0 is no stock, 1 means that have stock

Steps:
    1. build dp table; the dp table size is (the number of prices + 1) * 2
    2. dp[i][0] = max(sell, rest) = max(dp[i-1][1] + price[i - 1], dp[i-1][0])
       dp[i][1] = max(buy, rest) = max( - price[i - 1], dp[i - 1][1])
       base case: 
        dp[0][0] = 0
        dp[0][1] = -float(inf)
    3. return dp[n][0]
    
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:  # corner case
            return 0
        
        dp = [[-float(inf)] * 2 for _ in range(n + 1)]
        
        dp[0][0] = 0
        
        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1][1] + prices[i - 1], dp[i - 1][0])
            dp[i][1] = max(- prices[i - 1], dp[i - 1][1])
        return dp[n][0]