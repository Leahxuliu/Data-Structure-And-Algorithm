# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/01  
# @Author  : XU Liu
# @FileName: 99.Recover Binary Search Tree.py

'''
1. 题目类型：
    BST

2. 题目要求与理解：
    二叉搜索树中的两个节点被错误的交换，要求恢复

3. 解题思路：
    a. 中序遍历
    b. 错误交换的点是相邻的（中序遍历结果 1324）：使用 first 和 second 表示错误交换的两个点，在第一次遇到不递增的情况时，将 first 置为 3，second 置为 2，遍历结束后交换 first 与 second。
    c. 错误交换的点是不相邻的（中序遍历结果 3214）：在第一次遇到不递增的情况时，将 first 设置为 3，second 设置为 2，在第二次遇到不递增的情况时，只改变 second，将 second 置为 1. 遍历结束后交换 first 与 second。
       遍历结果：   4     2     3     1
                 pre   cur   pre    cur
                first              second

4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    

''' 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None

        pre = TreeNode(float('-inf'))  # 之后first要等于pre，所以每次保存pre都是treenode
        first = None
        second = None
        stack = []
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            cur = stack.pop()

            # 当遇到错误点时
            if cur.val <= pre.val:
                # 第一次遇到
                if first == None:
                    first = pre
                    second = cur
                # 第二次遇到
                else:
                    second = cur
            # 保存        
            pre = cur

            # 遍历right
            if cur.right != None:
                node = cur.right
        
        first.val, second.val = second.val, first.val

