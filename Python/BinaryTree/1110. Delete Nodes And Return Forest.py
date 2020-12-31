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
        

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root == None or len(to_delete) == 0:
            return []
        
        def forest(root, is_root):
            '''
            return 该点是否要被删除 True 删除 False 不删除
            同时True的时候，也就意味着下一个节点是新的root
            '''
            if root == None:
                return True
            
            if is_root and root.val not in to_delete:
                self.res.append(root)
            
            flag = False
            if root.val in to_delete:
                flag = True
            
            L = forest(root.left, flag)
            R = forest(root.right, flag)
            if L == True:
                root.left = None
            if R == True:
                root.right = None

            return flag

        self.res = []
        to_delete = set(to_delete)
        forest(root, True)
        return self.res


# 错误
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root == None or root.val in to_delete:
            return[]
        
        def findRoots(root, newRoot):
            if root == None:
                return
                
            # newRoot是True意味着上一个node是delete，现在的root就是新的root
            # 但是 还需要判读现在的root是否是被删除的root
            if newRoot:
                res.append(root)
            if root.val in to_delete:
                newRoot = True
            else:
                newRoot = False
            
            root.left = findRoots(root.left, newRoot)
            root.right = findRoots(root.right, newRoot)
            if newRoot:
                return None
            return root

        res = []
        to_delete = set(to_delete)
        findRoots(root, True)
        return res
