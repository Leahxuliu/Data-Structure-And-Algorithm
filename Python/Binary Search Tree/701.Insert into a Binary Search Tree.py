# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/31  
# @Author  : XU Liu
# @FileName: 701.Insert into a Binary Search Tree.py

'''
1. 题目类型：
    BST


2. 题目要求与理解：
    典型插入题
    没有重复的数，要插入的数也不存在于已有的tree里面


3. 解题思路：


4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    

'''

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        
        def insert(root):
            if root == None:
                return TreeNode(val)
            
            if root.val < val:
                root.right = insert(root.right)
            else:
                root.left = insert(root.left)

            return root
                    
        insert(root)
        return root


from collections import deque
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()

            if node.val < val:
                if node.right:
                    queue.append(node.right)
                else:
                    node.right = TreeNode(val)
                    break
            else:
                if node.left:
                    queue.append(node.left)
                else:
                    node.left = TreeNode(val)
                    break
        return root