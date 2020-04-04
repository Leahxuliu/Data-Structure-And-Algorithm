# !/usr/bin/python
# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

Node1 = TreeNode(3)
Node2 = TreeNode(4)
Node3 = TreeNode(5)
Node4 = TreeNode(7)
Node5 = TreeNode(8)

Node1.left = Node2
Node1.right = Node3
Node2.left = Node4
Node2.right = Node5

root = Node1


# 二叉树遍历路径，不用回溯法
# DFS
class Solution:
    def binaryTreePaths(self, root):
        def dfs(root, path):
            if root == None:
                return
            
            if root.left == None and root.right == None:
                path.append(root.val)
                path_all.append(path)
            
            dfs(root.left, path+[root.val])  # 每一个node对应一个path，不管其它node上的path怎么变，该node上的path是不会发生改变的
            dfs(root.right, path+[root.val])
        
        
        path = []
        path_all = []
        dfs(root, path)
        return path_all

x = Solution()
print(x.binaryTreePaths(root))


# DFS
class Solution:
    def binaryTreePaths(self, root):
        def dfs(root, path):
            if root == None:
                return
            
            path += [root.val]  

            if root.left == None and root.right == None:
                path_all.append(path)

            dfs(root.left, path[:])  # copy list 关键点
            dfs(root.right, path[:])
        
        path = []
        path_all = []
        dfs(root, path)
        return path_all

x = Solution()
print(x.binaryTreePaths(root))


# 二叉树遍历路径，用回溯法
class Tree:
    def findPath(self, root):
        def dfs(root, path):
            if not root:
                return
            
            path.append(root.val)
            if not root.left and not root.right:
                res.append(path[:])

            '''for node in (root.left, root.right): 
                dfs(node, path)
            path.pop()'''
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()  # node.left node.right都是空的时候，pop，到底是回溯点

        res = []
        dfs(root, [])
        return res

Y = Tree()
print(Y.findPath(root))


# 二叉树遍历路径，用回溯法
class Solution:
    def binaryTreePaths(self, root):
        if root == None:  # 不能省，因为回溯是从root.left,root.right开始的
            return 
            
        def helper(root, path):
            if root == None:
                return 
            
            if root.left == None and root.right == None:
                all_path.append('->'.join(path[:]))
                return all_path
                
            for node in (root.left, root.right):  # 从选择列表里面做选择
                if node:
                    path.append(str(node.val))  # 执行
                    helper(node, path)  # 下一层的选择
                    path.pop()  # 撤销选择
                
        all_path = []
        helper(root, [str(root.val)])  # root是第一层（选择root作为第一层，有且只有一个选择）
        return all_path

'''Z = Solution()
print(Z.binaryTreePaths(root))'''