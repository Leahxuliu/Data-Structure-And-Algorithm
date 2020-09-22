#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/18  
# @Author  : XU Liu
# @FileName: 

'''
1. 题目要求：
    判断是不是对称树

'''

'''
方法一
错误
思路：
BFS按层遍历，记录每一层的value，然后用对撞指针判读这一层数值是不是对称的

错误原因：
没有考虑到[None, 3, None, 3]的情况
因为记录值的时候，[3,3]
误以为是对称的

from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        queue = deque()
        queue.append(root)
        
        while queue:
            q_len = len(queue)
            level = []
            for i in range(q_len):
                node = queue.popleft()
                level.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            l = 0
            r = q_len - 1
            while l < r:
                if level[l] != level[r]:
                    return False
                else:
                    l += 1
                    r -= 1
        return True

'''

'''

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        def DFS(t1,t2):
            
            if t1 == None and t2 == None:  
                return True
            if t1 == None or t2 == None:  # 不能先写这个！ t1 == None , t2 == None, 也符合该if条件！！！
                return False
            if t1.val != t2.val:
                return False
            if t1.val == t2.val:
                return DFS(t1.left, t2.right) and DFS(t1.right, t2.left)
            
        return DFS(root.left, root.right)