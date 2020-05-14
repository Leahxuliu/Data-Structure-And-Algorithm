'''
Method:
Linkedlist --> int --> Linkedlist

Steps:
    1. convert l1 and l2 to integers
        a. traverse listnodes from l1 and l2
        b. int =+ listnode.val * 10^n
    2. calculate temp = int1 + int2
    3. convert temp to ListNode

Time Complexity: O(N), N = max(m,n)
Space: O(N)

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        int1 = 0
        n = 1
        while l1:
            int1 += l1.val * n
            n *= 10
            l1 = l1.next
        
        int2 = 0
        m = 1
        while l2:
            int2 += l2.val * m
            m *= 10
            l2 = l2.next
        
        # 构建新的linkedlist
        temp = str(int1 + int2)
        dummy = p = ListNode(0)
        for i in range(len(temp) - 1, -1, -1):
            p.next = ListNode(int(temp[i]))
            p = p. next
        return dummy.next
            
        