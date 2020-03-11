#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/04  
# @Author  : XU Liu
# @FileName: 116. Populating Next Right Pointers in Each Node

'''
1. 题目要求：


2. 理解：
每一个node多一个性质，self.next = next
改变root

3. 题目类型：
BT，遍历

4. 输出输入以及边界条件：
input: node
output: [1,#,2,3,#,4,5,6,7,#]
corner case: root == None

5. 解题思路
    1. BFS遍历
    2. 通过上一层给下一层加东西

'''

from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        res = root
        
        if root == None:
            return  res
        
        queue = deque()
        queue.append(root)
        
        while queue:
            q_len = len(queue)
            for i in range(q_len - 1):
                queue[i].next = queue[i + 1]
            queue[q_len - 1].next = None
            
            for i in range(q_len):
                node = queue.popleft()
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                
        return res
        

