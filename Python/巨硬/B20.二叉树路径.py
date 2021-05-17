'''
LC 113

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root == None:
            return []
        
        def find(root, count, path):
            if root == None:
                return 
            # 易错；一定不能再root==None的地方加入path，这样的话，会加入两次一样的path
            if root.left == None and root.right == None:
                if count == targetSum - root.val:
                    res.append(path[:] + [root.val])
                return 
            
            
            find(root.left, count + root.val, path + [root.val])
            find(root.right, count + root.val, path + [root.val])

            return 
        
        res = []
        find(root, 0, [])
        return res