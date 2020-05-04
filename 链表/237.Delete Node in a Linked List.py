# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05  
# @Author  : XU Liu
# @FileName: 237.Delete Node in a Linked List.py

'''
1. 题目要求：
删掉指定的node (except the tail) 

2. 理解：
只输入了需要删除的节点 node，因此无法获取删除节点 node 的前一个节点 pre，
从而也就无法将前一个节点 pre 指向删除节点的下一个节点 next；既然无法通过修改指针完成

3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    
5. 空间时间复杂度

'''

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
