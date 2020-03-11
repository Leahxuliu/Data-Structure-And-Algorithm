#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/04  
# @Author  : XU Liu
# @FileName: 108. Convert Sorted Array to Binary Search Tree.py

'''
1. 题目要求：
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
一个高度平衡二叉树是指一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1。

2. 理解：
一个高度平衡的二叉树，遍历之后得出的list，是升序排列 --> 中序遍历
平衡树 --> list的中间点是根结点
输出一种可能性就可以

3. 题目类型：
BST，构造

4. 输出输入以及边界条件：
input: list[int] array
output: treenode
corner case: 

5. 解题思路
    1. DFS inorder
    2. inorder左右边界
    3. 中点是root

难点：
中间点index： len(num) // 2
特例，len(num) == 1  --> num[0] 
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums == []:
            return None
        
        if len(nums) == 1:
            root = TreeNode(nums[0])
            
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root