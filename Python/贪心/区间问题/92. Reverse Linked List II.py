# 微软高频

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        # not reverse
        curr = dummy
        times = m - 1
        while times:
            curr = curr.next
            times -= 1

        # reverse
        change = curr.next
        tail = curr.next
        curr.next = None
        times = n - m + 1
        new = None 
        while times:
            next_head = change.next
            change.next = new
            new = change
            change = next_head
            times -= 1

        curr.next = new

        # not reverse
        tail.next = change

        return dummy.next

