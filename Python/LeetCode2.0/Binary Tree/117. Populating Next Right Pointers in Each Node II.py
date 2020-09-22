'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/19

Method - BFS
Steps:
    0. traverse nodes in Tree
    1. use queue to store nodes in each level
    2. popleft nodes in last level and store nodes in next level
    3. make the node have the property of Node

Time: O(N)
Space: O(N/2)


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
        
        new_root = root
        queue = deque()
        queue.append(root)
        
        while queue:
            q_len = len(queue)
            
            for i in range(q_len):
                if i == q_len - 1:
                    queue[i].next = None
                else:
                    queue[i].next = queue[i + 1]
            
            for j in range(q_len):
                node = queue.popleft()
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        return new_root
        