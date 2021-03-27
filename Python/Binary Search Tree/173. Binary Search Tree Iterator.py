# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []

    def next(self) -> int:
        if self.stack or self.root:
            
            while self.root:
                self.stack.append(self.root)
                self.root = self.root.left

            curr = self.stack.pop()
            if curr.right:
                self.root = curr.right
        return curr.val


    def hasNext(self) -> bool:
        if self.stack or self.root:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()