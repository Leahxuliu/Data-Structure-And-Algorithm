# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        # dummy = ListNode()
        curr = None

        while head:
            next_head = head.next
            head.next = curr
            curr = head
            head = next_head
        return curr