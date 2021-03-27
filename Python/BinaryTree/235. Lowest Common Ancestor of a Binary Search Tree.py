# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
面试的时候，注意p,q不存在的情况
'''

# 不用二分索搜树的性质
# 自下而上
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None

        def traversal(root):
            if root == None:
                return False, False 
            
            ql, pl = traversal(root.left)
            qr, pr = traversal(root.right)
            flagq = False
            flagp = False

            if root == p or pl or pr:
                flagp = True
            if root == q or ql or qr:
                flagq = True
            
            if flagp and flagq:
                self.res = root
                return False, False

            return flagq, flagp
        
        self.res = None
        traversal(root)
        return self.res

# 用二分索搜树的性质
# 自上而下
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

# 用迭代
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return 
                
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        return None