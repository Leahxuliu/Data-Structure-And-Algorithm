#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/08


'''

1. use dict to store 
    key: old node
    vale: new node
2. use BFS to scan the nodes and the neighbors -- node
    if node not in dict, dict[node] = Node(node.val)
    dict[node].neighbors.append(dict[B])
    
'''

# BFS + dict
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        dic = {}
        queue = deque()
        queue.append(node)
        dic[node] = Node(node.val)
        while queue:
            root = queue.popleft()
            for elem in root.neighbors:
                if elem not in dic:
                    queue.append(elem)
                    dic[elem] = Node(elem.val)
                dic[root].neighbors.append(dic[elem])
        return dic[node]

# DFS + dict
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        def DFS(root):
            if not root:
                return 
            
            for elem in root.neighbors:
                if elem not in dic:
                    dic[elem] = Node(elem.val)
                    DFS(elem)
                dic[root].neighbors.append(dic[elem])
        
        dic ={}
        dic[node] = Node(node.val)
        DFS(node)
        return dic[node]


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return 
        
        info = {}
        
        def DFS(root):  
            if root == None:
                return 
            
            if root not in info:
                info[root] = Node(root.val)
            
            for out in root.neighbors:
                if out not in info:
                    DFS(out)
                info[root].neighbors.append(info[out])
        
        DFS(node)
        return info[node]