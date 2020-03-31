#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2/27/2020  
# @Author  : XU Liu
# @FileName: constructTree.py

import constructTree
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    '''
    题目理解：
    judge whether two binary tree are same

    思路：
    DFS
    using recursion to check the root, left-child and right-child

    time complexity order: O(N) 
    space complexity order: O(log(N)) average; O(N) worse
    '''
    def isSameTree(self, p, q):
        # p and q are both None
        if not p and not q:  # p 和 q都已经结束了，没有节点了；或者，这两个树，原本就是空的
            return True
        # one of p and q is None
        if not q or not p:  # p或q，其中一个已经遍历完了，没有节点了；或者，其中一个树，原本就是空的
            return False
        if p.val != q.val:  # 有节点，但是值不同
            return False
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)


    '''
    思路：
    BFS

    time complexity order: O(N) 
    space complexity order: O(N) average; O(1) best
    '''

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
    
        queue = deque([(p, q)])
        
        while queue:
            p_node, q_node = queue.popleft()

            if not p_node and not q_node:
                return True
            
            elif not p_node or not q_node:
                return False
            
            elif p_node.val != q_node.val:
                return False

            else:
                queue.append((p_node.left, q_node.left))
                queue.append((p_node.right, q_node.right))
        return True

if __name__ == '__main__':
    #root = constructTree([1,2,3,4,None,5])
    p = constructTree.constructTree([1,2,3])
    q = constructTree.constructTree([1,2,3])
    
    result = Solution()
    print(result.isSameTree2(p, q))
    

    