'''
21
合并两个sorted链表
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        new_head = ListNode()
        curr = new_head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        while l1:
            curr.next = l1
            l1 = None  # 勿忘！
        while l2:
            curr.next = l2
            l2 = None  # 勿忘！
        return new_head.next
        