#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/04  
# @Author  : XU Liu
# @FileName: 

'''
1. 题目要求：
Given preorder and inorder traversal of a tree, construct the binary tree.

2. 理解：
通过preorder和inorder来构建树

3. 题目类型：
BT，构建

4. 输出输入以及边界条件：
input: 两个list[int]
output: treenode
corner case: len(list) == 0 --> None

5. 解题思路
    1. preorder[0]: root
    2. inorder: root之前的是左边的
                root之后的是右边的
                记录找到第一个与root相等的数所在位置,mid
    3. preorder[1:mid+1]是root的左边，并且该list里面的第一位数，是下一个root
    4. root.left = left, root.righr = right,构成TreeNode

'''

'''
DFS
时间复杂度： O (N^2)，这里 N 是二叉树的结点个数，每调用一次递归方法创建一个结点，一共创建 N 个结点，在中序遍历中找到根结点在中序遍历中的位置，是与 N 相关的，这里不计算递归方法占用的时间。
空间复杂度： O (1)
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        '''
        易错
        root = preorder[0]
        mid = inorder.index(root)
        '''
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
        
        
'''
DFS的优化
用哈希表（字典）来存储中序遍历，这样就可以在 O(1) 时间复杂度下找到根结点在中序遍历数组中的索引
哈希表仅仅建立一次，后续递归中每次都能有直接调用
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def dfs(pre_left,pre_right,in_left,in_right):
            if len(preorder) == 0:
                return None
            
            root = TreeNode(preorder[0])
            mid = inorder_info[preorder[0]]

            # 更新前序遍历、中序遍历边界，然后递归构建左右子树
            # 我们可以通过“前序和中序个数是相同”这个隐含条件，求出前序左右边界
            root.left = self.buildTree(pre_left+1,pre_left+1+mid-in_left,in_left,mid)  # 难点
            root.right = self.buildTree(pre_left+1+mid-in_left,pre_right,mid+1,in_right)
            return root
        


        inorder_info = {}
        for i, each in enumerate(inorder):
            inorder_info[each] = (i)  # key: node.val, value: index
        # 这三行可简写成：
        # inorder_info = {each:i for i, each in enumerate(inorder)}

        root = dfs(0,len(preorder),0,len(inorder))
        return root