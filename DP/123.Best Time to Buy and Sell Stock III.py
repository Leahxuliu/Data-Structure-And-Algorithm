# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04  
# @Author  : XU Liu
# @FileName: 123.Best Time to Buy and Sell Stock III.py

'''
k == 0
没有任何交易，都是0
k == 1,2
持股或观望

# 状态转移方程式
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

# base
dp[-1][k][0] = 0
dp[-1][k][1] = -infinity
dp[i][0][0] = 0
dp[i][0][1] = -infinity

'''

class Stock:
    def maxProfit(self, prices):
        if prices == []:
            return 0

        n = len(prices)
        max_k = 2
        dp = [[[float('-inf')] * 2 for _ in range(max_k + 1)] for _ in range(n+1)]

        for i in range(0, n + 1):
            for k in range(0, max_k + 1):
                if i == 0:
                    dp[0][k][0] = 0
                elif k == 0:
                    dp[i][0][0] = 0
                else:
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i-1])
                    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i-1])
        return dp[n][max_k][0]

X = Stock()
print(X.maxProfit([3,3,5,0,0,3,1,4]))



'''
方法2
这里的k是2
可以把k的范围直接列出来

# 状态转移方程式
dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])
dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
dp[i][1][1] = max(dp[i-1][1][1], -prices[i])

# base
dp[-1][k][0] = 0
dp[-1][k][1] = -infinity
dp[i][0][0] = 0
dp[i][0][1] = -infinity
'''

class Stock:
    def maxProfit(self, prices):
        if prices == []:
            return 0
            
        n = len(prices)
        dp_i10 = 0
        dp_i20 = 0
        dp_i11 = float('-inf')
        dp_i21 = float('-inf')

        for i in prices:
            dp_i20 = max(dp_i20, dp_i21 + 1)
            dp_i21 = max(dp_i21, dp_i10 - 1)
            dp_i10 = max(dp_i10, dp_i11 + 1)
            dp_i11 = max(dp_i11, -1)

        return dp_i20