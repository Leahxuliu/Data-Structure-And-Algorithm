# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/04  
# @Author  : XU Liu
# @FileName: 141.Linked List Cycle.py

'''
1. 题目要求：
判断是否有环

2. 理解：


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    
5. 空间时间复杂度

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        
        s, f = head, head
        
        while f != None and f.next != None:
            s = s.next
            f = f.next.next
            
            # if s.val == f.val: 错误 因为None是没有val的
            if s == f:
                return True
        return False
            