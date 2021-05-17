'''
120
120. 三角形最小路径和

   2
  3 4
 6 5 7
4 1 8 3
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle == [] or triangle == [[]]:
            return 0
        
        dp = triangle[-1]
        n = len(triangle)

        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]