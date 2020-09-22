#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/22

'''
Method
Steps:
    1. create dummy = pre = ListNode(0), pre.next = head
    2. compare pre.next and pre.next.next, and count the number of value
    3. return dummy.next
    
Time: O(N)
Space: O(N)
        
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return 
        
        dummy = pre = ListNode(0)
        pre.next = head
        flag = False
        
        while pre:
            while pre.next and pre.next.next and pre.next.val == pre.next.next.val:
                flag = True
                pre.next = pre.next.next
                    
            if flag == True:
                flag = False
                pre.next = pre.next.next
            else:
                pre = pre.next
            
        return dummy.next