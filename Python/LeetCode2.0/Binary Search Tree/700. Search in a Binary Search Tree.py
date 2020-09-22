#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/16

'''
Method
A.BFS
Steps: 
    1. traverse nodes from tree
    2. if root.val == val, return root
       if root.val > val, continue scan root.left
       if root.val < val, continue scan root.right

B.DFS
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BSF
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return 
        
        while root:
            if root.val == val:
                return root
            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right

# DSF
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return 
        
        if root.val == val:
            return root
        
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)