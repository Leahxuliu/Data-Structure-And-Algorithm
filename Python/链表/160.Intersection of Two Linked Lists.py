# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/03  
# @Author  : XU Liu
# @FileName: 160.Intersection of Two Linked Lists.py

'''
1. 题目要求：


2. 理解：


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    1. 两个出发点，A从headA开始走，B从headB开始走
    2. 走完自己的nodes之后，A再从headB开始走，B再从headA开始走
    3. A和B相遇点就是交点
    4. 若无交点，AB‘相遇点’是None，A == B == None
    
5. 空间时间复杂度

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        
        curA = headA
        curB = headB
        while curA != curB:
            print('A',curA.val,'B',curB.val)
            if curA:
                curA = curA.next
            else:
                curA = headB
            
            if curB:
                curB = curB.next
            else:
                curB = headA
        return curA