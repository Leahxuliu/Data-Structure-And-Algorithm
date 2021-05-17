# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路一，放入stack
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        stack1 = []
        stack2 = []

        def add2stack(l, stack):
            while l:
                next_l = l.next
                l.next = None
                stack.append(l)
                l = next_l
            return 
        
        add2stack(l1, stack1)
        add2stack(l2, stack2)

        '''
        放入指针也可
        s1, s2 = [], []
        
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        '''

        carry = 0
        curr = None
        while stack1 or stack2 or carry:  # 勿忘 or carry,比如5+5 = 1 0
            if stack1:
                node = stack1.pop()
                carry += node.val 
            if stack2:
                node = stack2.pop()
                carry += node.val
            
            new = ListNode(carry % 10)
            new.next = curr
            curr = new
            carry = carry // 10

        return curr


# 思路2  reverse + add + reverse