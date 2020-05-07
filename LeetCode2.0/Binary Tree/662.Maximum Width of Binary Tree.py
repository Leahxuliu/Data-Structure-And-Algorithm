#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/06 


'''
I. Clarify
    to find Maximum Width
    the width between most left node and most right node, including None
    
    input:root:TreeNode; the length range is from 0 to ?
    output:int
    corner case: root == None
    
II. Method 
    A. BFS
    Steps:
        1. use a queue to store node and the index of the node
        2. the index of root is n (start at 0), left child is 2n + 1, right child is 2n + 2
        3. width = right - left + 1
        4. each loop for one level
    
    Complexity:
        Time: O(N)  N is the number of nodes
        Space: O(N/2) the widest breadth
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        queue = deque()
        queue.append([root, 0])
        width = 0
        
        while queue:
            len_q = len(queue)
            width = max(width, queue[-1][1] - queue[0][1] + 1)
            
            for i in range(len_q):
                node, index = queue.popleft()
                if node.left != None:
                    queue.append([node.left, index * 2 + 1])
                if node.right != None:
                    queue.append([node.right, index * 2 + 2])
        return width