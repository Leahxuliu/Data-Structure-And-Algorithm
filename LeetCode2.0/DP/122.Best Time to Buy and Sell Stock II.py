'''
Method - DP
dp[i][0]: the most profit, when in day i and dont have stock
dp[i][i]: the most profit, when in day i and have stock

Steps:
    1. build a dp table, the table size is (the number of days + 1) * 2
    2. scan dp table from left to right
        dp[i][0] = max(sell, rest) = max(dp[i - 1][1] + prices[i - 1], dp[i - 1][0])
        dp[i][1] = max(buy, rest)  = max(dp[i - 1][0] - prices[i - 1], dp[i - 1][1])
        base case:
            dp[0][0] = 0
            dp[0][1] = -inf
    3. retrun dp[n][0]
Time: O(N)
Space:O(2N)


Optimal solution:
    1. dp_i_0 = 0
       dp_i_1 = -prices[0]
    2. renew them
        dp_i_0, dp_i_1 = max(dp_i_1 + prices[i], dp_i_0), max(dp_i_1, dp_i_0 - prices[i])
Time: O(N)
Space:O(2)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        if n == 0:
            return 0
        
        dp = [[-float(inf)] * 2 for _ in range(n + 1)]
        dp[0][0] = 0
        
        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1][1] + prices[i - 1], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][0] - prices[i - 1], dp[i - 1][1])
        
        return dp[n][0]
            

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        if n == 0:
            return 0
        
        dp_i_0 = 0
        dp_i_1 = -float('inf')
        
        for i in range(n):
            dp_i_0 = max(dp_i_1 + prices[i], dp_i_0)
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        
        return dp_i_0