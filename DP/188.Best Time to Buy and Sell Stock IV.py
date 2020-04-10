# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/10  
# @Author  : XU Liu
# @FileName: 188.Best Time to Buy and Sell Stock IV.py



'''
k是指定次数
0：还没有操作
1-k：操作k次

# 状态转移方程
i start at day1
dp[i][k][0] = max(rest,  sell)
            = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(rest,  buy)
            = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

# base
0 means before day1
dp[0][k][0] = 0
dp[0][k][1] = -inf  # does not exist
dp[i][0][0] = 0
dp[i][0][1] = -inf  # does not exist
'''


'''
Time Limit Exceeded
'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if prices == []:
            return 0

        n = len(prices)
        dp = [[[-float('inf'), -float('inf')] for _ in range(k + 1)] for _ in range(n+1)]  # 易写错
        
        for i in range(0, n+1):
            for k in range(0, k+1):
                if i == 0:
                    dp[0][k][0] = 0
                elif k == 0:
                    dp[i][0][0] = 0
                else:
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i-1])
                    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i-1])
                    
        return dp[n][k][0]
        



'''
一次交易由买入和卖出构成，至少需要两天。所以说有效的限制 k 应该不超过 n/2，如果超过，就没有约束作用了，
相当于 k = +infinity。这种情况是之前解决过的
'''

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def maxProfit1(prices):
            if prices == []:
                return 0

            n = len(prices)
            dp_0 = 0
            dp_1 = float('-inf')

            for i in range(n):
                dp_0 = max(dp_0, dp_1 + prices[i])
                dp_1 = max(dp_1, dp_0 - prices[i])
            return dp_0
        
        def maxProfit2(k, prices):
            n = len(prices)
            dp = [[[-float('inf'), -float('inf')] for _ in range(k + 1)] for _ in range(n+1)]  # 易写错

            for i in range(0, n+1):
                for k in range(0, k+1):
                    if i == 0:
                        dp[0][k][0] = 0
                    elif k == 0:
                        dp[i][0][0] = 0
                    else:
                        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i-1])
                        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i-1])

            return dp[n][k][0]
        
        if prices == [] or k ==0:
            return 0
        
        if k > len(prices) //2:
            res = maxProfit1(prices)
        else:
            res = maxProfit2(k, prices)
        return res
            
        
        
        
        
        
        
        
        
        
       