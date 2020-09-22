#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/30


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        def helper(l, r):
            if l == None and r == None:
                return True
            if l == None or r == None:
                return False
            if l.val != r.val:
                return False
            
            return helper(l.left, r.right) and helper(l.right, r.left)

        return helper(root.left, root.right)