'''
25 
reverse linkedlist in k group

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 转成list 用stack
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return 
        
        stack = []
        dummy = ListNode()
        curr = dummy

        while head:
            stack.append(head.val)
            head = head.next

            if len(stack) == k:
                while stack:
                    curr.next = ListNode(stack.pop())
                    curr = curr.next

        stack = stack[::-1]  # 勿忘！
        
        while stack:
            curr.next = ListNode(stack.pop())
            curr = curr.next

        return dummy.next