'''
double linkedlist
'''
class Node:
    def __init__(self,key = 0, val = 0, next = None, pre = None):
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.start = Node()
        self.end = Node()
        self.start.next = self.end
        self.end.pre = self.start
        self.data = {}

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        
        node = self.data[key]
        self.remove(node)
        self.add(node)
        return node.val 

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node = self.data[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            if self.size == self.capacity:
                self.data.pop(self.start.next.key)
                self.remove(self.start.next)
                self.size -= 1
            
            node = Node(key, value)
            self.add(node)
            self.size += 1
            self.data[key] = node
        return 
    
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = None
        node.next = None
        return 
    

    def add(self, node):
        preNode = self.end.pre
        preNode.next = node
        node.pre = preNode
        node.next = self.end
        self.end.pre = node
        return 



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)3.
