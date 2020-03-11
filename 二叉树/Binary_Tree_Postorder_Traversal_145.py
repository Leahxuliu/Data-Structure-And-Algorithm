#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/04  
# @Author  : XU Liu
# @FileName: Binary_Tree_Postorder_Traversal_145.py

'''
1. 题目要求：
Given a binary tree, return the postorder traversal of its nodes' values.

2. 理解：
按left，right，root的顺序，遍历树

3. 题目类型：
BT里面的遍历

4. 输出输入以及边界条件：
input: tree
output: list
corner case: root == None

5. 解题思路
    1. using DFS to traversal the tree
    2. 用一个list来储存遍历的值,需要一个helper函数

'''

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        if root == None:
            return nodes
        
        self.postorder(root, nodes)  # 容易忘记写！！！
        return nodes
        
    def postorder(self, root, nodes):  # 注意对齐！！！
        if root.left != None:
            self.postorder(root.left, nodes)

        if root.right != None:
            self.postorder(root.right, nodes)

        nodes.append(root.val)
