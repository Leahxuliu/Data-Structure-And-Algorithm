'''
236
BT
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        if p == None or q == None:
            return None
        
        def find(root):
            if root == None:
                return False, False

            lp, lq = find(root.left)
            rp, rq = find(root.right)
            flagp, flagq = False, False

            if lp or rp or root == p:
                flagp = True
            if lq or rq or root == q:
                flagq = True
            
            if flagp and flagq:
                self.ans = root
                return False,False
            return flagp, flagq
        
        self.ans = None
        find(root)
        return self.ans

# 非递归

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        
        queue = deque()
        queue.append([root, []])

        p_path = []
        q_path = []
        while queue:
            node, path = queue.popleft()
            path.append(node)
            if node == p:
                p_path = path[:]
            if node == q:
                q_path = path[:]

            if node.left:
                queue.append([node.left, path[:]])
            if node.right:
                queue.append([node.right, path[:]])
        
        i = 0
        j = 0

        while i < len(p_path) and j < len(q_path):
            if p_path[i] == q_path[j]:
                i += 1
                j += 1
            else:
                break
        
        return p_path[i - 1] if i - 1 > 0 else p_path[0]