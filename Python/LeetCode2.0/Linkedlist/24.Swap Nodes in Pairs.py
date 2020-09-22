'''
Method - 
Steps:
    1. set dummy and pre = ListNode(0)
    2. traverse listnodes from linked list
    3. 
       

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return 
        
        dummy = pre = ListNode(0)
        dummy.next = head

        while head and head.next:
            firstNode = head
            secondNode = head.next
            
            pre.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode
            
            pre = firstNode
            head = firstNode.next
        return dummy.next
