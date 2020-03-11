#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2/27/2020  
# @Author  : XU Liu
# @FileName: max_wight.py

import constructTree
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxWight(self, root):
        max_len = 0
        if root == None:
            return max_len
        
        queue = deque()
        queue.append(root)

        while queue:
            q_len = len(queue)
            max_len = max(max_len, q_len)
            for i in range(q_len):
                node = queue.popleft()

                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)

        return max_len


if __name__ == "__main__":
    root = constructTree.constructTree([1,2,3,4,5,6,7,None,None,12])

    result = Solution()
    print(result.maxWight(root))

    