# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/30  
# @Author  : XU Liu
# @FileName: 235.Lowest Common Ancestor of a Binary Search Tree.py

'''
1. 题目类型：
    binary search tree (BST)

2. 题目要求与理解：
    find the lowest common ancestor (LCA) of two given nodes in the BST（最近公共祖先）
    对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）
    All of the nodes' values will be unique

3. 解题思路：
       2
      / \
     0   4
        / \
        3  5  
    最近公共祖先的三种情况：
        case1.  0,5 --> 2
        case2.  2,4 --> 2
        case3.  0,2 --> 2
    具体步骤：
        1. 从root开始遍历数
        2. 如果节点p和节点q都在右子数上(p,q都比root大)，那么以右孩子为根节点继续遍历 
        3. 如果节点p和节点q都在左子数上(p,q都比root小)，那么以左孩子为根节点继续遍历
        4. 如果2，3条件都不成立，也就是找到p,q的LCA了 --> 本题的关键点，只要p,q不在一边，就是结果的节点

4. 输出输入以及边界条件：
input:  root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
output: 'TreeNode'
corner case: None

5. 空间时间复杂度
    

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root
        return None

# DFS
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)