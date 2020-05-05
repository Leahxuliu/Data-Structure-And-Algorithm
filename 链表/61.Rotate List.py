# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05  
# @Author  : XU Liu
# @FileName: 61.Rotate List.py

'''
1. 题目要求：
最后一个node移动到第一个，重复k次

2. 理解：


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    
5. 空间时间复杂度

'''

'''
two pointers (slow and fast pointer) 仅限于k的取值比链表长度小
    
    1. make dummy, dummy = ListNode(0)
    2. set two pointers start at dummy
    3. fast pointer move k steps
    4. slow and fast move one step together until fast.next == None
    5. fast.next = head
    6. head = s.next  # 易错 记录头
    7. slow.next = None
    
    此方法错误，因为k的取值范围是没有规定的，所以可以是很大，轮好几回
    需要知道链表的长度
    可是上面这个方法没法知道链表的长度
'''
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return 
        
        dummy = ListNode(0)
        dummy.next = head
        
        s, f = dummy, dummy
        
        while k > 0:
            f = f.next
            k -= 1
        
        while f.next != None:
            s = s.next
            f = f.next
        
        f.next = dummy.next
        head = s.next
        s.next = None
        return head


'''
1. 找到旧的尾部并将其与链表头相连（cur.next = head）
2. 整个链表闭合成环，同时计算出链表的长度 n
3. 找到新的尾部，第 n - k % n个节点 ，新的链表头是第 n - k % n + 1个节点 (1-based)
4. 断开环 end.next = None，并返回新的链表头 new_head。
'''

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return 
        
        curr = head
        n = 1  # 易错 下面的while次数是步数，步数+1是个数
        
        while curr.next:
            curr = curr.next
            n += 1
            
        curr.next = head
        
        end = head
        new_k = n - k % n
        while new_k > 1:
            end = end.next
            new_k -= 1
        new_head = end.next
        end.next = None
        return new_head
            