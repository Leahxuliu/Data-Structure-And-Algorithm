#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/16

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
Method - convert array + binary search + DFS
Steps:
    1. convert linked list to list (arr)
    2. use binary search to find root
       root = arr[mid]
       root.left: arr[:mid]
       root.right:arr[mid+1:]

'''
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return 
        
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
        
        def DFS(arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = l + (r - l) // 2

                root = TreeNode(arr[mid])
                root.left = DFS(arr[:mid])
                root.right = DFS(arr[mid+1:])
                return root
        
        return DFS(arr)