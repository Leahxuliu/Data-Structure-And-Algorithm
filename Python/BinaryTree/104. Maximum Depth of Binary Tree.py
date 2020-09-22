#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/18  
# @Author  : XU Liu
# @FileName: 104. Maximum Depth of Binary Tree.py

'''
1. 题目要求：
    判断是不是对称树

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
方法一
DFS
time complex: O(N)
space complex: worst O(N), average O(logN)

'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def DFS(root, depth):
            if root == None:
                return depth  # return 0是错的; 因为这里的depth是最底层的高度值，不是0
            return max(DFS(root.left, depth + 1), DFS(root.right, depth + 1))
            '''
            if root == None:
                return 0
            return max(DFS(root.left, depth), DFS(root.right, depth)) + 1
            '''
        return DFS(root, 0)


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right: 
            return 1

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) # get the longest one by df

'''
方法2
BFS
time complex: O(N)
space complex: best O(1) average O(N)
'''

from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:  # corner case
            return 1

        queue = deque()
        queue.append([root, 0])
        max_depth = 0

        while queue:  # bfs scan and record
            node, height = queue.popleft()
            height += 1
            if not node.left and not node.right:  # must have subtree, it can add one
                max_depth = max(height, max_depth)
            if node.left:
                queue.append([node.left, height])
            if node.right:
                queue.append([node.right, height])
        return max_depth

'''
方法三
BFS
'''
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        queue = deque()
        queue.append(root)
        res = 0
        while queue:
            q_len = len(queue)
            for i in range(q_len):
                node = queue.popleft()
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            res += 1
        return res


'''
错误
易错
注意
'''
while queue:
    depth += 1
    while queue:
        node = queue.popleft()
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)

# depth 永远都是1，因为出来的同时，还在不停的往里面加新的
