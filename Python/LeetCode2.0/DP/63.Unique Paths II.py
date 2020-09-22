'''
Method - DP
dp[i][j]: the number of paths from [0][0] to [i][j]
Steps:
    1. build a dp table, the table size is m * n
    2. scan [0][0] to [m-1][n-1]
        if grid[i][j] is 0:
            dp[i][j] = from left + from up
                     = dp[i][j - 1] + dp[i - 1][j]
        if grid[i][j] == 1:
            dp[i][j] = 0
        
        base case:
            if grid[0][0] == 0, dp[0][0] = 1
            else, dp[0][0] == 0
            dp[i][0] = dp[i - 1][0]
            dp[0][j] = dp[0][j]

time complexity: O(nm)
space:O(mn)
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid == [] or obstacleGrid == [[]]:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    if obstacleGrid[0][0] == 0:
                        dp[0][0] = 1
                elif i == 0 and obstacleGrid[i][j] == 0:
                    dp[0][j] = dp[0][j - 1]
                elif j == 0 and obstacleGrid[i][j] == 0:
                    dp[i][0] = dp[i - 1][0]
                elif obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]