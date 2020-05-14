#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/13

'''
API is difined

input: head: ListNode, the lenth of the linkedlist is from 0 to inf
       n: n is from 1 to the number of nodes
output: a new linkedlist’s head
corner: head == None, return None

Method - Two pointer
Steps:
    0. create a dummy
    1. i, j both start at dummy
    2. firstly j move n
        d->1->2->3->4->5
        i
        j  j  j
    3. i, j move together until j.next != None
        d->1->2->3->4->5
        i  i  i  i   
        j  j  j  j  j  j
    4. if i.next.next != None, i.next = i.next.next
        else, i.next = None
    5. return dummy.next
Time Complexity: O(N)
Space:O(1)
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return 
        
        dummy = ListNode(0)
        dummy.next = head
        
        i = dummy
        j = dummy
        
        for _ in range(n):
            j = j.next
            
        while j.next:
            i = i.next
            j = j.next
        
        if i.next.next != None:
            i.next = i.next.next
        else:
            i.next = None
        return dummy.next
            
            
            