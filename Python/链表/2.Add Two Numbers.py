# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05  
# @Author  : XU Liu
# @FileName: 2.Add Two Numbers.py

'''
1. 题目要求：


2. 理解：


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    1. 链表变成数
    2. 两数相加
    3. 建立新的链表
    
5. 空间时间复杂度
O(m+n)
O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a1 = 0
        t1 = 1
        
        a2 = 0
        t2 = 1
        
        while l1:
            a1 += l1.val * t1
            l1 = l1.next
            t1 *= 10
        while l2:
            a2 += l2.val * t2
            l2 = l2.next
            t2 *= 10
        
        s = str(a1 + a2)
        dummy = pre = ListNode(0)
        for i in range(len(s)-1,-1,-1):
            node = ListNode(int(s[i]))
            pre.next = node
            pre = pre.next
        return dummy.next
            