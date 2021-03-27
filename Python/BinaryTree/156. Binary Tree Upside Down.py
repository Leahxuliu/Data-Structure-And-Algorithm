# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        
        def DFS(root):
            if root == None:
                return None
            if root.left == None and root.right == None:
                return root

            
            new_root = DFS(root.left)

            root.left.left = root.right
            root.right = None
            root.left.right = root
            root.left = None
            return new_root

        
        return DFS(root)