# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Middle of the Linked List
奇数就是中间那个node，偶数是中间右边那个node

不加dummy，s，f
最终s所在位置就是答案
'''
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        s = head 
        f = head 

        while f and f.next:
            s = s.next
            f = f.next.next
        
        return s