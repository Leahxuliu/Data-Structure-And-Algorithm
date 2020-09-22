#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/11

from collections import deque
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        queue = deque()
        num = 0
        
        queue.append(root)
        while queue:
            node = queue.popleft()
            num += 1
            
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return num