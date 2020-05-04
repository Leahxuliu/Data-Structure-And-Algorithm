# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05  
# @Author  : XU Liu
# @FileName: 83.Remove Duplicates from Sorted List.py

'''
1. 题目要求：
a sorted linked list, 删掉重复的，只留下一个
[1,1,2,3,3] --> [1,2,3]

2. 理解：


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    快慢双指针
    
5. 空间时间复杂度

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
快慢双指针
'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return 
        s, f = head, head
        
        while f:
            if f.val == s.val:
                f = f.next
            else:
                s.next = f
                s = s.next
                f = f.next
        s.next = f  #一定要写，最后几个数重复的时候，s.next是None 比如[1,1,2,3,3]，如果没有这一行的话，最后答案是[1,2,3,3]
        return head



'''
方法2
'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        
        curr = head
        while head:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            head = head.next
        return curr