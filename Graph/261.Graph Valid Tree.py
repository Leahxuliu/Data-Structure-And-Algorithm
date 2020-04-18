#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/23  
# @Author  : XU Liu
# @FileName: 261.Graph Valid Tree.py

'''
1. 题目要求：


2. 理解：
判断有没有环且是孤立的
没环孤立 --> true
else --> false

3. 题目类型：
无向图，判断环

4. 输出输入以及边界条件：
input: n: int, edges: List[List[int]]
output: bool
corner case: 

5. 解题思路
    因为是无环孤立，所以必然满足，len(edges) == n - 1:

    方法一：并查集
    方法二：DFS visited [0,1] parent_index
    方法三：BFS

'''

'''
方法一  并查集
time O(N) space O(N)
'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        if n == 1:
            return True
        if len(edges) != n - 1:
            return False
        
        gT = [i for i in range(n)]
        
        def find(index):
            if gT[index] == index:
                return index
            else:
                return find(gT[index])
            
        for i, j in edges:
            root1 = find(i)
            root2 = find(j)
            
            if root1 == root2:
                return False
            
            else:
                gT[root2] = root1
                
        return True

'''
DFS
visited [0,1] parent_index
无环：其访问过的节点有且只有一个，并且是其节点的上一个节点（parent_index)

时间复杂度：
vetex: 角
edge：边
建立邻接表的时候是E，然后扫各个点是V
O(E + V)

空间复杂度：
建立visited用了V
建立邻接表用E
O(E + V)
'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        if n == 1:
            return True
        if len(edges) != n - 1:
            return False
        
        visited = [0] * n
        graph = [[] for _ in range(n)]
        
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        def dfs(index, parent_index):
            visited[index] = 1
            for j in graph[index]:
                if visited[j] == 1:
                    if j != parent_index:
                        return False
                elif visited[j] == 0:
                    if dfs(j, index) == False:
                        return False
            return True
        
        
        for i in range(n):
            if visited[i] == 0:
                if dfs(i, -1) == False:
                    return False
        return True

'''
BFS 判断环
parent法
'''
from collections import deque, defaultdict
class Solution:
    def validTree(self, n: int, edges) -> bool:
        if not n:
            return False
        if n == 1:
            return True
        if not edges:
            return False
        if n != len(edges) + 1:
            return False

        visited = [0] * n
        graph = defaultdict(set)
        # graph = [[] for _ in range(n)]
        queue = deque()
        
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
            
        for i in range(n):
            if visited[i] == 0:
                queue.append([i,-1])
            
            while queue:
                index, parent = queue.popleft()
                visited[index] = 1
                
                for out_index in graph[index]:
                    if visited[out_index] == 0:
                        queue.append([out_index, index])
                    elif out_index != parent:
                        return False
        return True