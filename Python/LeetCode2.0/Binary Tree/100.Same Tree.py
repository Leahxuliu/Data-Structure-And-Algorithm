#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/18

'''
Method
A. BFS
    1. use BFS to traverse nodes
    2. store [p1, p2] into queue
        popleft queue --> N1, N2
        if N1 == None and N2 == None, continue
        if N1 == None or N2 == None, return False
        if N1.val != N2.val, return False
        if N1.val == N2.val, put [N1.left, N2.left] and [N1.right, N2.left] into queue
        repeat step2
    3. return True

Time: O(N) N: the number of nodes; scan every nodes
Space: O(N/2) the max width in tree; store nodes into queue


B. DFS
Steps:
    1. use dfs to traverse nodes
    2. corner case: 
        if p == None and q == None, return True
        if p == None or q == None, return False
    3. if p.val != q.val, return False
       if p.val == q.val, return self.def(p.left, q.left) and self.def(p.right, q.right)

Time: O(N)
Space:O(logN)
'''

# BFS
from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        
        queue = deque()
        queue.append([p, q])
        while queue:
            n1, n2 = queue.popleft()
            if n1 == None and n2 == None:
                continue
            elif n1 == None or n2 == None:
                return False
            elif n1.val != n2.val:
                return False
            elif n1.val == n2.val:
                queue.append([n1.left, n2.left])
                queue.append([n1.right, n2.right])
        return True

# DFS
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)