# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        inorder = []
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            inorder.append(node.val)

            if node.right:
                root = node.right
        return inorder[-k]