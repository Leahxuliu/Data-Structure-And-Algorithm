# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        r = self.invertTree(root.right)
        l = self.invertTree(root.left)
        
        root.left = r
        root.right = l
        return root


# wrong
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        
        return root

