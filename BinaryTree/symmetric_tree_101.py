# -*- coding: utf-8 -*-
# @Time    : 2/27/2020  
# @Author  : XU Liu
# @FileName: symmetric_tree_101.py

import constructTree
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == '__main__':
    root = constructTree.constructTree([9,-42,-42,None,76,76,None,None,13,None,13])
    class Solution(object):
        def isSymmetric(self, root):
            
            if root == None:
                return True
            
            return self.isMirror(root.left, root.right)

        def isMirror(self, n1, n2):
            if n1 == None and n2 == None:
                return True
            
            elif n1 == None or n2 == None:
                return False
            
            elif n1.val != n2.val:
                return False
            
            else:
                return self.isMirror(n1.left,n2.right) and self.isMirror(n1.right,n2.left)
                
        resurt = isSymmetric(root)
        print(resurt)

    