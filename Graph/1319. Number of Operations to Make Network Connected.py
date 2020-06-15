# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/14

class Solution:
    def makeConnected(self, n: int, pairs: List[List[int]]) -> int:
        if n == 0 or n == 1:  # corner case
            return 0
        # number of PC - 1 > number of pairs
        if n - 1 > len(pairs):
            return -1

        graph = [[] for _ in range(n)]
        visited = [0] * n

        for i, j in pairs:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(i):
            if visited[i] == 1:
                return 
            visited[i] = 1
            for out in graph[i]:
                if visited[out] == 0:
                    dfs(out)

        island = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                island += 1
        return island - 1


# union find
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n == 0 or n == 1:
            return 0
        if n - 1 > len(connections):
            return -1
        
        gT = [x for x in range(n)]
        times = 0
        
        def find(i):
            if i == gT[i]:
                return i
            else:
                return find(gT[i])
        
        for i, j in connections:
            root1 = find(i)
            root2 = find(j)
            if root1 != root2:
                times += 1
                gT[root2] = root1
        return n - times - 1
 

# union find + rank
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n == 0 or n == 1:
            return 0
        if n - 1 > len(connections):
            return -1
        
        gT = [x for x in range(n)]
        times = 0
        rank = [1] * n
        
        def find(i):
            if i == gT[i]:
                return i
            else:
                return find(gT[i])
        
        for i, j in connections:
            root1 = find(i)
            root2 = find(j)
            if root1 != root2:
                times += 1
                if rank[root1] >= rank[root2]:
                    rank[root1] += rank[root2]
                    gT[root2] = root1
                else:
                    rank[root2] += rank[root1]
                    gT[root1] = root2
                    
        return n - times - 1
        