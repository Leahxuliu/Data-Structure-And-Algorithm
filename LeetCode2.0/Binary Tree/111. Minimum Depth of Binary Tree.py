#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/24

# BFS
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        queue = deque()
        queue.append([root, 0])
        res = float('inf')

        while queue:
            node, depth = queue.popleft()
            depth = depth + 1

            if node.left == None and node.right == None:
                res = min(res, depth)

            
            if node.left != None:
                queue.append([node.left, depth])
            
            if node.right != None:
                queue.append([node.right, depth])
        
        return res

# DFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        def helper(root, depth):
            depth = depth + 1
            if root.left == None and root.right == None:
                self.res = min(self.res, depth)
                
            if root.left != None:
                helper(root.left, depth)
            if root.right != None:
                helper(root.right, depth)

        self.res = float('inf')
        helper(root, 0)
        return self.res

# DFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)

        if l != 0 and r != 0:
            return min(l, r) + 1
        else:
            return max(l, r) + 1