'''
329
给定一个二维数组，求数组中最长的连续下降路径的长度


本题相当于无环有向图，找最长路径，且带有memo，所以可以不用visited

'''

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if matrix == [] or matrix == [[]]:
            return 0
        
        def find(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
                        
            # visited[i][j] = 1

            res = 1
            for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
                    continue
                # if visited[x][y] == 1:
                    # continue
                if matrix[i][j] < matrix[x][y]:
                    res = max(res, find(x, y) + 1)  # 是本点为起始点时的最长，所以find(xxx)+1而不是+len（path）

            # visited[i][j] = 0

            memo[(i, j)] = res
            return res

        m = len(matrix)
        n = len(matrix[0])

        # visited = [[0] * n for _ in range(m)]
        memo = {}
        self.res = 1
        
        # find(2, 1, [])

        for i in range(m):
            for j in range(n):
                # find the longest path start at [i, j]
                self.res = max(self.res, find(i, j))
        
        return self.res

