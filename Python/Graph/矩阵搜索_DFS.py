#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/18  
# @Author  : XU Liu
# @FileName: 矩阵搜索_DFS.py

class MySolution:
    def main(self, grid):
        if not grid:  # corner case
            return None
        if len(grid) == 1:
            return
        
        # build empty visited with the same size as grid
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        # visited =[[0] * len(grid[0]) for _ in range(len(grid))] --> [[0], [0], [0], [0]]
        
        # scan grid and dfs the island node
        for i in range(len(grid)):  # len(grid) = 行数
            for j in range(len(gird[i])):  # len(gird[i]) = 每行里面的个数
                if grid[i][j] == 1 and visited[i][j] == 0:
                    self.dfs(i, j, visited, grid)
        return
        
    def dfs(self, i, j, visited, grid):  # i: 行; j: 列
        if i < 0 or j <0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or visited[i][j] == 1:  # 结束条件
            return

        # set visited
        visited[i][j] = 1
        self.dfs(i - 1, j, visited, grid)  # 上走一格
        self.dfs(i + 1, j, visited, grid)  # 下走一格
        self.dfs(i, j - 1, visited, grid)  # 左走一格
        self.dfs(i, j + 1, visited, grid)  # 右走一格
