'''
LC:138 Copy List with Random Pointer 
'''

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# DFS + Dict
def copyRandomList(head):
    if head == None:
        return None

    def helper(head):
        if head == None:
            return None
        if head in newList:
            return newList[head]

        node = Node(head.val, None, None)
        newList[head] = node

        node.next = helper(head.next)
        node.random = helper(head.random)
        return node

    newList = {}
    helper(head)
    return newList[head]

# B 最好理解
def copyRandomList(head):
    if head == None:
        return 
    
    def getCloneNone(node):
        if node == None:
            return None

        if node not in info:
            info[node] = Node(node.val, None, None)
            return info[node]
        else:
            return info[node]

    info = {}
    curr = head
    while curr:
        if curr not in info:
            info[curr] = Node(curr.val, None, None)
        
        node = info[curr]
        node.next = getCloneNone(curr.next)
        node.random = getCloneNone(curr.random)

        curr = curr.next
    
    return info[head]
