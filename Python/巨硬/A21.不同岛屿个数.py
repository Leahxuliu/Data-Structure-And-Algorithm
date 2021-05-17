'''
694. Number of Distinct Islands

不同岛屿个数
核心：
左上角是固定不变的
与左上角的差值是path
'''

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if grid == [] or grid == [[]]:
            return 0
        
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        def find(i, j, prei, prej):
            # 左上角，即起始点是不变的！！！
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 
            if visited[i][j] == 1 or grid[i][j] == 0:
                return

            visited[i][j] = 1
            path.append(str(i - prei) + str(j - prej))
            for (x, y) in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                find(x, y, prei, prej)

            return 
        

        all_path = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    path = []
                    find(i, j, i, j)
                    all_path.add(''.join(path))
        return len(all_path)
