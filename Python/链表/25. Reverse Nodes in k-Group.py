# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
放入stack
'''
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or head == None:
            return head
        
        stack = []
        count = 0

        # 都放入stack，断开链接
        curr = head
        while curr:
            count += 1
            next_curr = curr.next
            curr.next = None
            stack.append(curr)
            curr = next_curr
        
        # 处理不需要转置的
        last = None 
        if count % k != 0:
            for _ in range(count % k):
                node = stack.pop()
                node.next = last
                last = node

        # 按块转置
        new_head = None
        for _ in range(count // k):
            new_head = stack.pop()
            curr = new_head
            for _ in range(k - 1):
                node = stack.pop()
                curr.next = node
                curr = curr.next
            curr.next = last
            last = new_head
        
        return new_head



            

'''
1. dummy
2. move linkedlist k - 1 times, cut them into a part, reverse, then connect

'''

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None and head.next == None:
            return head
        
        def reverse(head):
            '''
            return the reversed head and tail
            '''
            curr = None
            tail = head
            while head:
                next_head = head.next
                head.next = curr
                curr = head
                head = next_head
            
            return curr, tail
        

        dummy = ListNode()
        dummy.next = head
        s = dummy
        f = dummy

        while f:
            for _ in range(k):
                if f.next == None:  # 不是if f == None:
                    return dummy.next
                f = f.next
            
            next_f = f.next
            f.next = None

            new_head, new_tail = reverse(s.next)
            s.next = new_head
            new_tail.next = next_f
            
            s = new_tail
            f = new_tail  # key
        return dummy.next


        