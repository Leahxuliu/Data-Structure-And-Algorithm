# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0
        
        def countdistance(root):
            # return the distance of leaf to root
            if root == None:
                return []
            if root.left == None and root.right == None:
                return [1]
            
            l = countdistance(root.left)
            r = countdistance(root.right)

            for i in l:
                for j in r:
                    if i + j <= distance:
                        self.res += 1

            return [each + 1 for each in l + r]
        

        self.res = 0
        countdistance(root)
        return self.res
