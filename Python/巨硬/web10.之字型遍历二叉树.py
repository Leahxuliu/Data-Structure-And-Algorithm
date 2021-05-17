'''
103. Binary Tree Zigzag Level Order Traversal
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        def traversal(root, depth):
            if root == None:
                return 
            
            depth += 1
            if len(res) < depth:
                res.append([])
            if depth % 2 == 1:
                res[depth - 1].append(root.val)
            else:
                res[depth - 1].insert(0, root.val)
            
            traversal(root.left, depth)
            traversal(root.right, depth)
            return 
        
        res = []
        traversal(root, 0)
        return res


from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        
        res = []
        queue = deque()
        queue.append(root)
        count = 0

        while queue:
            len_queue = len(queue)
            level = deque()
            count += 1

            for _ in range(len_queue):
                curr = queue.popleft()
                if count % 2 == 1:
                    level.append(curr.val)
                else:
                    level.appendleft(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(list(level))
        return res