# -*- coding: utf-8 -*-
# @Time    : 3/04/2020  
# @Author  : XU Liu

import constructTree
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def minDepth(self, root):
        if root == None:
            return 0
        
        queue = deque()
        queue.append([root,0])
        
        while queue:
            node, depth = queue.popleft()
            depth += 1

            if node.left == None and node.right == None:
                return depth

            if node.left != None:
                queue.append([node.left, depth])
            if node.right != None:
                queue.append([node.right, depth])

if __name__ == '__main__':
    root = constructTree.constructTree([1,None,2])
    result = Solution()
    print(result.minDepth(root))
    