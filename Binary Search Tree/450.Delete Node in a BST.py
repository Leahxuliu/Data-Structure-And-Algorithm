# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/31  
# @Author  : XU Liu
# @FileName: 450.Delete Node in a BST.py

'''
1. 题目类型：
    BST

2. 题目要求与理解：
    remove node

3. 解题思路：


4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    

'''

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        if key == root.val:
            if root.left == None and root.right == None:
                root = None
            elif root.left == None:
                root = root.right
            elif root.right == None:
                root = root.left
            else:
                root.val = self.findPre(root)
                root.left = self.deleteNode(root.left, root.val)
                '''
                root.val = self.findSuc(root)
                root.right = self.deleteNode(root.right, root.val)
                '''
        return root

    # 移前驱点         
    def findPre(self,root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    # 移动后去点
    def findSuc(self, root):  # find the smallest node of root right subtree
        root = root.right
        while root.left:
            root = root.left
        return root.val

'''
BFS 
错误
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None or key == 0:
            return 
        
        def find(root):
            node = root.left
            while node.right:
                node = node.right
            return node.val
        
        res = root
        
        while root:
            if root.val == key:
                if root.left == None and root.right == None:
                    root = None  # 错误，res里面，这个node没有变成None
                    return res
                
                elif root.left == None:
                    root.val = root.right.val
                    root.right = None
                    return res
                
                elif root.right == None:
                    root.val = root.left.val
                    root.left = None
                    return res
                
                else:
                    pre = find(root)
                    root.val = pre
                    key = pre
                    root = root.left
            
            elif root.val > key:
                root = root.left
            
            elif root.val < key:
                root = root.right
        
        return res