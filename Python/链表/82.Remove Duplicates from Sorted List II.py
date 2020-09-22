# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/04  
# @Author  : XU Liu
# @FileName: 82.Remove Duplicates from Sorted List II.py

'''
1. 题目要求：
a sorted linked list, 删掉重复的，全删
[1,1,2,3,3] --> [2]

2. 理解：


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    快慢双指针
    
5. 空间时间复杂度

'''

'''
方法1
先用dict储存node值和出现过的次数
然后遍历dict，用只出现1次的值，构建链表

空间复杂度：O(N) dict的空间复杂度，所有的value和
时间复杂度：O(2N)

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
        
        info = {}
        while head:
            if head.val in info:
                info[head.val] += 1
            else:
                info[head.val] = 1
            
            head = head.next  
        
        # dummy = ListNode(0)  # 不能分开来写
        # pre = ListNode(0)
        dummy = pre = ListNode(0)  # ListNode(0)赋给pre，pre赋给dummy，都在同一个节点上
        
        for k, v in info.items():
            if v == 1:
                node = ListNode(k)
                pre.next = node
                pre = pre.next
        return dummy.next


'''
方法2
inplace
from discuss
'''
#p1 -> always last node before repeate sequence
#p2 -> first node within repeat sequence
#t -> first node after repeat sequence
#so, repeat sequence is always contained in between p1 and t
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:    
        if not head or not head.next:
            return head
        dummy = ListNode(None)
        dummy.next = head
        p1 = dummy
        p2 = head
        
        while p2 and p2.next:
            if p2.val == p2.next.val:
                #find repeat sequence boundaries and delete it in one pass
                t = p2.next
                val = p2.val
                while t and val == t.val:
                    del p2
                    p2 = t
                    t = t.next 
                del p2
                p1.next = t
                p2 = t
            else:
                p1 = p2
                p2 = p2.next
        return dummy.next