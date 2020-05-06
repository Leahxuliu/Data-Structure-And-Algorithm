#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/06 

'''
利用BFS和node之间的index关系构造二叉树

parent: n (start at 0)
left child: 2n + 1
right chile: 2n + 2
'''

from collections import deque

# define TreeNode
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# construct the Binary Tree
class BinaryTree:
    def constructBT(self, nodeList):
        if nodeList == None:
            return
        
        root = TreeNode(nodeList[0])
        queue = deque()
        queue.append([root, 0])
        while queue:
            node, index = queue.popleft()
            left_index = 2 * index + 1
            right_index = 2 * index + 2

            if left_index < len(nodeList):
                node.left = TreeNode(nodeList[left_index])
                queue.append([node.left, left_index])
            if right_index < len(nodeList):
                node.right = TreeNode(nodeList[right_index])
                queue.append([node.right, right_index])
        return root


X = BinaryTree()
print(X.constructBT([1,2,3,4,5]))