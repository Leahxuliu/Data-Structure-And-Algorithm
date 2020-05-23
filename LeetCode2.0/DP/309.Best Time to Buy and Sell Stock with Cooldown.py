#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/23

'''
Method - DP
dp[i][0]: the most profit in day i, no stock
dp[i][1]: the most profit in day i, have stock

Steps:
    1. build dp table, the table size is 2 * (days + 1)
    2. scan the dp table
        dp[i][0] = max(rest, sell) = max(dp[i - 1][0], dp[i - 1][1] + price[i - 1])
        dp[i][1] = max(rest, buy) = max(dp[i - 1][1], dp[i - 2][0] - price[i - 1])
        base case:
        dp[0][0] = 0
        dp[0][1] = -inf
        dp[1][1] = - prices[0] 易错
        dp[1][0] = 0

Time: O(2N)
Spcae: O(2N)

Optimal solution
二维减一维
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        dp = [[float('-inf')] * 2 for _ in range(n + 1)]
        dp[0][0] = 0
        dp[1][1] = - prices[0]
        dp[1][0] = 0

        for i in range(2, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i - 1])
        
        return dp[n][0]


# 不熟
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        dp_i_0 = 0
        dp_i_1 = float('-inf')
        pre = 0  # i - 2

        for i in range(n):
            temp = dp_i_0  # 暂存一下i-1
            if i == 0:
                dp_i_1 = -prices[i]
            else:
                dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
                dp_i_1 = max(dp_i_1, dp_pre - prices[i])
            dp_pre = temp  # 对于下一层来说就是i-2了

        return dp_i_0