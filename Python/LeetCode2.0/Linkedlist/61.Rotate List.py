#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/18

'''
Method
Steps:

    1. calculate the number of nodes (N)
    2. new_k = N - k % N
    3. curr.next = head, forming a circle
    4. cut the link of (N - k % N - 1)th node and (N - k % N)th node
    5. return new_head

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return
        
        curr = head
        n = 1
        while curr.next:
            n += 1
            curr = curr.next
        
        curr.next = head
        end = head
        new_k = n - k % n
        
        while new_k >1:
            end = end.next
            new_k -= 1
        new_head = end.next
        end.next = None
        return new_head
        
  