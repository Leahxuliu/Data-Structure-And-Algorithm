#!/usr/bin/python
# -*- coding: utf-8 -*-

# BFS
# 以无向图举例
from collections import deque
class Solution:
    def bfsGraph(self, num, pairs):
        graph = [[] for _ in range(num)]  # 建立空邻接表 tO(N)
        visited = [0 for _ in range(num)]  # 建立空访问表

        for i, j in pairs:  # 填充邻接表 tO(E)
            graph[i].append(j)
            graph[j].append(i)
        print(graph)
        queue = deque()
        queue.append(0)

        while queue:
            node_index = queue.popleft()  # 从某个顶点出发，访问其各个邻接点
            visited[node_index] = 1
            print('visited node index:%s' % node_index)
            print('visit: %s' % visited)
            for neigh_index in graph[node_index]:  # 从邻接点出发，访问邻接点的邻接点
                if visited[neigh_index] == 0:
                    queue.append(neigh_index)
        return
    
    #def isCyclic(self, n, pairs):  # return T for cyclic, False for acyclic
        
x = Solution()
x.bfsGraph(5, [[0,1], [0,2], [0,3], [1,4]])