#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/27

'''recursion: depth first search
time complexity: O(N) N is the number of treenodes; scan every nodes
space complexity:average O(logN) logN is the most depth of the tree; the stack is used by recursion  
                 worse O(N)
'''
class Solution:
    def inorderTraversal(self, root):
        if root == None:
            return []

        def helper(root):
            if root == None:
                return 
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        res = []
        helper(root)
        return res


'''
dfs: use stack to simulate recursion
iteration will more efficence than recursion

'''

class Solution:
    def inorderTraversal(self, root):
        if root == None:
            return []

        stack = []
        res = []
        p_node = root
        while p_node or stack:
            while p_node:
                stack.append(p_node)
                p_node = p_node.left
            node = stack.pop()
            res.append(node.val)
            if node.right:
                p_node = node.right

        return res


# 用迭代写前序


# 用迭代写后序