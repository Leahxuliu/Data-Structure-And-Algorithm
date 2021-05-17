"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
'''

traversal nodes in inorder with stack

node.left is pre
node.right is successor 
'''


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # corner case
        if root == None:
            return None
        
        head = Node(0)
        curr = head
        pre = None

        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            curr.right = node
            curr = node
            if pre:
                curr.left = pre
            pre = curr

            if node.right:
                root = node.right
                    
        head.right.left = pre
        pre.right = head.right

        return head.right

'''
简化
'''

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        
        head = Node(0)
        # curr = head
        pre = head

        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            node = stack.pop()
            if node.right:
                root = node.right

            pre.right = node 
            node.left = pre 
            pre = node 



        head.right.left = pre 
        pre.right = head.right
        return head.right

