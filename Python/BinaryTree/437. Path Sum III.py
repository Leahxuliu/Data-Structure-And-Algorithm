# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
错误
因为node有负数
'''

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        def dfs(root, path, sumPath):
            print(root, path, sumPath)
            
            if sumPath == sum:
                self.res += 1
            if sumPath > sum:
                sumPath -= path[0]
                path.pop(0)
                if sumPath == sum and len(path) > 0:
                    self.res += 1
            
            if root.left:
                dfs(root.left, path + [root.left.val], sumPath + root.left.val)
            if root.right:
                dfs(root.right, path + [root.right.val], sumPath + root.right.val)
            return 
        
        self.res = 0
        dfs(root, [root.val], root.val)
        return self.res


'''
DFS + prefix

'''

from collections import defaultdict
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        def dfs(root, sumPath):            
            if root == None:
                return 0

            res = 0
            sumPath += root.val
            res = prefix[sumPath - sum]
            
            prefix[sumPath] += 1
            res += dfs(root.left, sumPath)
            res += dfs(root.right, sumPath)
            prefix[sumPath] -= 1
            return res
        
        prefix = defaultdict(int)
        prefix[0] = 1
        return dfs(root, 0)
