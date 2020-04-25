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
        if not p and not q:  
            return True
        # one of p and q is None
        if not q or not p:  
            return False
        if p.val != q.val:  
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
    
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        
        queue = deque()
        queue.append([p, q])
        
        while queue:
            p, q = queue.popleft()
            if p == None and q == None:
                continue  # 关键点，易错！ DFS的时候，会返回到上一层，所以可以return True，但是BFS，这里如果return True了，就截止遍历了！[12,null,72] [12,null,-72]就会报错
            if p == None or q == None:
                return False
            if p.val != q.val:
                return False
            else:
                queue.append([p.left, q.left])
                queue.append([p.right, q.right])
        return True


if __name__ == '__main__':
    #root = constructTree([1,2,3,4,None,5])
    p = constructTree.constructTree([1,2,3])
    q = constructTree.constructTree([1,2,3])
    
    result = Solution()
    print(result.isSameTree2(p, q))
    

    