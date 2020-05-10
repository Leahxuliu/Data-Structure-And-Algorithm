#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/11

'''
Method - DP
DP[i]: minimum number of coins when amount is i
Steps:
    1.build a dp list, the list size is amount + 1; 0,1,2,....amount
    2.scan list from 1 to amount
        dp[i] = min(choose the coin, don’t)
                = min(dp[i], dp[i - coin] + 1, coin < i)
        base case:
            dp[0] = 0
            initial value：inf
    3.if dp[amount] == inf, return -1,else return dp[amount]

Time: O(MN), M is amount, N is the number of coins
Space: O(M)

'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if coins == []:
            return -1
        
        dp = [float(inf)] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        if dp[amount] == float(inf):
            return -1
        else:
            return dp[amount]
            