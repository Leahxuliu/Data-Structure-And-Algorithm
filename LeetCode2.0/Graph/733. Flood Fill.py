#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/20

'''
Method - BFS
Steps:
    1. build visited, the size of visited is same as image
    2. scan vetexs by using bfs, start at [sr][sc] and visited the neighbors
        if visited[i][j] == 0 and image[i][j] == 1, add the vetex into queue, and renew color
'''
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        
        if m == 0 or n == 0:
            return 
        
        visited = [[0] * n for _ in range(m)]
        queue = deque()
        
        
        queue.append([sr, sc])
        visited[sr][sc] = 1
        color = image[sr][sc]
        image[sr][sc] = newColor

        while queue:
            r, c = queue.popleft()
            
            for x, y in [[r - 1, c], [r + 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= x <= m - 1 and 0 <= y <= n - 1 and image[x][y] == color and visited[x][y] == 0:
                    visited[x][y] = 1
                    image[x][y] = newColor
                    queue.append([x, y])
    
        return image