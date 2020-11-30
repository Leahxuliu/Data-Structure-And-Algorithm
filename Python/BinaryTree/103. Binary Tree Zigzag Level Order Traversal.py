# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
BFS 按层次遍历
'''
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        queue = deque()
        queue.append(root)
        flag = 1
        res = []

        while queue:
            n = len(queue)
            temp = []
            for _ in range(n):
                node = queue.popleft()
                if flag == 1:
                    temp.append(node.val)
                else:
                    temp.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            flag = -flag
            res.append(temp)
        
        return res
        

'''
DFS
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []

        def traversal(root, level):
            if root == None:
                return 

            if len(self.res) < level + 1:
                self.res.append([])

            if level % 2 == 0:
                self.res[level].append(root.val)
            else:
                self.res[level].insert(0, root.val)
            
            traversal(root.left, level + 1)
            traversal(root.right, level + 1)
            return 
        
        self.res = []
        traversal(root, 0)
        return self.res
