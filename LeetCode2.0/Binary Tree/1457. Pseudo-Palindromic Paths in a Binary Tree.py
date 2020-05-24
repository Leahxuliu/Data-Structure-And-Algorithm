#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/24

'''
Method - DFS
Steps:
    1. use dfs help function to find all path
    2. check the path can be Palindromic or not
    3. choose the max one

Time: O(N + MlogN) scan the nodes + check the path is Palindromic or not
Space:O(N) store the paths
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        
        # find all paths
        def dfs(root, path):
            path.append(root.val)
            if root.left == None and root.right == None:
                all_path.append(path[:])
            
            if root.left != None:
                dfs(root.left, path[:])
            if root.right!= None:
                dfs(root.right, path[:])
        
        # check the path is Palindromic or not
        def check(path):  # True is Palindromic
            odd_num = 0
            for i in range(1, 10):
                if path.count(i) % 2 == 1:  # dict更好 maybe
                    odd_num += 1
                if odd_num > 1:
                    return False
            return True
            
        all_path = []
        dfs(root, [])
        return sum(check(each_path) for each_path in all_path)
            
