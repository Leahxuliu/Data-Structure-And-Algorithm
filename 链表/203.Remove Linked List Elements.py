# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05  
# @Author  : XU Liu
# @FileName: 203.Remove Linked List Elements.py

'''
1. 题目要求：


2. 理解：
删除链表中所有指定的值

3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    1. 先建dummy （head可能就是要删的值）
    2. 快慢双指针
        f遇到val，s.next = f.next  f = f.next
        不是val， s = s.next       f = f.next


5. 空间时间复杂度

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return 
        
        dummy = ListNode(0)
        dummy.next = head
        
        s, f = dummy, head
        
        while f:
            if f.val == val:
                s.next = f.next
                f = f.next
            else:
                s = s.next
                f = f.next
        return dummy.next
                