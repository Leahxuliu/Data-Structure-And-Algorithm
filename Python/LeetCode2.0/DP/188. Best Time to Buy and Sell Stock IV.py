# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/19

'''
Method - DP
dp[i][k][0]: the most profit in day i, no stock, buy k times
dp[i][k][1]: the most profit in day i, have stock, buy k times

Steps:
    a. if k <= len(prices) // 2
        1. build dp table, the table size is (the number of days + 1) * (k + 1) * 2
        2. scan dp table from left to right, up to down
            dp[i][k][0] = max(sell, rest) = max(dp[i - 1][k][1] + prices[i - 1], dp[i - 1][k][0])
            dp[i][k][1] = max(buy, rest) = max(dp[i - 1][k - 1][0] - prices[i - 1], dp[i - 1][k][1])
            base case:
                dp[0][0][0] = 0
                # dp[0][k][0] = -float('inf') 错误
                dp[0][k][0] = 0
                dp[0][k][1] = -float('inf')
                dp[i][0][0] = 0
                dp[i][0][1] = -float('inf')
        3. return dp[n][k][0] ??
    b. if k > len(prices) // 2 --> can buy any times
        dp[i][k][0 or 1] --> dp[i][0 or 1]
        scan prices by days, renew dp_i_0 and dp_i_1
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_0 - prices[i], dp_i_1)
        base case:
            dp_i_0 = 0
            dp_i_1 = -float('inf')

'''


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        if n == 0:
            return 0
        
        res = 0
        if k > n // 2:
            res = self.profit1(prices)
        
        else:
            res = self.profit2(k, prices)
        
        return res
    
    
    def profit1(self, prices):
        dp_i_0 = 0
        dp_i_1 = -float('inf')
        
        for i in range(1, len(prices) + 1):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i - 1])
            dp_i_1 = max(dp_i_0 - prices[i - 1], dp_i_1)
        return dp_i_0
    
    def profit2(self, k, prices):
        n = len(prices)
        dp = [[[-float('inf'), -float('inf')] for _ in range(k + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            for K in range(k + 1):
                if i == 0:
                    dp[0][K][0] = 0  # 易错 dp[0][2][0]表示，白白耗去两次交易，这样才能确保最后输出dp[n][k][0]是最优
                    # dp[0][0][0] = 0， dp[0][K][0] = -inf 是错误的
                elif K == 0:
                    dp[i][0][0] = 0
                else:
                    dp[i][K][0] = max(dp[i-1][K][0], dp[i-1][K][1] + prices[i-1])
                    dp[i][K][1] = max(dp[i-1][K][1], dp[i-1][K-1][0] - prices[i-1])
        print(dp)
        return dp[n][k][0]
    
    