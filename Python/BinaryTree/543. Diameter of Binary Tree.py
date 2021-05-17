# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0

        def find(root):
            nonlocal res
            if root == None:
                return 0
            if root.left == None and root.right == None:
                return 1
            
            l = find(root.left)
            r = find(root.right)
            res = max(res, l + r + 1)
            return max(l, r) + 1
        
        res = 0
        find(root)
        
        return res - 1