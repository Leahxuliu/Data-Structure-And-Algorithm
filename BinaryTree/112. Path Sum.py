#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/04  
# @Author  : XU Liu
# @FileName: 112. Path Sum.py

'''
1. 题目要求：


2. 理解：
找到是否有相应路径和的path

3. 题目类型：
BT，路径和

4. 输出输入以及边界条件：
input: treenode
output: bool
corner case: root == None

5. 解题思路
    1. 用DFS，一边遍历，一边找路径和

'''

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        sum -= root.val

        if root.left == None and root.right == None:
            return sum == 0
            
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

'''
错误
原因还没想明白
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        sum -= root.val
        if root.left != None:
            self.hasPathSum(root.left, sum)
        if root.right != None:
            self.hasPathSum(root.right, sum)
        
        if root.left == None and root.right == None:
            if sum == 0:
                return True
            else:
                return False
'''

'''
思路2
DFS
考虑结束条件是什么：
结束条件 1：如果当前节点是空的，则返回 false。
结束条件 2：如果是叶子，那么如果剩余的 sum 等于当前叶子的值，则找到满足条件的路径，返回 true。
'''

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False

        # 当前节点是叶子，检查 root.val 值是否为 sum
        if root.left == None and root.right == None and root.val == sum:
            return True

        # 当前节点不是叶子，对它的所有孩子节点，递归调用 hasPathSum() 函数
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)

'''
找到所有path
'''
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        
        
        def helper(root, path):
            if root.left == None and root.right == None:
                return all_path.append(path + root.val)
        
            if root.left != None:
                helper(root.left, path + root.val)
            if root.right != None:
                helper(root.right, path + root.val)
            
        all_path = []
        helper(root, 0)
        if sum in all_path:
            return True
        else:
            return False

'''
思路2
BFS
用栈将递归转成迭代的形式
栈中保存当前节点前的剩余值
虽然是按层遍历，但是sum减掉的都是上一层的parent
'''
from collections import deque
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        
        queue = deque()
        queue.append([root, sum])
        
        while queue:
            node, sum = queue.popleft()
            sum -= node.val
            if node.left == None and node.right == None:
                if sum == 0:
                    return True
            
            if node.left != None:
                queue.append([node.left, sum])
            if node.right != None:
                queue.append([node.right, sum])
                
        return False