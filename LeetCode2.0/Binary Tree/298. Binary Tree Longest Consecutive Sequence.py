# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
Method - BFS
use queue to store the consecutive sequence path
scan the tree nodes and renew the logest path

'''
from collections import deque
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        queue = deque()
        queue.append([root, []])
        res = 0

        while queue:
            node, path = queue.popleft()
            if path == []:
                path.append(node.val)
            elif node.val == path[-1] + 1:
                path.append(node.val)
            else:
                path = [node.val]  # 易错
            res = max(res, len(path))

            if node.left != None:
                queue.append([node.left, path[:]])

            if node.right != None:
                queue.append([node.right, path[:]])
        
        return res


# DFS
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        def find(root, pre, n):
            if root == None:
                return 
            
            if root.val == pre + 1:
                n += 1
                self.res = max(self.res, n)
            else:
                n = 1
            
            find(root.left, root.val, n)
            find(root.right, root.val, n)
            return 
            


        self.res = 1  #易错，[1],res = 1 或者写到corner case里
        find(root, -1, 0)
        return self.res