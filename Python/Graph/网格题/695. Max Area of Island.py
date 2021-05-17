class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid == [] or grid == [[]]:
            return 0
        
        def traversal(i, j):
            if grid[i][j] == 0:
                return 
            
            grid[i][j] = 0
            self.count += 1

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                    if grid[x][y] == 1:
                        traversal(x, y)
            return 
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.count = 0
                    traversal(i, j)
                    res = max(res, self.count)
        return res



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid == [] or grid == [[]]:
            return 0
        
        def traversal(i, j):
            if grid[i][j] == 0:
                return 
            
            grid[i][j] = 0
            res = 1
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                    if grid[x][y] == 1:
                        res += traversal(x, y)
            return res
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # self.count = 0
                    res = max(res, traversal(i, j))
        return res