"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# DFS
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        def DFS(root):
            if not root:
                return
            
            res.append(root.val)
            for each in root.children:
                DFS(each)
            return 
        
        res = []
        DFS(root)
        return res


# 迭代
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        res = []
        stack = [root]

        while stack:
            curr = stack.pop()
            res.append(curr.val)

            for each in curr.children[::-1]:
                stack.append(each)

        return res