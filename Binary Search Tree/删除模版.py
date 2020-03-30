#!/usr/bin/python
# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST:
    def deleteNode(self, root, target):
        if not root:
            return None
        
        if target < root.val:
            root.left = self.deleteNode(root.left, target)
        
        if target > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key == root.val:
            if root.left == None and root.right == None:
                root = None
            elif root.left == None:
                root = root.right
            elif root.right == None:
                root = root.left
            else:
                predecessor = self.findPre(root)
                root.val = predecessor
                root.left = self.deleteNode(root.right, target)
                
        return root

    def findPre(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val