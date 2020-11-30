# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_ancestor(root):
            if root == None:
                return False, False
            
            lp, lq = find_ancestor(root.left)
            rp, rq = find_ancestor(root.right)

            anp, anq = False, False
            if lp or rp or root.val == p.val:
                anp = True
            if lq or rq or root.val == q.val:
                anq = True

            if anq == True and anp == True:
                self.ans = root
                return False, False
            return anp, anq
        
        self.ans = TreeNode()
        find_ancestor(root)
        return self.ans