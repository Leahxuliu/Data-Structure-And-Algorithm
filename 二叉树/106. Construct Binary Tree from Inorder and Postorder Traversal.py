#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/04  
# @Author  : XU Liu
# @FileName: 106. Construct Binary Tree from Inorder and Postorder Traversal.py

'''
1. 题目要求：


2. 理解：
通过给出的inorder和postorder构成树

3. 题目类型：
BT，构成

4. 输出输入以及边界条件：
input: list[int]
output: treenode
corner case: list == None

5. 解题思路
    1. dfs
    2. 难点以及易错点：
        root.left = self.buildTree(inorder[0:mid], postorder[0:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[0:mid], postorder[0:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        
        return root

'''
方法二 优化
把inorder放入字典
减少遍历次数

易错点
root.left = helper(iL, mid, pL, pR-iR+mid)
root.right = helper(mid+1, iR, pR-iR+mid, pR-1)
思路见笔记本
注意： （iL, iR, pL, pR) 指的是 index / index+1==len / index / index+1==len
'''


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(iL, iR, pL, pR):
            if iL==iR:
                return None
            root = TreeNode(postorder[pR-1])
            print(root.val)
            mid = info[postorder[pR-1]]

            root.left = helper(iL, mid, pL, pR-iR+mid)
            root.right = helper(mid+1, iR, pR-iR+mid, pR-1)
            return root
        
        info = {each_val:i for i, each_val in enumerate(inorder)}

        root = helper(0, len(inorder), 0, len(postorder))
        
        return root

