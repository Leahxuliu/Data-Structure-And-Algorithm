#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/18  
# @Author  : XU Liu
# @FileName: 矩阵搜索_BFS.py

class MySolution:
    def main(self, grid):
        if not grid:  # corner case
            return None
        if len(grid) == 1:
            return
        
        # build empty visited with the same size as grid
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        from collections import deque
        
        for i in range(len(grid)):
            for j in range(len(gird[i])):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    queue.append([i, j])  # 0行0列
                    visited[i][j] = 1
                    while queue:
                        r, c = queue.popleft()  # row 行, cloumn 列
                        if r - 1 >= 0 and visited[r - 1][c] == 0:
                            queue.append([r - 1, c])  # 向上走一格
                            visited[r - 1][c] = 1
                        if r + 1 <= len(grid) - 1 and visited[r + 1][c] == 0:
                            queue.append([r + 1, c])  # 向下走一格
                            visited[r + 1][c] = 1
                        if c - 1 >= 0 and visited[r][c - 1] == 0:
                            queue.append([r, c - 1])  # 向右走一格
                            visited[r][c - 1] = 1
                        if c + 1 <= len(grid[0]) - 1 and visited[r][c + 1] == 0:
                            queue.append([r, c + 1])  # 向左走一格
                            visited[r][c + 1] = 1
        return