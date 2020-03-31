# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/31  
# @Author  : XU Liu
# @FileName: 700.Search in a Binary Search Tree.py

'''
1. 题目类型：
    BST

2. 题目要求与理解：
    最最最普通的查找

3. 解题思路：


4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    

'''

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None
        
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
        return None


# 递归的速度更快
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        
        if root.val < val:
            return self.searchBST(root.right, val)
        if root.val > val:
            return self.searchBST(root.left, val)