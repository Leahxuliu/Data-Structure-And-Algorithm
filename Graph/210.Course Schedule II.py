#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/17  
# @Author  : XU Liu
# @FileName: 210.Course Schedule II.py

'''
1. 题目要求：


2. 理解：
[0,1] --> 要想上0的课，就要先上1的课
类似tree里面的找路径
从0开始

3. 题目类型：
有向图
路径

4. 输出输入以及边界条件：
input: num pairs
output: list
corner case: 易错点 corner case有三个
             numCourses == 0 --> None
             numCourses == 1 --> [0]
             prerequisites == None --> [i for i in range(nums)]

5. 解题思路
    1. 如果有环，输出[]
    2. 如果没环，输出一种选课
    3. 用dfs，[-1,0,1]或者用拓扑排序

'''

'''
dfs
'''

class Solution:
    def findOrder(self, numCourses, prerequisites):
        if numCourses == 0:
            return None
        if numCourses == 1:
            return [0]
        if prerequisites == None:
            return [i for i in range(numCourses)]
        
        
        graph = [[] for _ in range(numCourses)]
        visited = [-1] * numCourses
        
        for i, j in prerequisites:
            graph[j].append(i)
        
        path = []
        for i in range(numCourses):
            if self.pathDFS(graph, visited, i, path) == True:  # 易错点：path是一个参数
                return []        
        return path[::-1]  # 因为dfs是先到根部，再往回走，所以要倒一下
            
        
    def pathDFS(self, graph, visited, index, path):
        if visited[index] == 0:
            return True
        
        if visited[index] == 1:
            return False
        
        visited[index] = 0
        for elem in graph[index]:
            if self.pathDFS(graph, visited, elem, path) == True:
                return True
        visited[index] = 1
        path.append(index)
        return False


'''
toposort
'''
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:  # corner case
            return []
        if numCourses == 1:
            return [0]
        if prerequisites == []:
            return [x for x in range(numCourses)]
        
        outdegree = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for i,j in prerequisites:
            outdegree[j].append(i)
            indegree[i] += 1
        
        path = []
        queue = deque()
        for i, each_in in enumerate(indegree):
            if each_in == 0:
                queue.append(i)
                
        while queue:
            node_index = queue.popleft()
            path.append(node_index) 
            for elem in outdegree[node_index]:
                indegree[elem] -= 1
                if indegree[elem] == 0:
                    queue.append(elem)
        
        if indegree == [0] * numCourses:  # 本题，还需要判断是否有环
            return path  # 易错点，这里不需要path[::-1]
        else:
            return []

x = Solution()
print(x.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))