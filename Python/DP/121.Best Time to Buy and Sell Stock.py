# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/08  
# @Author  : XU Liu
# @FileName: 121.Best Time to Buy and Sell Stock.py

'''
n是天数，K是最多交易次数，0和1表示不持股状态和持股状态
此问题共有n * K * 2种状态
dp[i][k][0 or 1]表示当前状态下的利润

0 <= i <= n-1, 1 <= k <= K
dp[i][k][0 or 1]
比如：dp[3][2][1] 的含义就是：今天是第三天，我现在手上持有着股票，至今最多进行 2 次交易。值表示利润？
再比如 dp[2][3][0] 的含义：今天是第二天，我现在手上没有持有股票，至今最多进行 3 次交易

for i in range(n-1):
    for k in range(1, K + 1):
        for s in [0, 1]:
            dp[i][k][s] = max(buy, sell, rest)
            
最终答案是： dp[n - 1][K][0]，即最后一天，最多允许 K 次交易，最多获得多少利润
# 为什么不是 dp[n - 1][K][1]？
# 因为 [1] 代表手上还持有股票，[0] 表示手上的股票已经卖出去了，很显然后者得到的利润一定大于前者。

# 状态转移方程式
dp[i][k][0] = max(选择rest， 选择sell)
            = max(dp[i-1][k][0], dp[i-1][k][1] + price[i])
            # 今天没有股，要么就是昨天就没有股，要么就是今天sell了，利润里面增加price[i]
    
dp[i][k][1] = max(选择rest， 选择buy)
            = max(dp[i-1][k][1], dp[i-1][k-1][0] - price[i])
            # 今天有股，要么就是昨天就有股，要么就是今天buy了，利润里面减少price[i]
        
# base case
dp[-1][k][0] = 0
    # i = -1，意味着还没有开始，利润是0
dp[-1][k][1] = -infinity
    # 还没有开始的时候，是不可能持有股票，用负无穷大表示不可能 不好理解
dp[i][0][0] = 0
    # k = 0, 从未交易过
dp[i][0][1] = -infinity
    # 不允许交易的情况下，是不可能持有股票，用负无穷大表示不可能

'''

# 第一题 k = 1 只交易一次的情况
'''
K = 1, 不会发生改变，所以可以简化成dp[i][0 or 1]

# 状态转移方程式：
dp[i][0] = max(选择rest， 选择sell)
         = max(dp[i-1][0], dp[i-1][1] + price[i])
dp[i][1] = max(选择rest， 选择buy)
         = max(dp[i-1][1], dp[i-1][0] - price[i]) # 错误！！！why??? 
                                                    因为这样写表示i-1天的时候，没有持股，拥有dp[i-1][0]元的利润，再买入新股时，-price[i]; 可是只有一次买卖，i-1天的时候，没有持股也就表示没有过交易，现在的利润为0
         = max(dp[i-1][1], - price[i]) # 因为只有一次买卖，买进就表示-price

# base：
dp[0][0] = 0
    # 第0天，还没有持股
dp[0][1] = -infinity
    # 用无穷大表示不可能存在

'''

'''
dp + table
'''
class Stock:
    def maxProfit(self, prices):
        if prices == []:
            return 0
        
        n = len(prices)
        dp = [[float('-inf')] * 2 for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])  # prices[i-1]易错
            dp[i][1] = max(dp[i-1][1], - prices[i-1])  # prices[i-1]易错
        return dp[n][0]

X = Stock()
print(X.maxProfit([7,1,5,3,6,4]))


# 空间优化

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        
        n = len(prices)
        # dp = [[0] * (n + 1) for _ in range(2)]

        dp_1 = float('-inf')
        dp_0 = 0

        for i in range(1, n + 1):
            dp_0 = max(dp_0, dp_1 + prices[i - 1])
            dp_1 = max(dp_1, -prices[i - 1])
        
        return dp_0

'''
状态转移方程，新状态只和相邻的一个状态有关，其实不用整个 dp 数组，
只需要一个变量储存相邻的那个状态就足够了，这样可以把空间复杂度降到 O(1)
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
            dp_1 = max(dp_1, -prices[i])
        return dp_0

'''
递归 + memo
'''
'''class Stock:
    def maxProfit(self, prices):
        if prices == []:
            return 0

        def dfs(i):
            if 
'''

