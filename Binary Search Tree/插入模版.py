#!/usr/bin/python
# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

'''
一定是成为left child 或者right child，除了root=None的情况
所以插入一个新的节点时，关键点找到父节点
'''

class BST:
    # 方法一 BFS
    def insertIteration(self, rrot, target):  # return root with inserted target
        if not root:  # corner case
            return TreeNode(target)  # 成为新的BST，len只有一

        res = root
        while root:
            if root.val > target:  
                if root.left is None:  # 成为这个node的left child
                    root.left = TreeNode(target)
                    return res
                else:
                    root = root.left  # 继续往左走
            
            else:  # root.val < target:  root.left < root.val < target <= root.right
                if root.right if None:
                    root.right = TreeNode(target)
                    return res
                else:
                    root = root.right


    # 方法二 DFS
    def insert(self, root, target):
        if not root:  # corner case + ending条件
            return TreeNode(target)
        
        if target < root.val:
            root.left = self.insert(root.left, target)
        else:
            root.right = self.insert(root.right, target)
        return root
