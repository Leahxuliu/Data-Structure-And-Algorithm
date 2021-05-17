'''
BST中的特定节点中序遍历后的下一个节点

面试题 04.06. Successor LCCI
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方法1 用stack进行中序遍历
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        stack = []
        flag = False
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            curr = stack.pop()
            if flag:
                return curr
                
            if curr == p:
                flag = True
            
            if curr.right:
                root = curr.right
        return None

# 用二分
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if root == None:
            return None 
        
        # if root == p:
        #     return self.inorderSuccessor(root.right, p)
        # elif root.val < p.val:

        res = None
        curr = root

        while curr:
            if curr.val <= p.val:
                curr = curr.right
            else:
                res = curr
                curr = curr.left
        return res
