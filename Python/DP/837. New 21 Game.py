'''
推荐官解视频

优化版本dp
'''

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        # corner case
        if K == 0:
            return 1.0
        
        dp = [0.0] * (K - 1 + W + 1)  # 能取到的最大值是K-1+W

        # base case
        # K 到 min(N, K - 1 + W)之间的概率是1， 超过N的概率是0
        for i in range(K, min(N, K - 1 + W) + 1):
            dp[i] = 1.0

        # K - 1
        dp[K - 1] = min(N - (K - 1), W) / W
        # K - 2开始
        for i in range(K - 2, -1, -1):
            dp[i] = dp[i + 1] - (dp[i + 1 + W] - dp[i + 1]) / W
        return dp[0]