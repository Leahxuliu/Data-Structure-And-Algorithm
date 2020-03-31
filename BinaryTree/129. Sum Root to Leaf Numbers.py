#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/04  
# @Author  : XU Liu
# @FileName: 129. Sum Root to Leaf Numbers.py

'''
1. 题目要求：


2. 理解：
sum root to leaf
每一条路径构成一个数，把所有路径构成的数都相加

3. 题目类型：
BT，路径和

4. 输出输入以及边界条件：
input: treenood
output: int
corner case: root == None --> return 0

5. 解题思路
    BFS
    1. 寻找所有路径
    2. deque([root, path])
    3. path是list，构成数，相加
        path = [str(i) for i in path]
        res += int(''.join(path))

    或者直接构成数
    tmp *= 10
    tmp += root.val
'''

from collections import deque
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        res = 0
        queue = deque()
        path = []
        queue.append([root, path])

        while queue:
            node, path = queue.popleft()
            path.append(node.val)

            if node.left == None and node.right == None:
                path = [str(i) for i in path]
                res += int(''.join(path))

            if node.left != None:
                queue.append([node.left, path[:]])
            if node.right != None:
                queue.append([node.right, path[:]])
        return res


'''
解题思路
    DFS
    1. 用一个helper函数，寻找所有路径并记录
    2. 再对记录下来的路径list做处理
    
'''

class Solution:
    def sumNumbers(self, root: TreeNode) -> int: 
        def dfs(root, path):
            if root == None:
                return
            
            if root.left == None and root.right == None:
                path.append(root.val)
                path_all.append(path)
            
            dfs(root.left, path+[root.val])
            dfs(root.right, path+[root.val])
        
        
        path = []
        path_all = []
        res = 0
        dfs(root, path)
        
        for each in path_all:
            each = [str(i) for i in each]
            res += int(''.join(each))
        return res

'''
或者直接构成数
    tmp *= 10
    tmp += root.val
'''
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(root, nums):
            if root == None:
                return 0

            # 更新路径和
            nums *= 10
            nums += root.val

            # 如果已经是叶子节点，保存路径和到列表中
            if root.left == None and root.right == None:
                res.append(nums)

            if root.left != None:
                helper(root.left,nums)

            if root.right != None:
                helper(root.right,nums)

        
        res = []
        helper(root,0)

        return sum(res)