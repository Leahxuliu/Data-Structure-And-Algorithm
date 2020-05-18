#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/18


'''
注意
不能用网格搜索，网格搜索不能斜着走

考点：
邻接矩阵表


Method
A. DFS
Steps:
    1. build visited table to memo the node is visited or not
    # 2. use M to build graph 这一步会导致时间复杂度变大
        [[1], [0], []]
    3. traverse vertexs
        a. when visited[i] == 0, use dfs to visited the neighbors of i
        b. count the times of a
    4. return times

Time: O(N) N = V + E
space: O(N)
    
    
B.Union find
Steps:  
    1. create graphTag by using the index as tag
    2. scan the paris(i, j), M[i][j] == 1
        use dfs() to find the i and j's root
        if i root == j root, pass
        if i root != j root, make j root == i root, and count the times
    3. res = the number of students - times
    
'''



# DFS
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        
        if N == 0:
            return 0
        
        visited = [0] * N
        
        def DFS(i):
            if visited[i] == 1:
                return 
            
            visited[i] = 1
            for j in range(len(M)):
                if j != i:
                    if M[i][j] == 1:
                        DFS(j)
        
        res = 0
        for i in range(N):
            if visited[i] == 0:
                DFS(i)
                res += 1
        return res

# BFS
from collections import deque
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        
        if N == 0:
            return 0
        
        visited = [0] * N
        
        
        res = 0
        queue = deque()
        for i in range(N):
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                res += 1
                
                while queue:
                    index = queue.popleft()
                    
                    for j in range(N):
                        if j != index:
                            if M[index][j] == 1 and visited[j] == 0:
                                queue.append(j)
                                visited[j] = 1
        return res

# Union find
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        
        if N == 0:
            return 0
        
        gT = [x for x in range(N)]
        
        def find(i):
            if gT[i] == i:
                return i
            else:
                return find(gT[i])
        
        
        times = 0
        for i in range(N):
            for j in range(i + 1):
                if M[i][j] == 1:
                    root1 = find(i)
                    root2 = find(j)
                    
                    if root1 == root2:
                        pass
                    else:
                        gT[root2] = root1
                        times += 1
        return N - times