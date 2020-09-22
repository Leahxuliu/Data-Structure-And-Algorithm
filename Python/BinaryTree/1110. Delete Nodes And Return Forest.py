# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/07/3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root == None:
            return []
        
        def helper(root, is_root):  # return new root
            if root == None:
                return None
            
            flag = False
            if root.val in to_delete:
                flag = True
                
            if flag == False and is_root == True:
                res.append(root)
            
            root.left = helper(root.left, flag)
            root.right = helper(root.right, flag)
            
            if flag == False:
                return root
            else:
                return None
        
        res = []
        to_delete = set(to_delete)
        helper(root, True)
        return res
        