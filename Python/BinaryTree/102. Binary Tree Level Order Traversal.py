# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
BFS 层次遍历
'''
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            n = len(queue)
            temp = []
            for _ in range(n):
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(temp)
        
        return res

'''
DFS 层次遍历
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        def dfs(root, depth):
            if not root:
                return
            
            if len(res) < depth + 1:
                res.append([root.val])
            else:
                res[depth].append(root.val)
            
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
            return
        
        res = []
        dfs(root, 0)
        return res