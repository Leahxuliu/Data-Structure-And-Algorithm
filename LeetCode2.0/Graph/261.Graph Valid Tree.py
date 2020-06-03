#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/09

'''
I. Clarify
    a valid tree == no cirle and one island
    
II. Method
    1. DFS / BFS
    Steps:
        1. the length edges != n - 1 --> False 
            beacuse the graph has circle or more than one island
        2. build visited (0: not visited yet, 1: visited) and graph(adjacent table)
        3. scan vertexs and its neighbors using BfS / DFS
            [now_index, out_index]
            if neighbor vertex has been visited, and the vertex is not parent vertex --> have circle --> False
            else: True
    Complexity:
        Time: O(V + E)
        Space:O(V + E)
    
    3. union find
    Steps:
        1. build groupTag, the vertex's root as th index of the vertex
        2. scan vertexs using edges
            find root by using DFS
            if root1 == root2  --> have circle
    Complexity:
        Time: O(V + E)
        Space:O(V + E)

'''

# BFS
from collections import deque
class Solution:
    def validTree(self, n, edges):
        if n == 0:
            return False
        if n == 1:
            return True
        if len(edges) != n - 1:
            return False
        
        visited = [0] * n
        graph = [[] for _ in range(n)]
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        queue = deque()
        for i in range(n):
            if visited[i] == 0:
                queue.append([i, -1])
                visited[i] = 1
                
                while queue:
                    index, parent = queue.popleft()
                    for out in graph[index]:
                        if visited[out] == 0:
                            queue.append([out, index])
                            visited[out] = 1
                        else:
                            if out != parent:
                                return False
        return True

# DFS
class Solution2:
    def validTree2(self, n, edges):
        if n == 0:
            return False
        if n == 1:
            return True
        if len(edges) != n - 1:
            return False
        
        visited = [0] * n
        graph = [[] for _ in range(n)]
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(index, parent):
            if visited[index] == 1:
                return True
            
            visited[index] = 1
            for out in graph[index]:
                if visited[out] == 1:
                    if out != parent:
                        return False
                else:
                    if dfs(out, index) == False:
                        return False
            return True
        
        for i in range(n):
            if visited[i] == 0:
                if dfs(i, -1) == False:
                    return False
        return dfs(i, -1)

X = Solution2()
print(X.validTree2(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))

# Union find
class Solution:
    def validTree(self, n, edges):
        if n == 0:
            return False
        if n == 1:
            return True
        if len(edges) != n - 1:
            return False
        
        groupTag = [i for i in range(n)]
        def find(i):
            if groupTag[i] == i:
                return i
            else:
                return find(groupTag[i])
        
        for i, j in edges:
            root1 = find(i)
            root2 = find(j)
            if root1 == root2:
                return False
            else:
                groupTag[root2] = root1
        return True