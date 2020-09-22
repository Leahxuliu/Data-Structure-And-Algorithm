#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/16

'''
Method 
A. DFS
Steps:
    1. initialize max_val = float('inf') and min_val = float('-inf')
    2. use dfs to scan the nodes
        if node.val >= max_val or node.val <= min_val, return False
        else True

Time complexity: O(N)
Space: O(logN)


B. 中序遍历BFS

C. 普通的BFS
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        def helper(root, max_val, min_val):
            if root == None:
                return True
            
            if root.val >= max_val or root.val <= min_val:
                return False
            return helper(root.left, root.val, min_val) and helper(root.right, max_val, root.val)
        
        max_val = float('inf')
        min_val = float('-inf')
        return helper(root, max_val, min_val)


# BFS 中序遍历
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        stack = []
        pre = -float('inf')
        node = root
        
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            curr = stack.pop()
            if curr.val <= pre:
                return False
            else:
                pre = curr.val
            
            if curr.right != None:
                node = curr.right
            
        return True


# BFS 普通
from collections import deque
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True

        queue = deque()
        queue.append([root, float('inf'), float('-inf')])

        while queue:
            node, max_val, min_val = queue.popleft()

            if node.val >= max_val or node.val <= min_val:
                return False
            
            if node.left != None:
                queue.append([node.left, node.val, min_val])
            if node.right != None:
                queue.append([node.right, max_val, node.val])

        return True