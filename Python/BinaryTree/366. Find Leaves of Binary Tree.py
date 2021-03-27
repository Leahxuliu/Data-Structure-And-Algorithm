# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        def remove_node(root):
            '''
            return flag weather this node should be removed or not
            return depth of the node
            '''
            if root == None:
                return True, 0
            if root.left == None and root.right == None:
                res[1].append(root.val)
                return True, 1
            
            l, depthl = remove_node(root.left)
            r, depthr = remove_node(root.right)
            if l:
                root.left = None
            if r:
                root.right = None
            
            depth = max(depthl, depthr) + 1
            if l and r:
                res[depth].append(root.val)

            return l and r, depth
            

        
        res = defaultdict(list)
        remove_node(root)
        res = [each for each in res.values()]
        return res

