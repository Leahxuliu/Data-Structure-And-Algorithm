#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/17

'''
Method
A. iteration
Steps:
    1. creat dummy = pre = ListNode(0)
    2. traverse l1 and l2
    3. compare l1.val and l2.val, pre.next = smaller one, repeat this step until l1 == None or l2 == None
    4. after step3, if l1 != None(l2==None), pre.next = l1
        else, pre.next = l2
    5. return dummy.next

Time: O(n+m) n, m the number of nodes in l1, l2
Space: O(1)

B. Recursion
Time: O(n+m) n, m the number of nodes in l1, l2
Space: O(m+n)

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# iteration
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        dummy = pre = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = ListNode(l1.val)
                pre = pre.next
                l1 = l1.next
            else:
                pre.next = ListNode(l2.val)
                pre = pre.next
                l2 = l2.next
            
        if l1 != None:
            pre.next = l1
        if l2 != None:
            pre.next = l2
        
        return dummy.next

# Recursion
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2