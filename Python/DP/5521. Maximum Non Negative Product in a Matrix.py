'''
dp[i][j][0]到(i,j)的最小累乘值
dp[i][j][1]到(i,j)的最大累乘值

if grid[i][j] > 0:
    dp[i][j][1] = grid[i][j] * max(dp[i-1][j][1],dp[i][j-1][1])
    dp[i][j][0] = grid[i][j] * min(dp[i-1][j][0],dp[i][j-1][0])
else:
    dp[i][j][1] = grid[i][j] * min(dp[i-1][j][0],dp[i][j-1][0])
    dp[i][j][0] = grid[i][j] * max(dp[i-1][j][1],dp[i][j-1][1])

if i == 0 and j == 0:
    dp[i][j][0] = grid[i][j]
    dp[i][j][1] = grid[i][j]
elif i == 0:
    dp[i][j][0] = dp[i][j - 1][0] * grid[i][j]
    dp[i][j][1] = dp[i][j - 1][1] * grid[i][j]
elif j == 0:
    dp[i][j][0] = dp[i - 1][j][0] * grid[i][j]
    dp[i][j][1] = dp[i - 1][j][1] * grid[i][j]

'''

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[[float(inf), float(-inf)] for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j][0] = grid[i][j]
                    dp[i][j][1] = grid[i][j]
                elif i == 0:
                    dp[i][j][0] = dp[i][j - 1][0] * grid[i][j]
                    dp[i][j][1] = dp[i][j - 1][1] * grid[i][j]
                elif j == 0:
                    dp[i][j][0] = dp[i - 1][j][0] * grid[i][j]
                    dp[i][j][1] = dp[i - 1][j][1] * grid[i][j]
                else:
                    if grid[i][j] > 0:
                        dp[i][j][1] = grid[i][j] * max(dp[i-1][j][1],dp[i][j-1][1])
                        dp[i][j][0] = grid[i][j] * min(dp[i-1][j][0],dp[i][j-1][0])
                    else:
                        dp[i][j][1] = grid[i][j] * min(dp[i-1][j][0],dp[i][j-1][0])
                        dp[i][j][0] = grid[i][j] * max(dp[i-1][j][1],dp[i][j-1][1])
        
        return dp[m - 1][n - 1][1] % (10 ** 9 + 7) if dp[m - 1][n - 1][1] >=0 else -1