#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/06 

'''
I.Clarify
    Determine if there is a path and equal to sum

    input: root: TreeNode  None?  sum:int the value of sum is 0 to ?
    output: bool
    corner case: root == None --> return False
    
II.Method
    A. DFS (find all path sum)
    Steps:
        1. make a helper function(DFS) to count all path sum
            a. ending condition: root == None
            b. when left is None and right is None, add the path sum
        2. determine the sum in the all path or not
    Complexity:
        Time: O(N)
        Space: O(logN + N)
        
    B. DFS (renew sum)
    Steps:
        1. ending condition: root == None
        2. use self function to renew the sum, sum - root.val
        3. when left is None and right is None and sum = root.val, return True
    Complexity:
        Time: O(2N)
        Space: O(logN)
        
    C. BFS
    Steps:
        1. ues queue to store the node and the path sum
        2. when left is None and right is None and Sum = sum, return True
    Complexity:
        Time: O(N)
        Space: O(N)
        
    D. Backtrack (有头版)
    Steps:
        1. use the backtrack to choose the node
        2. use self.res to store the res
        3. when left is None and right is None and Sum = sum, return True
    
    Complexity:
        Time: O(N)
        Space: O(logN)  worse O(N)
        
    E.Backtrack (无头版)
    Steps:
        1. 
    
    Complexity:
        Time: O(N)
        Space: O(logN)  worse O(N)
    

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# A 
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        
        all_sum = []
        def helper(root, Sum):
            if root == None:
                return 
            
            if root.left == None and root.right == None:
                return all_sum.append(Sum + root.val)
            
            Sum = Sum + root.val
            
            helper(root.left, Sum)
            helper(root.right, Sum)
            
        helper(root, 0)
        if sum in all_sum:
            return True
        else:
            return False

# B
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None and sum == root.val:
            return True
        
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


# C
from collections import deque
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        
        queue = deque()
        queue.append([root, 0])
        
        while queue:
            node, Sum = queue.popleft()
            Sum = Sum + node.val
            
            if node.left == None and node.right == None and Sum == sum:
                return True
            
            if node.left != None:
                queue.append([node.left, Sum])
            if node.right != None:
                queue.append([node.right, Sum])
        return False

# D
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        self.res = False
        def backtrack(root, sum):
            if root == None:
                return

            if root.left == None and root.right == None and sum == root.val:
                print(sum)
                self.res = True
                return

            sum = sum - root.val
            backtrack(root.left, sum)
            backtrack(root.right, sum)
            sum = sum + root.val
        
        backtrack(root, sum)
        return self.res


# E
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        
        self.res = False
        def backtrack(root, sum):
            if root.left == None and root.right == None and sum == 0:
                self.res = True
                return
            for node in (root.left, root.right):
                if node:
                    sum = sum - node.val
                    backtrack(node, sum)
                    sum = sum + node.val
        
        backtrack(root, sum - root.val)
        return self.res