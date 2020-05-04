# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05  
# @Author  : XU Liu
# @FileName: 19.Remove Nth Node From End of List.py

'''
1. 题目要求：
删除倒数第n个数，return 新链表

2. 理解：


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    快慢双指针
    
    1. f先走n步
    2. while f.next:
        s,f一起走
    3. f走到底的时候，s在倒数第n个节点前一个节点
    4. s.next = s.next.next 跳过要删掉的节点
    
5. 空间时间复杂度

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)  # 一定要建立空头，因为[1],1，链表只有一个node，要删掉的是head的时候，如果没有空头就会报错
        dummy.next = head
        
        s, f = dummy, dummy
        
        while n > 0:
            f = f.next
            n -= 1
        
        while f.next:
            s = s.next
            f = f.next
        
        s.next = s.next.next
        return dummy.next