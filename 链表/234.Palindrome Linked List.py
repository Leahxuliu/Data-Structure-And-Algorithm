# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/06  
# @Author  : XU Liu
# @FileName: 234.Palindrome Linked List.py

'''
1. 题目要求：
给出一个链表，判断是不是回文

2. 理解：


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    1. reverse the linkedlist,and return new head 
    2. compare the linked list and the reversed list
        eg: 1->2->3->1   
            1->3->2->1
    3. if there are difference nodes, return False
    
5. 空间时间复杂度
T: O(2N) N: the length of list
S: O(N)
'''

'''
错误
因为在转置list的时候，原本的list发生了改变
要在转置之前要copy一个链表
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        
        # reverse the link list
        curr = head  # curr只是head的标签， curr发生改变，head也发生改变
        new_head = None
        while curr:
            next_head = curr.next
            curr.next = new_head
            new_head = curr
            curr = next_head
        
        while new_head:
            if new_head.val != head.val:
                return False
            else:
                new_head = new_head.next
                head = head.next
        
        return True




'''
Follow up:
Could you do it in O(n) time and O(1) space?


1. slow and fast pointer to find the mid node; slow: 1step; fast: 2 steps
2. reverse the front part （边找中点边转置, f走到底，s就是中点，s每走一步都置换，直到f走到底，注意奇偶）
3. scan reversed front part and later part to compare
    奇数(f != None)：newhead 与 s.next
    偶数(f == None)：newhead 与 s

'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        if head.next == None:
            return True
        
        s = f = head
        newH = None
        while f and f.next:  # 边找中点边置换前半部 如果是偶数，f走到末尾的None，s在中点(右中点)；如果是奇数，f在末尾非None处，s在中点
            f = f.next.next
            nextHead = s.next
            s.next = newH
            newH = s
            s = nextHead
        
        if f == None:  # 偶数：newhead 与 s
            later = s
            front = newH
        else:  # 奇数：newhead 与 s.next
            later = s.next
            front = newH
        
        while later:
            if later.val != front.val:
                return False
            later = later.next
            front = front.next
        return True
            
