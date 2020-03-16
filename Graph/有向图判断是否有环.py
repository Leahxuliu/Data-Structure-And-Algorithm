#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution:
    def canFinish(self, nums, pairs):  # return T有环/F无环
        if nums == 0:  # corner case
            return False
        if pairs == []:
            return False

        graph = [[] for _ in range(nums)]
        visit = [-1] * nums  # 三种状态，-1未访问，0正在DFS中访问，1已经访问

        for i, j in pairs:  # build adjacency table
            #graph[j].append(i)  # pairs里面从右到左
            graph[i].append(j)  # 两者方向不同，根据题目来；pairs里面从左到右

        print(graph)

        for i in range(nums):
            if self.dfs(graph, visit, i):
                return True
        return False


    def dfs(self, graph, visit, index):  # when repeat, return True有环or False无环
        if visit[index] == 0:  # 关键条件，遇到正在visited的node --> 环
            return True
        if visit[index] == 1: # 只访问未访问的，相当于剪枝
            return False

        visit[index] = 0
        for elem in graph[index]:
            if self.dfs(graph, visit, elem) == True:
                return True
        visit[index] = 1
        return False

x = Solution()
print(x.canFinish(6, [[0,1], [1,2], [2,3], [3,4], [4,5], [5,2], [3,0]]))
#print(x.canFinish(4, [[0,1], [1,2], [0,3], [3,2]]))  # 不是循环环，1，2都指向3 --> false
#print(x.canFinish(5, [[0,1], [0,2], [0,3], [1,4]]))

# 以一个点出发，在dfs里面转一圈，转到有0的点，也就意味着是一个环
# 这一点都转完之后，这一点就记录成1
