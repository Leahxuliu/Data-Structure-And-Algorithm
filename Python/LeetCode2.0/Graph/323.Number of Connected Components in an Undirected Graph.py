#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/08

'''
I.Clarify
    to count how many connected components 
    
    input: n:int, the number of nodes, [0:] 
           edges:list[int], the length of edges:[0:]
           the node's value: [0:]
    output: int -- the number of components
    corner case: n == 0 --> 0
                 len(edges) == 0 --> n

II.Method
    A. BFS / DFS
    Steps:
        1. build the visited list (0: not visited; 1:visited) and the graph (adjacent table)
        2. scan the nodes and its neighbors using BFS / DFS
        3. count components
        
    Complexity:
        Time and Space: O(V + E), V is vertex, E is edge
    
    C. Union find
    Steps:(写法参考李厨子)
        1. tag every node's parent as index of the node in groupTag
        2. scan every pair [i, j] of edge
            find i's parent by dfs
            find j's parent by dfs
            if i's parent == j's parent, they are connected
            else: 
                change j's parent as i's parent
        3. count connect of changing, n - connect is result
            当所有点都相连，需要n - 1个connect
            1个island n - 1个connect  n - (n - 1) = 1
            2个island n - 2个connect  n - (n - 2) = 2
    Complexity:
        Time: O(V + E)
        Sapce:O(V + E)
        
    
'''



# BFS
from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
        if edges == [[]] or edges == []:
            return n
        
        visited = [0] * n
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        queue = deque()
        res = 0
        for i in range(n):
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                res += 1
                while queue:
                    index = queue.popleft()
                    for out in graph[index]:
                        if visited[out] == 0:
                            queue.append(out)
                            visited[out] = 1
        return res

# DFS
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
        if edges == [[]] or edges == []:
            return n
        
        visited = [0] * n
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(i):
            if visited[i] == 1:
                return
            
            visited[i] = 1
            for elem in graph[i]:
                if visited[elem] == 0:
                    dfs(elem)
        
        res = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                res += 1
                
        return res

# union find
class Solution:
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
        if edges == [[]] or edges == []:
            return n
        
        groupTag = [i for i in range(n)]
        
        def find(i):  # return root:int
            if groupTag[i] == i:
                return i
            return find(groupTag[i])
        
        connect = 0
        for i, j in edges:
            root1 = find(i)
            root2 = find(j)
            
            if root1 == root2:
                pass
            else:
                groupTag[root2] = root1
                connect += 1
        return n - connect