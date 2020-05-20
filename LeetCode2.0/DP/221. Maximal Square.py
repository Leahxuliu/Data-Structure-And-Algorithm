'''
Method - DP
dp[i][j]: the largest square in [0][0] --> [i][j]
Steps:
    1. build a dp table, the size of table is len(matrix) * len(matrix[0])
    2. scan dp table from left to right and up to down
       dp[i][j] = min(dp[i-1][j],dp[i−1][j−1],dp[i][j−1])+1, matrix[i][j] == '1'
       
       base case:
            dp[i][0] = 1, matrix[i][0] == '1'
            dp[0][j] = 1, matrix[0][j] == '1'
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == [[]] or matrix == []:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0] * n for _ in range(m)]
        
        max_res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0:
                        dp[i][j] = 1
                    elif j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_res = max(max_res, dp[i][j])
        return max_res * max_res