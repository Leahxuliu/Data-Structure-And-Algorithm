#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/24

# BFS
from collections import deque
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        res = 0
        queue = deque()
        if root.left != None:
            queue.append([root.left, 1, 'l'])
        if root.right != None:
            queue.append([root.right, 1, 'r'])
        
        while queue:
            node, depth, pre = queue.popleft()
            if pre == 'l':
                if node.right == None:
                    res = max(res, depth) 
                else:
                    queue.append([node.right, depth+1, 'r'])
                if node.left != None:
                    queue.append([node.left, 1, 'l'])

            else:
                if node.left == None:
                    res = max(res, depth)
                else:
                    queue.append([node.left, depth + 1, 'l'])
                if node.right != None:
                    queue.append([node.right, 1, 'r'])
        return res

# DFS
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 0
        
        def dfs(root, l, r):
            self.res = max(l, r, self.res)

            if root.left != None:
                dfs(root.left, r + 1, 0)
            if root.right != None:
                dfs(root.right, 0, l + 1)

        self.res = 0
        dfs(root, 0, 0)
        return self.res