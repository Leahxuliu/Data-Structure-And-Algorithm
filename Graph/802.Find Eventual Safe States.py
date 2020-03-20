#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/20  
# @Author  : XU Liu
# @FileName: 802.Find Eventual Safe States.py

'''
1. 题目要求：


2. 理解：
从start node开始走，走到重点的次数要少于nodes的个数
找到安全的起始点
也就是该点不在环里面-->找没有环的点

3. 题目类型：
有向图
判断是否有环

4. 输出输入以及边界条件：
input: graph
output: list
corner case: graph == None --> []

5. 解题思路
    1. 遍历nodes
    2. 判断该node所在路径里面是否包含环

'''

'''
indegree = [0] * nums
本方法是错误的
因为，入度都不为0的时候（有环），没法判断，没有环的部分也进不去了
比如graph：[[1,2],[2,3],[5],[0],[5],[],[]]
'''

'''
from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        if graph == None:
            return []
        
        indegree = [0] * len(graph)
        
        for each in graph:
            for out in each:
                indegree[out] += 1
        
        
        queue = deque()
        cir_nodes = []
        for i, v in enumerate(indegree):
            if v == 0:
                queue.append(i)
        
        safe_nodes = []
        while queue:
            node_index = queue.popleft()
            safe_nodes.append(node_index)
            for out_index in graph[node_index]:
                indegree[out_index] -= 1
                print(indegree)
                if indegree[out_index] == 0:
                    queue.append(out_index)
         
        
        print(safe_nodes)

'''

'''
拓扑排序
outdegree = [0] * nums
indegree = [[] for _ in range(len(graph))]
有环的话，出度永远不会为0
queue里面加入出度为0的node
从结束点往回走
'''

from collections import deque
class Solution:
    def eventualSafeNodes(self, graph):
        if graph == None:
            return []
        
        outdegree = [0] * len(graph)
        indegree = [[] for _ in range(len(graph))]
        
        for i, each in enumerate(graph):
            outdegree[i] = len(each)
            for s in each:
                indegree[s].append(i)
                
        queue = deque()
        safe_nodes = []
        for i, v in enumerate(outdegree):
            if v == 0:
                queue.append(i)
        
        while queue:
            index = queue.popleft()
            
            safe_nodes.append(index)
            
            for elem in indegree[index]:
                outdegree[elem] -= 1
                if outdegree[elem] == 0:
                    queue.append(elem)
        
        return sorted(safe_nodes)

'''
DFS
[-1,0,1]
'''

class Solution:
    def eventualSafeNodes(self, graph):
        if not graph:
            return []
        
        visited = [-1] * len(graph)
        
        def dfs(index):
            if visited[index] == 0:
                return True
            if visited[index] == 1:
                return False
            
            visited[index] = 0
            for elem in graph[index]:
                if dfs(elem):
                    return True
                
            visited[index] = 1
            return False
        
        
        safe_nodes = []
        for i in range(len(graph)):
            if dfs(i) == False:
                safe_nodes.append(i)
        
        return sorted(safe_nodes)
                
x = Solution()
print(x.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))