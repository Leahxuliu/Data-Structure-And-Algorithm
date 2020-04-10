'''
k 任意
卖掉会有fee

# 状态转移方程
dp[i][0] = max(继续观望，  卖掉)
         = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
dp[i][1] = max(继续持股，  买入)
         = max(dp[i-1][1], dp[i-1][0] - prices[i])
         
# base
dp[0][0] = 0
dp[0][1] = - prices[0]

'''

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if prices == None:
            return 0
        
        dp_i_0 = 0
        dp_i_1 = -float('inf')
        
        for i in range(len(prices)):
            if i == 0:
                dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
            else:
                dp_i_0 = max(dp_i_0, dp_i_1 + prices[i] - fee)
                dp_i_1 = max(dp_i_1, dp_i_0 - prices[i]) 
        return dp_i_0

'''
更改base
更简单
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if prices == None:
            return 0
        
        dp_i_0 = 0
        dp_i_1 = - prices[0]
        
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i] - fee)
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i]) 
        return dp_i_0