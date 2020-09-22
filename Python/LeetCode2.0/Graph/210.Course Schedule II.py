#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/08 



# Topo
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        
        indegree = [0] * numCourses
        outdegree = [[] for _ in range(numCourses)]
        
        for x, y in prerequisites:
            indegree[x] += 1
            outdegree[y].append(x)
        
        queue = deque()
        res = []
        for i, v in enumerate(indegree):
            if v == 0:
                queue.append(i)
        while queue:
            index = queue.popleft()
            res.append(index)
            for out in outdegree[index]:
                indegree[out] -= 1
                if indegree[out] == 0:
                    queue.append(out)
                    
        if indegree == [0] * numCourses:
            return res
        else:
            return []


# DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        
        visited = [-1] * numCourses
        graph = [[] for _ in range(numCourses)]
        
        for x, y in prerequisites:
            graph[y].append(x)
        
        def DFS(i):
            if visited[i] == 1:
                return True
            if visited[i] == 0:
                return False
            
            visited[i] = 0
            for out in graph[i]:
                if DFS(out) == False:
                    return False
            visited[i] = 1
            res.append(i)
            return True
        
        res = []
        for i, v in enumerate(visited):
            if v == -1:
                if DFS(i) == False:
                    return []
        return res[::-1]  # 易错 千万不能忘