# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/04  
# @Author  : XU Liu
# @FileName: 142.Linked List Cycle II.py

'''
1. 题目要求：
找环交点

2. 理解：


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    s: 1 step; f: 2 steps
    f赶上s则有环
    环的交点:
        在上面结果的基础上，i从s,f交点出发
        j从原点出发
        i与j相遇时，即环交点
        
5. 空间时间复杂度

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        s, f = head, head
        i, j = head, None
        
        while f and f.next:
            s = s.next
            f = f.next.next
            
            if s == f:
                j = f
                break  # 易错
                
        if j == None:
            return None
        
        while i != j:
            i = i.next
            j = j.next
        return i