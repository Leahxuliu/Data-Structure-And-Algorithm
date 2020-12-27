#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
BFS traversal the tree
如果中途开始不是complete，要计算从complete部分的node数
'''
from collections import deque
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        queue = deque()
        queue.append(root)
        res = 0
        flag = True

        while queue:
            curr = queue.popleft()
            res += 1

            if flag == False:
                continue
            
            if curr.left:
                queue.append(curr.left)
            else:
                flag == False
            
            if curr.right and flag:
                queue.append(curr.right)
        return res


'''
树是完全二叉树 
数有几个nodes
BFS
'''
from collections import deque
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        queue = deque()
        num = 0
        
        queue.append(root)
        while queue:
            node = queue.popleft()
            num += 1
            
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return num

'''
树是完全二叉树 
数有几个nodes
traversal the tree by using DFS + self.res
自上而下
'''
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0

        def dfs(root):
            if root == None:
                return 

            self.res += 1
            dfs(root.left)
            dfs(root.right)
            return 
        
        self.res = 0
        dfs(root)
        return self.res

'''
traversal the tree by using DFS 
自下往上
'''
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0

        return self.countNodes(root.left) + self.countNodes(root.right) + 1
