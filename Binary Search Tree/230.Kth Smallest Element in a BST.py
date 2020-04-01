# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/01  
# @Author  : XU Liu
# @FileName: 230.Kth Smallest Element in a BST.py

'''
1. 题目类型：
    BST

2. 题目要求与理解：
   找到第k小的数 

3. 解题思路：
    中序遍历
    找到第k个数

4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    Time: O(H + K), H is height of tree used by add all left node in stack, then do k times to find kth element 
          in average, H is logN, N is number of nodes, in worst case H is N for skewed tree
    space: O(H + k), in worst case, O(N + k), average O(logN + k)
    ?????????

'''

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root == None:
            return None
        
        n = 0
        stack = []
        pre = float('-inf')
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
                
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            
            pre = cur.val
            if cur.right != None:
                root = cur.right
        return None

'''
简化
不需要pre
'''
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root == None:
            return None

        # 中序遍历二叉树
        stack = []
        p_node = root

        while stack or p_node:
            while p_node:
                stack.append(p_node)
                p_node = p_node.left

            cur_node = stack.pop()
            
            # 返回第k个元素
            k -= 1
            if k == 0:
                return cur_node.val

            if cur_node.right != None:
                p_node = cur_node.right