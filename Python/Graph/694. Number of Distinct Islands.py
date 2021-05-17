# DFS

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def DFS(si, sj, i, j):
            if i >= n or i < 0 or j >= m or j < 0 or visited[i][j] == 1 or grid[i][j] == 0:
                return 
            
            visited[i][j] = 1
            self.path.append((i - si, j - sj))
            for newi, newj in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                DFS(si, sj, newi, newj)
            return 

        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for _ in range(n)]
        all_res = set()

        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    self.path = []
                    DFS(i, j, i, j)
                    all_res.add(tuple(self.path))
        return len(all_res)

# BFS
