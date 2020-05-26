# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/25

'''
Method - DP
dp[i][k][0]: most profit in day i, transaction most k times, no stock
dp[i][k][1]: most profit in day i, transaction most k times, have stock
注意，这里的k不一定是每一次都交易的，可以有k + 1时，其实并没有进行实质的交易

Steps:
    1. build dp table, the table size is (day + 1) * (3) * (2)
    2. scan dp table
    3. dp[i][k][0] = max(rest, sell) = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i - 1])
       dp[i][k][1] = max(rest, buy) = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i - 1])
       base case:
        dp[0][k][0] = 0
        dp[0][k][1] = -inf
        dp[i][0][0] = 0
        dp[i][0][1] = -inf


Optimal
# 状态转移方程式
dp_1_0 = max(dp_1_0, dp_1_1 + i)
dp_1_1 = max(dp_i11, -i)
dp_2_0 = max(dp_i20, dp_i21 + i)
dp_2_1 = max(dp_i21, dp_i10 - i)


# base
dp_i10 = 0
dp_i20 = 0
dp_i11 = float('-inf')
dp_i21 = float('-inf')

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0

        n = len(prices)
        dp = [[[float('-inf')] * 2 for _ in range(2 + 1)] for _ in range(n+1)]

        for i in range(0, n + 1):
            for k in range(0, 2 + 1):
                if i == 0:
                    dp[0][k][0] = 0
                elif k == 0:
                    dp[i][0][0] = 0
                else:
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i-1])
                    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i-1])
        print(dp)
        return dp[n][2][0]