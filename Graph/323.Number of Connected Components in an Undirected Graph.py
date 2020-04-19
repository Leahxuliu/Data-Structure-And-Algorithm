#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/20  
# @Author  : XU Liu
# @FileName: 323.Number of Connected Components in an Undirected Graph.py

'''
1. 题目要求：


2. 理解：
无向图
判断有几个群

3. 题目类型：
无向图
判断孤立和分群

4. 输出输入以及边界条件：
input: n: int, edges: List[List[int]]
output: int
corner case: n == 0 --> 0
             edges == [] --> n

5. 解题思路
    方法一：利用并查集对nodes进行分组
    方法二：dfs [0,1]法
    
'''
'''
union-find
易错点：有环的时候，groupTag里面数的个数不等于群的个数
要用一个numb来表示
具体原因见‘并查集.py'
'''

class Solution:
    def countComponents(self, n, edges):
        #if n == 0 or edges == []:  # 错误 n = 1, edges = []的时候，不应该输出0，而应该是1
        #    return 0  # 这里写成n，就对了
        if n == 0:
            return 0
        if edges == []:
            return n  # 易错，不是0是n
        
        groupTag = [i for i in range(n)]
        
        def find(index):
            if groupTag[index] == index:
                return index
            else:
                return find(groupTag[index])
            
        numb = 0
        for i,j in edges:
            root1 = find(i)
            root2 = find(j)
            
            if root1 == root2:
                pass
            else:
                numb += 1
                groupTag[root2] = root1
        print(groupTag)        
        return n - numb


'''
DFS
'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = [0] * n
        
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        def dfs(index):
            if visited == [1] * n:
                return 
            visited[index] = 1
            for out_node in graph[index]:
                if visited[out_node] == 0:
                    dfs(out_node)
            
        group = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                group += 1
        
        return group

x = Solution()
print(x.countComponents(4,[[2,3],[1,2],[1,3]]))


'''
BFS
'''

from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0 or edges == []:
            return n
       
        visited = [0] * n
        graph = [[] for _ in range(n)]
        
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        group = 0
        queue = deque()
        for i in range(n):
            if visited[i] == 0:
                queue.append(i)
                group += 1
                
            while queue:
                index = queue.popleft()
                visited[index] = 1
                for out in graph[index]:
                    if visited[out] == 0:
                        queue.append(out)
            
        return group
