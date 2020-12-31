#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/04  
# @Author  : XU Liu
# @FileName: 113.Path Sum II

'''
1. 题目要求：
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

2. 理解：
找到所有等于sum的路径

3. 题目类型：
BT，路径和
'''

import constructTree
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


# Backtracking 
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



if __name__ == '__main__':
    #root = constructTree([1,2,3,4,None,5])
    root = constructTree.constructTree([5,4,8,11,None,13,4,7,2,None,None,5,1])
    sum = 22

    result = Solution()
    print(result.pathSum2(root, sum))