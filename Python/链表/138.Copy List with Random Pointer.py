# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/06  
# @Author  : XU Liu
# @FileName: 138.Copy List with Random Pointer.py

'''
1. 题目要求：


2. 理解：


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    
5. 空间时间复杂度

'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return 
        
        dummy = Node(0)
        dummy.next = head

        # copy new node
        while head:
            next_head = head.next
            head.next = Node(head.val)
            head.next.next = next_head
            head = next_head
        
        # copy random
        head = dummy.next
        while head and head.next:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next
    
        # choose the new nodes
        head = dummy.next 
        dummy = Node(0)
        new_head = dummy
        while head and head.next:
            new_head.next = head.next
            head = head.next.next
            new_head = new_head.next
        return dummy.next