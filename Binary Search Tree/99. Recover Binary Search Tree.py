# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/28 


'''
A. Brute force
1. taverse the tree inorder and save val into list
2. find the two swaped value in list
3. taverse the tree again and change the swaped nodes

Time: O(N + N + N)
Space: O(N)

B. Itervation + inorder
    a. 中序遍历
    b. 错误交换的点是相邻的（中序遍历结果 1324）：使用 first 和 second 表示错误交换的两个点，在第一次遇到不递增的情况时，将 first 置为 3，second 置为 2，遍历结束后交换 first 与 second。
    c. 错误交换的点是不相邻的（中序遍历结果 3214）：在第一次遇到不递增的情况时，将 first 设置为 3，second 设置为 2，在第二次遇到不递增的情况时，只改变 second，将 second 置为 1. 遍历结束后交换 first 与 second。
       遍历结果：   4     2     3     1
                 pre   cur   pre    cur
                first              second

Time: O(N)
Space: O(H) H is height of tree, average value is O(logN)

C. recursion + inorder

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 迭代 中序遍历
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        p_node = root
        pre = TreeNode(float('-inf'))
        f = None
        s = None

        while stack or p_node:
            while p_node:
                stack.append(p_node)
                p_node = p_node.left

            curr = stack.pop()
            if curr.val > pre.val:
                pre = curr
            else:
                if f == None:
                    f = pre
                    s = curr
                else:
                    s = curr
            pre = curr

            if curr.right:
                p_node = curr.right
        
        f.val, s.val = s.val, f.val