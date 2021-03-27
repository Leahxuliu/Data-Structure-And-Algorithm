# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
stack 错误 例如[[1,2,3],[4,5,6,7]]

heap
'''
from heapq import heappush, heappop 
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists == [] or lists == [[]]:
            return None
        
        heap = []
        dummy = ListNode()
        curr = dummy

        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        while heap:
            node, index = heappop(heap)
            curr.next = ListNode(node)
            curr = curr.next
            if lists[index]:
                heappush(heap, (lists[index].val, index))
                lists[index] = lists[index].next
        return dummy.next
