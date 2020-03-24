#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/16  
# @Author  : XU Liu
# @FileName: 133.Clone Graph.py

'''
1. 题目要求：


2. 理解：
对无向图进行复制
graph看起来是一样的，nodes是new（deep copy）

3. 题目类型：
无向图
图的性质

4. 输出输入以及边界条件：
input: list，eg：adjList = [[2,4],[1,3],[2,4],[1,3]]；1链接的2，4；2链接着1，3
output: list，同上
corner case: 只有一个点 --> list，eg：adjList[[]] --> 输出[[]]
             空图：输入[] --> 输出[]
             两个点：输入：adjList = [[2],[1]] --> 输出 [[2],[1]]
5. 解题思路
    方案一
    1. 用BFS遍历一遍
    2. 同时创建新图的邻接点表
    3. 用dict保存新的结果，key是node，value是neighbors；同时这个dict也起到visited的作用
    4. 注意避免重复，neigbor遇到重复点时，不要重复新建节点

    time complexity O(N)  space O(N)

'''

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

'''
错误回答
虽然答案的数字是一样的，但是不具备Node的性质
'''

from collections import deque
import copy
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        if node.neighbors == None:
            return node.deepcopy()
        
        new = {}
        queue = deque()
        queue.append(node)
        
        while queue:
            node = queue.popleft()
            new[node.val] = []
            for i in node.neighbors:
                new[node.val].append(i.val)
                if i.val not in new:
                    queue.append(i)
        
        sort = sorted(new.items(),key=lambda d:d[0])
        res = []
        for each in sort:
            res.append(each[1])
        print(res)
        return res

'''
更正
'''

from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:  # corner case
            return None
        if not node.neighbors:
            res = Node(node.val)  # 易错点
            return res

        visited = {}

        queue =deque([node])
        visited[node] = Node(node.val)
        print(visited)

        while queue:
            n = queue.popleft()
            for elem in n.neighbors:
                if elem not in visited:
                    visited[elem] = Node(elem.val)
                    queue.append(elem)
                visited[n].neighbors.append(visited[elem])
        return visited[node]



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.neighbors = [b, d]
b.neighbors = [a, c]
c.neighbors = [b, d]
d.neighbors = [a, c]

x = Solution()
print(x.cloneGraph(a))