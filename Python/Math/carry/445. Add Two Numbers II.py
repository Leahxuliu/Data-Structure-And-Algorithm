# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
思路一
reverse + add + reverse

思路二
用栈
栈里面保存每一个node的值
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # non-empty

        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        # dummy = ListNode()
        curr = None
        carry = 0

        while stack1 or stack2 or carry:
            if stack1:
                carry += stack1.pop()
            if stack2:
                carry += stack2.pop()
            
            # 易错 要倒过来加
            # curr.next = ListNode(carry % 10)
            newNode = ListNode(carry % 10)
            newNode.next = curr
            curr = newNode
            carry //= 10
        return curr