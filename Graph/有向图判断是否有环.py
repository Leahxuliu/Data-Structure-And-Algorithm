#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution:
    def canFinish(self, nums, condition):  # return T有环/F无环
        if nums == 0:  # corner case
            return False
        if condition == []:
            return False

        graph = [[] for _ in range(nums)]
        visit = [-1] * nums  # 三种状态，-1未访问，0正在DFS中访问，1已经访问

        for i, j in condition:  # build adjacency table
            graph[j].append(i)

        for i in range(nums):
            if self.dfs(graph, visit, i):
                return True
        return False


    def dfs(self, graph, visit, ind):  # when repeat, return True有环or False无环
        if visit[ind] == 0:
            return True
        if visit[ind] == 1: # 只访问未访问的，相当于剪枝
            return False

        visit[ind] = 0
        for elem in graph[ind]:
            if self.dfs(graph, visit, elem):
                return True
        visit[ind] = 1
        return False

x = Solution()
print(x.canFinish(5, [[0,1], [0,2], [0,3], [1,4]]))
