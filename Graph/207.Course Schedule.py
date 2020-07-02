#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/16  
# @Author  : XU Liu
# @FileName: 207.Course Schedule.py

'''
1. 题目要求：


2. 理解：
能不能完成课 == 没有环

3. 题目类型：
有向图，判断是否有环

4. 输出输入以及边界条件：
input: list(pair)
output: bool
corner case: None --> T; 只有一个点 --> F

5. 解题思路
    用拓扑排序或者常规的dfs(-1,0,1)判断是否有环

'''

'''
方案一
拓扑排序
核心，queue里面加入入度为0的
只要有环，入度表里面一定会有不为0的
'''

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        outdegree = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for x,y in prerequisites:
            outdegree[y].append(x)
            indegree[x] += 1
            
        queue = deque()
        for i, v in enumerate(indegree):
            if v == 0:
                queue.append(i)
        
        while queue:
            node_index = queue.popleft()
            for out_index in outdegree[node_index]:
                indegree[out_index] -= 1
                if indegree[out_index] == 0:
                    queue.append(out_index)
                    
        return indegree == [0] * numCourses


'''
方案二
DFS
易错点：有环是F
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses:
            return True
        if not prerequisites:
            return True
        
        visited = [-1] * numCourses
        graph = [[] for _ in range(numCourses)]
        
        for i,j in prerequisites:
            graph[j].append(i)
        
        for i in range(numCourses):
            if self.dfs(graph, visited, i) == False:
                return False
        return True
            
    def dfs(self, graph, visited, i):  # T:有环 -->不行； F：无环
        if visited[i] == 0:
            return False
        if visited[i] == 1:
            return True
        
        visited[i] = 0
        for elem in graph[i]:
            if self.dfs(graph, visited, elem) == False:
                return False
        visited[i] = 1
        return True

    # ok
    def dfs(i):
            visited[i] = 0
            for out in graph[i]:
                if visited[out] == 0:
                    return False
                elif visited[out] == -1:
                    if dfs(out) == False:
                        return False
                    
            visited[i] = 1
            return True