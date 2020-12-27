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


Method - BFS
Steps:
    1. use queue to store nodes of each level
    2. make the node have next property
    3. pop last level's nodes and append next level's nodes
    

'''

from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue = deque()
        curr = root
        queue.append(curr)

        while queue:
            n = len(queue)
            for i in range(n):
                curr = queue.popleft() 
                if i == n - 1:
                    curr.next = None
                else:
                    curr.next = queue[0]
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root
        

'''
DFS
because this is a perfect binary tree, root.right.next = root.next.left
自上而下
'''

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        if root.left:
            root.left.next = root.right

        if root.right:
            if root.next:
                root.right.next = root.next.left
            # node 自带next，什么都不做时，node.next == None
            # 所以下面可写可不写
            #else:
            #    root.right.next = None
        
        root.left = self.connect(root.left)
        root.right = self.connect(root.right)
        return root