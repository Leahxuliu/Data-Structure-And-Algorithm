#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/09 


# BFS
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        visited = [0] * N
        queue = deque()
        
        queue.append(0)
        visited[0] = 1

        while queue:
            vertex = queue.popleft()
            for out in rooms[vertex]:
                if visited[out] == 0:
                    queue.append(out)
                    visited[out] = 1
        if 0 in visited:
            return False
        else:
            return True

# DFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        visited = [0] * N
        
        def dfs(index):
            if visited[index] == 1:
                return 
            
            visited[index] = 1
            for out in rooms[index]:
                dfs(out)
                
        dfs(0)
        if 0 in visited:
            return False
        else:
            return True