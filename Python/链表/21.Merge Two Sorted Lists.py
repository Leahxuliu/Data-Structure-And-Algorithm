# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05  
# @Author  : XU Liu
# @FileName: 21.Merge Two Sorted Lists.py

'''
1. 题目要求：
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

2. 理解：


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    

5. 空间时间复杂度

'''

'''
用递归

'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


'''
用指针(迭代)
创建一个新的dummy
curr是指针

Space O(N)
Time O(N)
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        dummy = curr = ListNode(0)
        while l1 and l2:
            
            if l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
                curr.next = node
                curr = curr.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
                curr.next = node
                curr = curr.next
        
        if l1 != None:
            curr.next = l1
        
        if l2 != None:
            curr.next = l2
        
        return dummy.next