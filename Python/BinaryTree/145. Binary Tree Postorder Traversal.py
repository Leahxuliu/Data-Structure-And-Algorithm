# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        def DFS(root):
            if not root:
                return 
            
            DFS(root.left)
            DFS(root.right)
            res.append(root.val)
            return

        res = []
        DFS(root)
        return res

# 迭代
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        stack = [root]

        while stack:
            curr = stack.pop()
            res.append(curr.val)

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return res[::-1]
        