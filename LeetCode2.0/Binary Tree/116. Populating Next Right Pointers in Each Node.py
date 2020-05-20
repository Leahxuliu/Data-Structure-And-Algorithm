#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/20

'''
Method - BFS
Steps:
    1. use queue to store nodes of each level
    2. make the node have next property
    3. pop last level's nodes and 
    
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return 
            
        queue = deque()
        queue.append(root)
        
        while queue:
            q_len = len(queue)
            
            for i in range(q_len):
                if i == q_len - 1:
                    queue[i].next = None
                else:
                    queue[i].next = queue[i + 1]
            
            for _ in range(q_len):
                node = queue.popleft()
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        return root