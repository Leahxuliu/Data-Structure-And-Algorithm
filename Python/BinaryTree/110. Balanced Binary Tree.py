#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/04  
# @Author  : XU Liu
# @FileName: 110. Balanced Binary Tree.py

'''
1. 题目要求：
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


2. 理解：
左右两边不超过1个高度

3. 题目类型：
BT，性质

4. 输出输入以及边界条件：
input: TreeNode
output: bool
corner case:  root == None --> false
'''


'''
方法 1：自顶向下暴力递归 top-down-dfs
    1. 当前节点的最大深度(depth) 
    2. 比较左右子树最大高度差
        abs(self.depth(root.left) - self.depth(root.right))

    main function: 
        scan every node, while compare max height of every node's subtree by DFS or BFS
    helper function: 
        calculate the max height of a root by DFS or BFS
    time complex:
        skewed tree: O(N*N) why？？？
        average:O(N) 
    space complex: 
        O(logN)
        哥哥的答案：O(N) why???
'''

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True

        # 当前节点满足平衡树，继续递归判断子树是否满足平衡树条件
        if abs(self.depth(root.left)-self.depth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def depth(self, root):
        if root == None:
            return 0
        if root.left ==  None and root.right == None:
            return 1
        
        if root.left != None or root.right != None:
            return 1+max(self.depth(root.left),self.depth(root.right))

            

'''
方法2
判读该node的left与right的depth差是否超过1
'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def DFS(root, depth):
            if root == None:
                return depth  # return 0是错的; 因为这里的depth是最底层的高度值，不是0
            return max(DFS(root.left, depth + 1), DFS(root.right, depth + 1))
        
        if root == None:
            return True
        if abs(DFS(root.right, 0) - DFS(root.left, 0)) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        def check(root):
            nonlocal res
            if root == None:
                return 0
            
            l = check(root.left)
            r = check(root.right)
            if abs(l - r) > 1 and res:
                res = False
            return max(l, r) + 1

        res = True
        check(root)
        return res