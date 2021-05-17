class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if grid == [[]] or grid == []:
            return 0
        
        def traversal(i, j):
            nonlocal res 
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                res += 1
                return 
            if grid[i][j] == 0:
                res += 1
                return 
            if grid[i][j] == 2:
                return 
            
            grid[i][j] = 2
            for x, y in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
                traversal(x, y)
            return 
        
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    traversal(i, j)
        return res        