'''
62
无障碍
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[-1][-1]

# 空间优化
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        dp = [1] * n 

        for i in range(1, m):
            pre = dp
            for j in range(1, n):
                dp[j] = pre[j] + dp[j - 1]
        
        return dp[-1]


'''
63
有障碍物
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        if j == 0:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]