#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/04  
# @Author  : XU Liu
# @FileName: 

'''
1. 题目要求：


2. 理解：


3. 题目类型：
BT，遍历

4. 输出输入以及边界条件：
input: root
output: root
corner case: root == None 

5. 解题思路
Steps:
    0. traverse nodes in Tree
    1. use queue to store nodes in each level
    2. popleft nodes in last level and store nodes in next level
    3. make the node have the property of Node

'''

# 同116
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

'''
利用层次遍历的DFS来完成
DFS只是遍历
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        def DFS(root, depth):
            if not root:
                return 

            root.next = None
            if len(nodes) < depth + 1:
                nodes.append([root])
            else:
                nodes[depth][-1].next = root
                nodes[depth].append(root)
            
            DFS(root.left, depth + 1)
            DFS(root.right, depth + 1)
            return 
        
        nodes = []
        DFS(root, 0)
        return root

'''
DFS不仅仅是遍历
同时还改变了tree，直接返回root

'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        def DFS(root, depth):
            if not root:
                return root

            root.next = None
            if len(nodes) < depth + 1:
                nodes.append([root])
            else:
                nodes[depth][-1].next = root
                nodes[depth].append(root)
            
            root.left = DFS(root.left, depth + 1)
            root.right = DFS(root.right, depth + 1)
            return root
        
        nodes = []
        return DFS(root, 0)

'''
preorder 变换先right再left
'''


'''
创建dummy node
space O(1)
'''

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        
        dummy = Node()
        pre = dummy
        curr = root

        while curr:
            if curr.left:
                pre.next = curr.left
                pre = pre.next
            if curr.right:
                pre.next = curr.right
                pre = pre.next
            
            curr = curr.next

            if curr == None:
                curr = dummy.next
                dummy.next = None
                pre = dummy
        return root