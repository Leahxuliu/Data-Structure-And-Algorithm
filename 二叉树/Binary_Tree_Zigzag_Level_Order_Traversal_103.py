#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/04  
# @Author  : XU Liu
# @FileName: Binary_Tree_Postorder_Traversal_145.py

'''
1. 题目要求：
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

2. 理解：
traversal of the nodes like zigzag
right to left, left to right

3. 题目类型：
BT，遍历

4. 输出输入以及边界条件：
input: treenode
output: list[int]
corner case: root == None

5. 解题思路
错误！！！
    1. 用BFS遍历
    3. 奇偶层
    2. left to right: append left right
    3. right to left: append right left
    
    Time comple O(N)
    Space average O(N), best O(1)

    易错点：
    如果用了pop(), 就不能在用append从尾部加，因为加进去又会被立刻pop出来
    append right  再append left是错误的

正确：
    1. 用BFS正常遍历
    2. 把每一层值存储起来
    3. 偶数层的list，[::-1]
'''

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        node_all = []

        if root == None:
            return node_all
        
        queue = deque()
        level = 0
        queue.append(root)

        while queue:
            length = len(queue)
            level += 1
            level_nodes = []

            for i in range(length):
                node = queue.popleft()
                level_nodes.append(node.val)
                
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            
            if level % 2 == 0:
                node_all.append(level_nodes[::-1])
            else:
                node_all.append(level_nodes)
        return node_all



