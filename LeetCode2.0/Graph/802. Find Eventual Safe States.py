#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/23

'''
Method - DFS
Steps:
    1. build visited list to store the node is visited or not yet
    2. use dfs to scan the node and its neighbors
    3. if the neighbor is visiting, it means there are a circle between nodes --> not safe node
       else, safe node

Space: O(V + E)
Time: O(V + E)


Method2 - Topo
Steps:
    1. use graph to build indegree and outdegree, store the neightbor nodes in to indegee, store the number of out in the outdegree 
    2. scan the vetexs
    3. if the node of outdegree is 0, append this node into res list
'''

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        if n == 0:
            return 
        
        def dfs(i):  # True == no circle / safe node
            if visited[i] == 1:
                return True
            if visited[i] == 0:
                return False
            
            visited[i] = 0
            for out in graph[i]:
                if dfs(out) == False:
                    return False
            visited[i] = 1
            res.append(i)  # add safe nodes
            return True


        visited = [-1] * n
        res = []
        for i in range(n):
            if visited[i] == -1:
                dfs(i)
        res.sort()     
        return res  # 易错点， return res.sort()则是空，因为sort()是没有返回值


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