# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
分成前一半和后一半
把后一半转置
然后交叉合并
'''

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return None
        if head.next == None:
            return head
        
        dummy = ListNode()
        dummy.next = head

        # find medium
        s = dummy
        f = dummy

        while f and f.next:
            f = f.next.next
            s = s.next

        curr = s.next
        s.next = None  # 勿忘！
        right = None

        # reverse right
        while curr:
            next_head = curr.next
            curr.next = right
            right = curr
            curr = next_head

        left = dummy.next
        # merge
        while left and right:
            next_left = left.next
            next_right = right.next
            left.next = right
            right.next = next_left
            left = next_left
            right = next_right
        
        return dummy.next
            

