# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
BFS
'''
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i == n - 1:
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''

先遍历left的话，就是最后一个遇到的就是
'''
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        def traversal(root, level):
            if root == None:
                return 
            
            if len(self.res) < level + 1:
                self.res.append([])
            
            self.res[level] = root.val
            traversal(root.left, level + 1)
            traversal(root.right, level + 1)
            return 

        self.res = []
        traversal(root, 0)
        return self.res



'''
递归
递归参数里面带depth
先访问right节点，这样所遇到的新一层的第一个node就是想要的节点
'''
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        def find(root, depth):
            if root == None:
                return 
            
            depth += 1
            if len(nodes) >= depth:  # >= !!!不是==
                pass
            else:
                nodes.append([root.val])
                res.append(root.val)
            
            find(root.right, depth)
            find(root.left, depth)
            return 
        
        nodes = []
        res = []
        find(root, 0)
        return res
