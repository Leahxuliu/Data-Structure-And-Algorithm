# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]

        # left boundary
        left_nodes = []
        curr = root.left
        while curr:
            if curr.left == None and curr.right == None:
                break
            left_nodes.append(curr.val)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
        
        # right boundary
        right_nodes = []
        curr = root.right
        while curr:
            if curr.left == None and curr.right == None:
                break
            right_nodes.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left

        # leaf
        # 不能用BFS，因为leaf不一定是最下面那一层，比如[1,2,7,3,5,null,6,4]
        
        leaf = []
        def traversal(root):
            if root == None:
                return 
            if root.left == None and root.right == None:
                leaf.append(root.val)
                return 
            
            traversal(root.left)
            traversal(root.right)
            return 
            
        traversal(root)
        return [root.val] + left_nodes + leaf + right_nodes[::-1]
        