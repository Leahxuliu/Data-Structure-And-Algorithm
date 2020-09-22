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

4. 输出输入
input: treenode, sum(int)
output: list[[int]]
corner case: root == None

5. 解题思路
    1. DFS
    2. 在path sum.py的基础上，加helper函数
    3. helper函数里面的结束条件：
        结束条件 1：如果当前节点是空的，则返回。
        结束条件 2：如果是叶子，那么如果剩余的 sum 等于当前叶子的值，则找到满足条件的路径，返回

    
    1. BFS
    2. 用deque来存储root，rum， path
    3. while之前用path_all来存储结果
    难点，怎么加path

'''

import constructTree
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 方法一
    def pathSum(self, root: TreeNode, sum: int):
        # helper函数
        def search(root, sum, path):
            if root == None:
                return
            if root.left == None and root.right == None and sum == root.val:
                    path.append(root.val)
                    path_all.append(path)
                    
            search(root.left, sum-root.val, path+[root.val])   # 不用写return
            search(root.right, sum-root.val, path+[root.val])

                    
        path = []
        path_all = []
        search(root, sum, path)
        return path_all

    

    # 方法二
    def pathSum2(self, root, sum):
        if root == None:
            return []
        
        path = []
        path_all = []
        queue = deque()
        queue.append([root, sum, path])
        
        while queue:
            node, sum, path = queue.popleft()
            sum -= node.val
            path.append(node.val)
            
            if node.left == None and node.right == None:
                if sum == 0:
                    path_all.append(path)
            if node.left != None:
                queue.append([node.left, sum, path[:]])  # 注意！！！不管之后path怎么变,这里的path都不变
            if node.right != None:
                queue.append([node.right, sum, path[:]])
                
        return path_all



if __name__ == '__main__':
    #root = constructTree([1,2,3,4,None,5])
    root = constructTree.constructTree([5,4,8,11,None,13,4,7,2,None,None,5,1])
    sum = 22

    result = Solution()
    print(result.pathSum2(root, sum))