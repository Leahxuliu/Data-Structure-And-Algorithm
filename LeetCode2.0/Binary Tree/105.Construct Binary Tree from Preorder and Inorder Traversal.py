#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/06


'''
I. Clarify:
    use preorder and inorder to build a binary tree
    TreeNode was defined? Yes
    
    input: two list[int]; length range if 0 to 10**5; 
    output: TreeNode root
    corner case: len(list) == 0 --> return None
    
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# A
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root

#########################################################################################

# B
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def dfs(pre_left,pre_right,in_left,in_right):
            if len(preorder) == 0:
                return None
            
            root = TreeNode(preorder[0])
            mid = inorder_info[preorder[0]]

            root.left = self.buildTree(pre_left+1,pre_left+1+mid-in_left,in_left,mid)  # 难点
            root.right = self.buildTree(pre_left+1+mid-in_left,pre_right,mid+1,in_right)
            return root
        
        inorder_info = {each:i for i, each in enumerate(inorder)}

        root = dfs(0,len(preorder),0,len(inorder))
        return root