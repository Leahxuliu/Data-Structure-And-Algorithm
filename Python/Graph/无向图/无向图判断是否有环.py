#!/usr/bin/python
# -*- coding: utf-8 -*-

# 核心：无环的时候，其节点的邻接点当中，有且只有一个是已经遍历过的，并且一定是上一个节点（parent）
class Solution:
    def isCyclic(self, nums, pairs):  # return T有环/F无环
        if not nums:
            return False
        if not pairs:  # 有点没有边 --> 都是散点
            return False
        
        visited = [0] * nums
        graph = [[] for _ in range(nums)]
        
        for i, j in pairs:
            graph[i].append(j)
            graph[j].append(i)
        
        for i in range(nums):
            if visited[i] == 0:  # 必须遍历unvisited node
                if self.dfs(i, graph, visited, -1):# -1 代表i=0的parent节点序号是-1
                    return True
        return False
    
    def dfs(self, i, graph, visited, parent_index):  # return T for 有环，F for 无环
        visited[i] = 1
        for j in graph[i]:  # 遍历第i位数的所有邻接点
            if visited[j] == 1:  # 这个邻接点已经被访问过
                if j != parent_index:  # 若无环，其访问过的节点有且只有一个，并且是其节点的上一个节点(parent)；若有，则不是
                    return True
            elif visited[j] == 0:
                if self.dfs(j, graph, visited, i):
                    return True
        return False

x = Solution()
print(x.isCyclic(5, [[0,1], [0,2], [0,3], [1,4]]))