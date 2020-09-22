# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/01  
# @Author  : XU Liu
# @FileName: 501.Find Mode in Binary Search Tree.py

'''
1. 题目类型：
    BST

2. 题目要求与理解：
    找到出现次数最多的数(可能不止一个)
    众数（mode）指一组数据中出现次数最多的数据值
    Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
    Assume a BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.



    

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
方法一
遍历+字典
因为用到字典，会增加额外的空间
Time complexity: O(N + N) = O(N) N is number of nodes
Space: O(N) used in dict
'''

from collections import defaultdict
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root == None:
            return None
        
        stack = []
        info = defaultdict(lambda: 0)
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
                
            cur = stack.pop()
            info[cur.val] += 1
            
            if cur.right != None:
                root = cur.right
        modes = []
        max_val = sorted(info.values())[-1]
        for k, v in info.items():
            if v == max_val:
                modes.append(k)
            
        return modes

'''
方法二
二叉搜索树的中序遍历是一个升序序列，逐个比对当前结点值 cur_node.val 与前驱结点值 pre_node.val。更新当前节点值出现次数 curTimes 及最大出现次数 maxTimes，更新规则：
若 curTimes=maxTimes，将 cur_node.val 添加到结果向量 res 中
若 curTimes>maxTimes，清空 res，将 cur_node.val 添加到 res，并更新 maxTimes 为 curTimes
Time: O(N) 
Space: O(1)
'''

'''
易错点
root只有一个的时候，mode就是root
如果所有的值都只出现过一次，那么只出现过一次的值就是mode
'''

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root == None:
            return None
        
        stack = []
        modes = []
        times = 1
        max_time = 0
        pre = float('-inf')
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            cur = stack.pop()
            if cur.val == pre:
                times += 1  # 这个值跟上一个值是一样的，累计
            else:
                pre = cur.val
                times = 1  # 易错 容易忘记
                
            if times == max_time:
                modes.append(cur.val)
            elif times > max_time:
                max_time = times
                modes = []
                modes.append(cur.val)
            
                
            if cur.right != None:
                root = cur.right
        return modes