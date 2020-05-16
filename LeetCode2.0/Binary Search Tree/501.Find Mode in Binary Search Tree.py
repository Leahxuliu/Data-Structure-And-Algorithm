#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/16


# DFS + dict
from collections import defaultdict
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        def dfs(root):
            if root == None:
                return 
            
            info[root.val] += 1
            dfs(root.left)
            dfs(root.right)
        
        info = defaultdict(int)
        dfs(root)
        
        max_val = sorted(info.values())[-1]
        res = []
        for k, v in info.items():
            if v == max_val:
                res.append(k)
            
        return res

# BFS
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        stack = []
        node = root 
        res = []
        max_times = 0
        times = 0
        pre = root.val
        
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            curr = stack.pop()
            if curr.val == pre:
                times += 1
            else:
                pre = curr.val
                times = 1  # 易错点， 不是0
                
            if times > max_times:  # 易错，注意不能放在if curr.val == pre:里面一层
                res = [curr.val]
                max_times = times
            elif times == max_times:
                res.append(curr.val)
                
            if curr.right != None:
                node = curr.right
        return res
