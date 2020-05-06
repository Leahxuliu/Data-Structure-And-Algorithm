#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/06

'''
I. Clarity
    find max depth of BT
    TreeNode was defined? yes
    
    input: root:TreeNode
    output: max depth(int)
    corner case: root == None --> return 0
    
II. Methods
    A. DFS (Recursion)
    Steps:
        1. ending condition: root == None --> return 0
        2. Select the maximum depth in left depth and right depth (temp_max_depth)
        3. temp_max_depth + 1
        
    Complexity:
        Time: O(N)
        Space: average:O(logN); worse:O(N)  # logN = the high of tree
    
    B. BFS 
    Steps:
        1. Use queue to store the first level of nodes
        2. pop them, then add next level of nodes
        3. repeat step2 until no node 
        4. depth = how many levels
        
    Complexity:
        Time: O(N)  
        Space: average:O(N/2); best:O(1)  #  N/2 = the maximum number of nodes at the same level
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

#########################################################################################

# BFS
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        depth = 0
        queue = deque()
        queue.append(root)
        
        while queue:
            len_q = len(queue)
            depth += 1
            for i in range(len_q):
                node = queue.popleft()
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        return depth