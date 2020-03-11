# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(root, path):
            if root == None:
                return
            
            if root.left == None and root.right == None:
                path.append(root.val)
                path_all.append(path)
            
            dfs(root.left, path+[root.val])
            dfs(root.right, path+[root.val])
        
        
        path = []
        path_all = []
        dfs(root, path)
        return path_all



# BFS
from collections import deque
class Solution:
    def binaryTreePaths(self, root: TreeNode):
        if root == None:
            return []
        
        queue = deque()
        path = []
        path_all = []
        queue.append([root, path])

        while queue:
            node, path = queue.popleft()
            path.append(node.val)

            if node.left == None and node.right == None:
                path_all.append(path)

            if node.left != None:
                queue.append([node.left, path[:]])
            if node.right != None:
                queue.append([node.right, path[:]])
        return path_all

