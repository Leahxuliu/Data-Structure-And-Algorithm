# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# dfs
# time O(n) space:O(logn)
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

        self.res = 0
        dfs(root)
        return self.res

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1