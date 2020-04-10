# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04  
# @Author  : XU Liu
# @FileName: 309.Best Time to Buy and Sell Stock with Cooldown.py


'''
k = 任意
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

# 状态转移方程
dp[i][0] = max(继续观望，  卖掉)
         = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(继续持股，  买入)
         = max(dp[i-1][1], dp[i-2][0] - prices[i])

# base
dp[0][0] = 0
dp[0][1] = -inf
dp[1][1] = - prices[1]

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        
        n = len(prices)
        dp = [[-float('inf')] * 2 for _ in range(n+1)]
        
        dp[0][0] = 0
        
        
        for i in range(1, n + 1):
            if i == 1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
                dp[i][1] = max(dp[i-1][1], - prices[i-1])
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i-1])
        return dp[n][0]
        

'''
二维减成一维
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = float('-inf')
        dp_pre = 0  # i-2
        
        for i in range(n):
            temp = dp_i_0  # 暂存一下i-1
            if i == 0:
                dp_i_1 = max(dp_i_1, - prices[i])
            else:
                dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
                dp_i_1 = max(dp_i_1, dp_pre - prices[i])
            dp_pre = temp  # 对于下一层来说就是i-2了
            
        return dp_i_0