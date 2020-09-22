#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/06


'''
I.Clarify
    to check the Tree is balanced or not
    balanced BT == Height difference between left and right does not exceed 1
    任何一个node都要符合条件 Any node must meet the condition
    ThreeNode was defined? Yes
    
    input: root: TreeNode 
    output: bool
    corner case: root == None --> return True
    
    
II. Methods
    A. DFS
    Steps:
        1. make a helper function to count the node's depth
            a. ending condition: root 
            b. depth = max(left, right) + 1
        2. check how many different with left depth and right depth
        3. repeat step1 and step2 for each node
    Complexity:
        Time: worse O(N**2)
        Space: O(logN) worse O(N) if the tree is skewed

    B. DFS (Optimization) from 李厨子
    Steps: 
        1. use self.res to memo the difference between the left depth and right depth of each node
        2. make a helper function to count the node's max depth
            a. ending condition: root 
            b. check the gap between left depth and right depth, if more than 1, self.res = False
            c. depth = max(left, right) + 1
        3. return self.res
    
    Complexity:
        Time: worse O(N)
        Space: O(logN) worse O(N) if the tree is skewed

    
        
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# A
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        def helper(root):
            if root == None:
                return 0
            return max(helper(root.left), helper(root.right)) + 1
        
        
        if abs(helper(root.left) - helper(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


# B
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        self.res = True  # 全局可用
        def helper(root):  # count the max depth of node
            if root == None:
                return 0
            
            l = helper(root.left)
            r = helper(root.right)
            
            if abs(l - r) > 1:
                self.res = False
            return max(l, r) + 1
        
        helper(root)
        return self.res
