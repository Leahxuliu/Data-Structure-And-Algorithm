#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/16

'''
Method - BFS(inorder)
Steps:
    1. use stack to store nodes
    2. traverse root.left, put them into stack
    3. pop node from stack, and count n
    4. if node have right, put right into stack
    5. when n == k, return node.val
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root == None:
            return 
        
        stack = []
        node = root
        n = 0
        
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            if curr.right != None:
                node = curr.right
                