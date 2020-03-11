#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/04  
# @Author  : XU Liu
# @FileName: Binary_Tree_Postorder_Traversal_145.py

'''
1. 题目要求：
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

2. 理解：
按层遍历，先出最下层的结果

3. 题目类型：
BT，遍历

4. 输出输入以及边界条件：
input: treenode
output: list[int]
corner case: root == None

5. 解题思路
    1. BFS 按层遍历
    2. list[::-1]

'''

from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        all_nodes = []
        
        if root == None:
            return all_nodes
        
        queue = deque()
        queue.append(root)
        
        while queue:
            level_nodes = []
            q_len = len(queue)
            
            for i in range(q_len):
                node = queue.popleft()
                level_nodes.append(node.val)
                
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            all_nodes.append(level_nodes)
        return all_nodes[::-1]