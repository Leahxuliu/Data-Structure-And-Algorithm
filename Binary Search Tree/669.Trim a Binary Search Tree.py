# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/30  
# @Author  : XU Liu
# @FileName: 669.Trim a Binary Search Tree.py

'''
1. 题目类型：
    BST

2. 题目要求与理解：
    Trim a Binary Search Tree（修剪树）
    给定一个二叉搜索树，同时给定最小边界 L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在 [L, R] 中 (R>=L) 

3. 解题思路：
    对比R, L, root之间的大小关系，类似二分法里找一定范围内的值
    用recursion
    a. end: root is None
    b. R < root.val --> 留下left subtree, 缩小范围
    c. l > root.val --> 留下right subtree, 缩小范围
    d. L <= root val and R >= root.val --> 留下both sides of the tree


4. 输出输入以及边界条件：
input: root: TreeNode, L: int, R: int
output: TreeNode
corner case: None

5. 空间时间复杂度
    

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root == None:
            return None
        
        if R < root.val:
            return self.trimBST(root.left, L, R)
        elif L > root.val:
            return self.trimBST(root.right, L, R)
        elif L <= root.val and R >= root.val:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root