class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 注意corner case
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        res = [[1],[1,1]]
        
        for i in range(numRows - 2):
            temp = [1]
            for j in range(len(res[-1])):
                if j == 0:
                    continue
                temp.append(res[-1][j - 1] + res[-1][j])
            res.append(temp + [1])
        return res


# 优化
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        dp = [[1] * i for i in range(1, numRows + 1)]

        for i in range(2, numRows):
            for j in range(len(dp[i - 1])):
                if j == 0:
                    continue
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp