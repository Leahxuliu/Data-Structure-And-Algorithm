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

先写头和尾，不需要改变或者只需要+-1的
通过len(preorder) = len(inorder)来计算中间值， 即通过in_end - in_start = post_end - post_start来计算
'''


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder == []:
            return None
        
        def DFS(in_start, in_end, post_start, post_end):
            if in_start > in_end:
                return None
                
            temp = postorder[post_end]
            root = TreeNode(temp)
            mid = inorder.index(temp)

            root.left = DFS(in_start, mid - 1, post_start, mid - 1 - in_start + post_start)
            root.right = DFS(mid + 1, in_end, mid - 1 - in_start + post_start + 1,post_end - 1)
            return root
        
        info = {each:i for i, each in enumerate(inorder)}
        return DFS(0, len(inorder) - 1, 0, len(postorder) - 1)
