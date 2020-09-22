'''
merge两个list
LC 21
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 递归

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2


# 迭代
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    
    dummy = curr = ListNode(0)
    while l1 and l2:
        
        if l1.val < l2.val:
            node = ListNode(l1.val)
            l1 = l1.next
            curr.next = node
            curr = curr.next
        else:
            node = ListNode(l2.val)
            l2 = l2.next
            curr.next = node
            curr = curr.next
    
    if l1 != None:
        curr.next = l1
    
    if l2 != None:
        curr.next = l2
    
    return dummy.next