# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/04  
# @Author  : XU Liu
# @FileName: 322.Coin Change.py

'''
1. 题目类型：
    DP

2. 题目要求与理解：
    找零钱

3. 解题思路：




'''


'''
暴力递归
Time Limit Exceeded
不太理解
'''

class Solution:
    def coinChange(self, coins, amount):
        #res = float('inf') 错误
        
        def dfs(n):
            if n == 0:
                return 0
            if n < 0:
                res = -1
                return res

            res = float('inf')  # 不太理解 为什么要写在里面，不能写在函数外面
            for i in coins:
                sub = dfs(n-i)
                if sub > -1:  # 易遗忘
                    res = min(dfs(n-i) + 1, res)
            
            if res != float('inf'):
                return res
            else:
                return -1
        
        return dfs(amount)

X = Solution()
print(X.coinChange([1,2,5],6))


'''
递归 + memo
'''

class Solution:
    def coinChange2(self, coins, amount):
        memo = {}
        
        def dfs(n):
            if n in memo:
                return memo[n]
            if n < 0:
                return -1
            if n == 0:
                return 0
            
            memo[n] = float('inf')
                
            for i in coins:
                sub = dfs(n - i)
                if sub > -1:
                    memo[n] = min(memo[n], sub + 1)
            if memo[n] == float('inf'):
                return -1
            else:
                return memo[n]
        return dfs(amount)
        

'''
dp + table
'''
class Solution2:
    def coinChange2(self, coins, amount):
        if amount == 0:
            return 0
        
        dp = [float('inf')] * (amount + 1)  # 容易写错 写成[inf, inf, inf.....]
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
                    
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]

X = Solution2()
print(X.coinChange2([1,2,5],11))
