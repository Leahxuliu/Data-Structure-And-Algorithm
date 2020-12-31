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
    4. root.left = left, root.right = right,构成TreeNode

II. Methods: 
    A. DFS
    Steps:
        1. ending condition: preorder is [], return 
        2. root is preorder[0]
        3. find root in inorder (mid = inorder.index(preorder[0]))
        4. root.left = dfs(left tree pre order, left tree right order)  # preorder[1:mid + 1]  inorder[:mid]
           root.right = dfs(right tree pre order, left tree right order)  # preorder[mid + 1:]  inorder[mid + 1:]
     
    Complexity:
        Time:  O(N**2)  index查找O(N), N*N
        Space: O(N) since we store the entire tree
    
    
    B. DFS + dict (optimization)
    when we use index, the Time Complexity is O(n).
    put inorder into dict to reduce time complexity
    Steps:
        1. put inorder into dict
        2. same as methodI, except indext
        
    
    Complexity:
        Time: O(N)
        Space:O(N) since we store the entire tree
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
        
        
'''
DFS的优化
用哈希表（字典）来存储中序遍历，这样就可以在 O(1) 时间复杂度下找到根结点在中序遍历数组中的索引
哈希表仅仅建立一次，后续递归中每次都能有直接调用
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder == []:
            return None
        
        def DFS(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
            
            temp = preorder[pre_start]
            root = TreeNode(temp)
            mid = info[temp]

            # 先写头和尾，不需要改变或者只需要+-1的
            # 通过len(preorder) = len(inorder)来计算中间值， 即通过in_end - in_start = pre_end - pre_start来计算
            root.left = DFS(pre_start + 1, pre_start - in_start + mid, in_start, mid - 1)
            root.right = DFS(pre_start - in_start + mid + 1, pre_end, mid + 1, in_end)
            return root
        
        info = {each:i for i, each in enumerate(inorder)}
        return DFS(0, len(preorder) - 1, 0, len(inorder) - 1)