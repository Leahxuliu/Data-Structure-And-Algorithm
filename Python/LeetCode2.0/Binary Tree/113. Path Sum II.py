#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/30

# BFS

from collections import deque
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        
        all_path = []
        queue = deque()
        queue.append([root, [], sum])

        while queue:
            node, path, sum = queue.popleft()
            path.append(node.val)
            sum -= node.val
            if node.left == None and node.right == None and sum == 0:
                all_path.append(path[:])
            
            if node.left != None:
                queue.append([node.left, path[:], sum])
            if node.right != None:
                queue.append([node.right, path[:], sum])
        
        return all_path

# DFS
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        
        def findAllPath(root, path):
            path.append(root.val)
            if root.left == None and root.right == None:
                all_path.append(path[:])
                return 
            
            if root.left != None:
                findAllPath(root.left, path[:])
            if root.right != None:
                findAllPath(root.right, path[:])


        all_path = []
        res = []
        findAllPath(root, [])
        for each_path in all_path:
            temp = 0
            for i in each_path:
                temp += i
            if temp == sum:
                res.append(each_path)
        return res

# DFS 改进版
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        
        def findAllPath(root, path, sum):
            path.append(root.val)
            sum -= root.val
            if root.left == None and root.right == None:
                if sum == 0:
                    all_path.append(path[:])
                return 
            
            if root.left != None:
                findAllPath(root.left, path[:], sum)
            if root.right != None:
                findAllPath(root.right, path[:], sum)


        all_path = []
        findAllPath(root, [], sum)
        return all_path


# Backtracking 最快
# Time O(N)

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []

        def Backtracking(root, path, sum):
            path.append(root.val)
            sum -= root.val
            if root.left == None and root.right == None and sum == 0:
                all_path.append(path[:])

            if root.left != None:
                Backtracking(root.left, path, sum)
            if root.right != None:
                Backtracking(root.right, path, sum)

            sum += path[-1]
            path.pop()
        
        all_path = []
        Backtracking(root, [], sum)
        return all_path
