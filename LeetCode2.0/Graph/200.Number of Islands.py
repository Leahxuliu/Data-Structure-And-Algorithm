#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/06 

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == [[]] or grid == []:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]
        
        queue = deque()
        numb = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and grid[i][j] == '1':
                    queue.append([i,j])
                    visited[i][j] = 1
                    numb += 1
                    
                    while queue:
                        x, y = queue.popleft()
                        if x + 1 < m and visited[x + 1][y] == 0 and grid[x + 1][y] == '1':
                            queue.append([x + 1, y])
                            visited[x + 1][y] = 1
                        if x - 1 >= 0 and visited[x - 1][y] == 0 and grid[x - 1][y] == '1':  # x - 1 >= 0 不能忘
                            queue.append([x - 1, y])
                            visited[x - 1][y] = 1
                        if y + 1 < n and visited[x][y + 1] == 0 and grid[x][y + 1] == '1':
                            queue.append([x, y + 1])
                            visited[x][y + 1] = 1
                        if y - 1 >= 0 and visited[x][y - 1] == 0 and grid[x][y - 1] == '1':
                            queue.append([x, y - 1])
                            visited[x][y - 1] = 1
        return numb

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == [] or grid == [[]]:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        visited = [[0] * n for _ in range(m)]
        
        def dfs(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or visited[i][j] == 1 or grid[i][j] == '0':
                return 
            
            visited[i][j] = 1
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        numb = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and grid[i][j] == '1':
                    dfs(i, j)
                    numb += 1
        return numb