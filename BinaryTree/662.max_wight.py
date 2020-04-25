#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2/27/2020  
# @Author  : XU Liu
# @FileName: max_wight.py

import constructTree
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
错误
这个写法 不包含None
'''
'''
           1
         /   \
        3     2
       / \     \  
      5   3     9 
The maximum width existing in the third level with the length 4 (5,3,null,9).
'''

class Solution:
    def maxWight(self, root):
        max_len = 0
        if root == None:
            return max_len
        
        queue = deque()
        queue.append(root)

        while queue:
            q_len = len(queue)
            max_len = max(max_len, q_len)
            for i in range(q_len):
                node = queue.popleft()

                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)

        return max_len


'''
订
'''
'''
time complex: O(N)
space complex: average O(N) best O(1)
'''
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        queue = deque()
        queue.append([root, 0])
        max_wight = 0
        
        while queue:
            l = queue[0][1]
            r = queue[-1][1]
            max_wight = max(max_wight, (r - l + 1))
            len_q = len(queue)
            
            for i in range(len_q):
                node, index = queue.popleft()
                if node.left != None:
                    queue.append([node.left, index*2+1])
                if node.right != None:
                    queue.append([node.right, index*2+2])
        return max_wight


if __name__ == "__main__":
    root = constructTree.constructTree([1,2,3,4,5,6,7,None,None,12])

    result = Solution()
    print(result.maxWight(root))

    