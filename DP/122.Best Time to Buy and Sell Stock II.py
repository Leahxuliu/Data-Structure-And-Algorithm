# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/08  
# @Author  : XU Liu
# @FileName: 122.Best Time to Buy and Sell Stock II.py


'''
k是任意次数，所以不需要记录k这个状态
# 状态转移方程式
dp[i][0] = max(选继续观望， 选卖掉股票)
         = max(dp[i-1][0], dp[i-1][1] + price(i))

dp[i][1] = max(选继续持股， 选买入股票)
         = max(dp[i-1][1], dp[i-1][0] - price[i])  # 121题与122题的区别

# base
dp[0][0] = 0
    # 第0天，还没有持股
dp[0][1] = -infinity
    # 用无穷大表示不可能存在

'''


class Stock:
    def maxProfit(self, prices):
        if prices == []:
            return 0
        
        n = len(prices)
        dp_0 = 0
        dp_1 = float('-inf')

        for i in range(n):
            dp_0 = max(dp_0, dp_1 + prices[i])
            dp_1 = max(dp_1, dp_0 - prices[i])
        return dp_0