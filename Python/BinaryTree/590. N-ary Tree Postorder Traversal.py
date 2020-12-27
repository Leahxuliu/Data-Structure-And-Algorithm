"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# DFS
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        def DFS(root):
            if not root:
                return 

            for each in root.children:
                DFS(each)

            res.append(root.val)
            return  
        
        res = []
        DFS(root)
        return res

# 迭代
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        res = []
        stack = [root]

        while stack:
            curr = stack.pop()
            res.append(curr.val)
            for each in curr.children:
                stack.append(each)
            
        return res[::-1]