#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/16


'''
input: root: distinct value

Method - DFS + BFS
1. traverse nodes by using BFS and used list
2. if node not in used list, DFS(root) --> return new root
   ending codition: if node.val in to_delete, return None; if node == None, return 
   root.left = DFS(root.left)
   root.right = DFS(root.right)

此方法错误
因为DFS return new root的同时，已经更改了原有的root
再用bfs遍历树是不可行的
如单边树:
[1,null,2,null,3,null,4]
[3]

按以下写法 输出[[1,null,2]]
然而正确答案是[[1,null,2],[4]]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if TreeNode == None:
            return []
        
        def DFS(root):
            if root == None:
                return 
            if root.val in to_delete:
                return None
            
            root.left = DFS(root.left)
            root.right = DFS(root.right)
            used.append(root.val)
            return root
        
        res = []
        used = []
        queue = deque()
        queue.append(root)
        while queue:
            print(queue)
            root = queue.popleft()
            if root.left != None:
                queue.append(root.left)
            if root.right != None:
                queue.append(root.right)
            
            if root.val not in used and root.val not in to_delete:
                res.append(DFS(root))
        return res


'''
正确
'''
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def helper(root, is_root):
            if root == None:
                return 
            if root.val in to_delete:
                flag = True
            else:
                flag = False
            
            if is_root == True and flag == False:
                res.append(root)
            
            root.left = helper(root.left, flag)
            root.right = helper(root.right, flag)
            
            if flag == True:
                return None
            else:
                return root
        
        
        res = []
        helper(root, True)
        return res