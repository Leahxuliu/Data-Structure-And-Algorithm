"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            n = len(queue)
            temp = []
            for _ in range(n):
                curr = queue.popleft()
                temp.append(curr.val)

                for each in curr.children:
                    queue.append(each)
            res.append(temp)
        
        return res