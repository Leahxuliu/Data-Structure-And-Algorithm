'''
863

一个二叉树，给出一个target节点，然后给出一个distance，要求找到树中离target距离为distance的节点 
'''

'''
1. 建立pre
2. BFS
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.pre = None

from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if root == None:
            return []
        
        def build(root, parent):
            if root == None:
                return 
            
            root.pre = parent
            build(root.left, root)
            build(root.right, root)
            return 
        
        def find(root):
            visited = set()
            visited.add(root.val)

            queue = deque()
            queue.append(root)
            count = 0
            while queue:
                len_queue = len(queue)
                level = []
                for _ in range(len_queue):
                    curr = queue.popleft()
                    level.append(curr.val)

                    for each in [curr.left, curr.right, curr.pre]:
                        if each and each.val not in visited:
                            queue.append(each)
                            visited.add(each.val)
                if count == K:
                    return level

                count += 1
            return []

        build(root, None)

        return find(target)
