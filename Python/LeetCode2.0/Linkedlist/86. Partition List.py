'''
two pointers
    1. make two dummy, one is for stocking < x, another is for stocking >=x
    2. set i, j to start at dummy1, dummy2
    3. scan ListNode
    4. if node.val < X, i.next = ListNode(node.val)
    5. if node.val >= x, j.next = ListNode(node.val)
    6. merge: dummy1 tail + dummy2 head
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None:
            return 
        
        dummy1 = i = ListNode(0)
        dummy2 = j = ListNode(0)
        
        curr = head
        
        while curr:
            if curr.val < x:
                i.next = ListNode(curr.val)
                i = i.next
                curr = curr.next
            else:
                j.next = ListNode(curr.val)
                j = j.next
                curr = curr.next
        i.next = dummy2.next
        return dummy1.next