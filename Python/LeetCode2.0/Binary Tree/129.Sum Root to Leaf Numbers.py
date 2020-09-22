'''
Method
A. DFS
Steps:
    1. use DFS to scan the nodes and store each path in list
    2. when node.left == None and node.right == None, all_res += int(''.join(path))
       else, continue scan nodes and path.append(str(node.val))

B. BFS

C. Backtracking

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        def dfs(root, path):
            if root == None:
                return 
            
            path.append(str(root.val))
            if root.left == None and root.right == None:
                self.all_res += int(''.join(path))
                
            if root.left != None:
                dfs(root.left, path[:])
            if root.right != None:
                dfs(root.right, path[:])
        
        self.all_res = 0
        dfs(root, [])
        return self.all_res

# BFS
from collections import deque
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        queue = deque()
        all_res = 0
        queue.append([root, []])
        while queue:
            node, path = queue.popleft()
            
            path.append(str(node.val))
            if node.left == None and node.right == None:
                all_res += int(''.join(path))
            
            if node.left != None:
                queue.append([node.left, path[:]])
            if node.right != None:
                queue.append([node.right, path[:]])
        return all_res

# backtracking
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        
        def backtracking(root, path):
            if root == None:
                return 
            
            path.append(str(root.val))
            
            if root.left == None and root.right == None:
                self.all_res += int(''.join(path))
            
            if root.left != None:
                backtracking(root.left, path)
            if root.right != None:
                backtracking(root.right, path)
            
            path.pop()
            
        
        
        self.all_res = 0
        backtracking(root, [])
        return self.all_res

# backtracking
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        
        def backtracking(root, path):
            if root.left == None and root.right == None:
                self.all_res += int(''.join(path))
            
            if root.left != None:
                backtracking(root.left, path+[str(root.left.val)])
            if root.right != None:
                backtracking(root.right, path+[str(root.right.val)])
            
            path.pop()
            
        
        
        self.all_res = 0
        backtracking(root, [str(root.val)])
        return self.all_res