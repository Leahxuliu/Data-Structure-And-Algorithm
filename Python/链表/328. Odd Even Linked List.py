# 把偶数上的node拆下来，放到最后 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return

        dummy = ListNode(0)
        dummy.next = head

        j = head
        n = 0
        while j.next != None:
            n += 1
            j = j.next
        n += 1

        if n == 2:
            return dummy.next

        i = head 
        for _ in range(n // 2):
            curr = i.next
            i.next = i.next.next
            curr.next = None
            j.next = curr
            j = curr
            i = i.next

        return dummy.next
            

# 用evenhead和oddhead
# 官方解答
