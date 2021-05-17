class ListNode:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.n = 0
        # key: the key of listnode; val: the pointer of the listnode
        self.data = {}
        self.start = ListNode()
        self.end = ListNode()
        self.start.next = self.end
        self.end.pre = self.start

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        curr = self.data[key]
        self.remove(curr)
        self.addnode(curr)
        return curr.val


    def put(self, key: int, value: int) -> None:
        if key in self.data:
            curr = self.data[key]
            curr.val = value
            self.remove(curr)
            self.addnode(curr)
            return 
        newNode = ListNode(key, value)

        if self.n < self.capacity:
            self.addnode(newNode)
        else:
            self.data.pop(self.start.next.key)
            self.remove(self.start.next)
            self.addnode(newNode)
        return 
    
    def remove(self, node):
        self.n -= 1
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = None
        node.pre = None
        return 
    
    def addnode(self, newNode):
        # print(newNode.key)
        self.n += 1
        tail = self.end.pre
        tail.next = newNode
        newNode.pre = tail
        newNode.next = self.end
        self.end.pre = newNode
        self.data[newNode.key] = newNode
        return 


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)