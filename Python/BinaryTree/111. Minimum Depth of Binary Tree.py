#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/04  
# @Author  : XU Liu
# @FileName: 111. Minimum Depth of Binary Tree.py

'''
1. 题目要求：
find its minimum depth.

2. 理解：
最小路径

3. 题目类型：
BT，性质，路径

4. 输出输入以及边界条件：
input: treenode
output: int
corner case: root == None --> 0
'''

'''
解题思路1
    1. DFS
    2. 遍历路径，找到最小值
    3. helper函数

复杂度
    Time: O(N)
    Space: average O(logN)
           worst O(N)
'''


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        def helper(root, depth):
            if root == None:
                all_depth.append(depth)  # 易错 别忘了 不然root==None的时候 会报错
                return

            if root.left == None and root.right == None:
                depth += 1
                all_depth.append(depth)
                
            if root.left != None:
                helper(root.left, depth+1)
            if root.right != None:
                helper(root.right, depth+1)
        
        depth = 0
        all_depth = []
        helper(root, depth)
        
        return min(all_depth)
                
'''
解题思路1 -- 优化
    1. DFS
    2. 直接找到最小值

复杂度
    Time: O(N)
    Space: average O(logN)
           worst O(N)
'''

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None or root.right == None:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
            # 易错 不是return 1，因为[1,2]的最小depth是2，不是1
        
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

'''
思路三
    1. BFS
    2. 某节点左右子树均为空，此节点即为叶子节点
    3. 层层遍历 --> 第一个叶子节点即为最小深度的叶子节点
    4. 在第一次到达叶子节点时，立马return depth
'''


from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        queue = deque()
        queue.append([root, 1])

        while queue:
            node, height = queue.popleft()
            if not node.left and not node.right:
                return height
            if node.left:
                queue.append([node.left, height + 1])
            if node.right:
                queue.append([node.right, height + 1])

'''
BFS
'''
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        '''if root.left == None and root.right == None:
            return 1
        if root.left == None or root.right == None:
            return 2'''  # [1,2,null,3,null,4,null,5] 正确是5，但是写了这个，就变成2了
        
        queue = deque()
        queue.append(root)
        depth = 0
        
        while queue:
            depth += 1
            len_q = len(queue)
            for i in range(len_q):
                node = queue.popleft()
                if node.left == None and node.right == None:
                    return depth
                #if node.left == None or node.right == None:
                #    return depth
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        return depth