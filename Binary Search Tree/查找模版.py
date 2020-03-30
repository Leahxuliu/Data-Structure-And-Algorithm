#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
若布局良好，则是O(log(n))
若是skewed tree，node分布在一条直线上，查找时间为 O(n) worst case
'''


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BST:
    def findBFS(self, root, target):
        if not root:
            return None
        
        while root:
            if root.val == target:
                return root
            elif root.val > target:
                root = root.left
            elif root.val < target:
                root = root.right
        return None
    
    def findDFS(self, root, target):
        if not root:
            return None
        if root.val == target:
            return root
        
        if target < root.val:
            return self.findDFS(root.left, target)
        else:
            return self.findDFS(root.right, target)
    