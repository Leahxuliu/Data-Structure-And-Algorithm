#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/18  
# @Author  : XU Liu
# @FileName: 200.Number of Islands.py

'''
1. 题目要求：
超级热门题

2. 理解：


3. 题目类型：
2d grid map

4. 输出输入以及边界条件：
input: List[List[str]]
output: int
corner case: none grid --> 0  

5. 解题思路
    1. 矩阵搜索
    易错点，注意输入的是str！！！
    注意边界！
'''

'''
dfs
把dfs写在里面，写法会更加便捷
'''
'''
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        visited =[[0] * len(grid[0]) for _ in range(len(grid))]
        
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visited[i][j] == 0 and grid[i][j] == '1':
                    self.dfs(i, j, visited, grid)
                    island +=1
        return island
                    
    def dfs(self, i, j, visited, grid):
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[i]) - 1 or visited[i][j] == 1 or grid[i][j] == '0':
            return 
        
        visited[i][j] = 1
        self.dfs(i-1, j, visited, grid)
        self.dfs(i+1, j, visited, grid)
        self.dfs(i, j-1, visited, grid)
        self.dfs(i, j+1, visited, grid)
        return 
'''
'''
BFS
'''
from collections import deque
class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        
        queue = deque()
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    queue.append([i,j])
                    visited[i][j] = 1
                    while queue:
                        r, c = queue.popleft()
                        if r - 1 >= 0  and visited[r-1][c] == 0 and grid[r-1][c] == '1':
                            queue.append([r - 1, c])
                            visited[r - 1][c] = 1  # 必须要写，如果不写的话，会超时
                        if r + 1 <= len(grid) -1 and visited[r+1][c] == 0 and grid[r+1][c] == '1':
                            queue.append([r + 1, c])
                            visited[r + 1][c] = 1
                        if c - 1 >= 0 and visited[r][c-1] == 0 and grid[r][c-1] == '1':
                            queue.append([r, c - 1])
                            visited[r][c - 1] = 1
                        if c + 1 <= len(grid[r]) - 1 and visited[r][c+1] == 0 and grid[r][c+1] == '1':
                            queue.append([r, c + 1])
                            visited[r][c + 1] = 1
                    island += 1
                    
        return island

x = Solution()
print(x.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))