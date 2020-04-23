#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/04  
# @Author  : XU Liu
# @FileName: 257.Binary Tree Paths.py

'''
1. 题目要求：


2. 理解：


3. 题目类型：


4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 解题思路
    

'''

#DFS
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        def dfs(root, path):
            if root == None:
                return
            
            if root.left == None and root.right == None:
                path += str(root.val)
                path_all.append(path)
            
            dfs(root.left, path+str(root.val)+'->' )  # 注意'->'加在的位置，易错! 中间要有'->',结尾不能有
            dfs(root.right, path+str(root.val)+'->' )
        
        path = ''
        path_all = []
        dfs(root, path)
        
        return path_all


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return 
        
        def dfs(root, path):
            
            if root.left != None:
                dfs(root.left, path + [str(root.left.val)])
            if root.right != None:
                dfs(root.right, path + [str(root.right.val)])                
                
            if root.right == None and root.left == None:
                all_path.append('->'.join(path)) 
        
        all_path = []
        dfs(root, [str(root.val)])
        
        return all_path


#BFS
from collections import deque
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        path_all = []
        if root == None:
            return  path_all
        
        queue = deque()
        path = ''
        queue.append([root, path])

        while queue:
            node, path = queue.popleft()
            path += str(node.val) + '->'

            if node.left == None and node.right == None:
                path = path.rstrip('->')
                path_all.append(path)

            if node.left != None:
                queue.append([node.left, path])
            if node.right != None:
                queue.append([node.right, path])
        
        return path_all
    
    
# 回溯
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return 
            
        def helper(root, path):
            if root == None:
                return 
            
            if root.left == None and root.right == None:
                all_path.append('->'.join(path[:]))
                return all_path
                
            for node in (root.left, root.right):
                if node:
                    path.append(str(node.val))
                    helper(node, path)
                    path.pop()
                
        all_path = []
        helper(root, [str(root.val)])
        return all_path
