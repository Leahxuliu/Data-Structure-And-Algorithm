#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/04  
# @Author  : XU Liu
# @FileName: 

'''
1. 题目要求：


2. 理解：
node1.next = node2
中间有None的话 node1.next = node3

3. 题目类型：
BT，遍历

4. 输出输入以及边界条件：
input: root
output: root
corner case: root == None 

5. 解题思路
    while下面再用一个for，按层遍历

'''

from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        res = root
        
        if root == None:
            return res
        
        queue = deque()
        queue.append(root)
        
        while queue:
            q_len = len(queue)
            
            for i in range(q_len - 1):
                queue[i].next = queue[i+1]
            queue[q_len - 1].next = None
            
            for i in range(q_len):
                node = queue.popleft()
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        return res