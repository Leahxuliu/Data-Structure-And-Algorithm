# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/10  
# @Author  : XU Liu
# @FileName: 337.House Robber III.py 

'''
二叉树 按层遍历
每一层为一个dp[i]

step1:
先遍历tree，储存每一层的和(money：list)

step2：
在money里面找到最优解
状态转移方程：
dp[i] = max(dp[i-2] + money[i], dp[i])
base:
dp[0] = money[0]
dp[1] = max(money[0], money[1])

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
[2,1,3,null,4]
报错
'''
from collections import deque
class Solution:
    def rob(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        queue = deque()
        queue.append(root)
        money = []
        
        while queue:
            n = len(queue)
            temp = 0
            for i in range(n):
                node = queue.popleft()
                temp += node.val
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            money.append(temp)
        
        dp_j = money[0]
        dp_j2 = money[0]
        for j in range(1, len(money)):
            if j == 1:
                dp_j = max(money[0], money[1])
            else:
                temp2 = dp_j
                dp_j = max(dp_j, dp_j2 + money[j])
                dp_j2 = temp2
        return dp_j
                

'''
方法2
'''



'''
方法3
'''
                