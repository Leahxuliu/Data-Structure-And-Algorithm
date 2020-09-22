#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/04  
# @Author  : XU Liu
# @FileName: Binary_Tree_Level_Order_Traversal_102.py

'''
1. 题目要求：
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

2. 理解：
输出node val，每一层的val放在一个list里

3. 题目类型：
BT，遍历

4. 输出输入以及边界条件：
input: treenode
output: list[int]
corner case: root == None

5. 解题思路
    1. BFS遍历
    2. 建立一个for循环，遍历一层的值，然后把每一层的值储存在一起

'''

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        nodes_all = []
        
        if root == None:
            return nodes_all
        
        queue = deque()
        queue.append(root)
        
        while queue:
            lenth = len(queue)
            
            level_nodes = []
            for i in range(lenth):
                node = queue.popleft()
                level_nodes.append(node.val)
                
                if node.left != None:
                    queue.append(node.left)
                    
                if node.right != None:
                    queue.append(node.right)
            nodes_all.append(level_nodes)
        return nodes_all