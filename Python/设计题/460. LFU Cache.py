class Node:
    def __init__(self, k = 0, v = 0, pre = None, next = None, freq = 0):
        self.key = k
        self.val = v 
        self.pre = pre 
        self.next = next 
        self.freq = freq

class LFUCache:

    def __init__(self, capacity: int):
        self.data = {}
        self.minfreq = float('inf')
        self.freq = {}
        self.capacity = capacity
        self.size = 0
        

    def get(self, key: int) -> int:
        if key in self.data:
            node = self.data[key]
            self.remove(node)
            node.freq += 1
            self.add(node)
            return node.val 
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 

        if key in self.data:
            node = self.data[key]
            node.val = value
            self.remove(node)
            node.freq += 1
            self.add(node)
            
        else:
            node = Node(key, value, None, None, 1)
            self.size += 1
            self.data[key] = node
            if self.size <= self.capacity:
                self.add(node)
                
            else:
                self.removeLastFreq(self.minfreq)
                self.add(node)
                
        return 
        

    def remove(self, node):
        preNode = node.pre 
        nextNode = node.next
        preNode.next = nextNode
        nextNode.pre = preNode
        node.pre = None
        node.next = None

        freq = node.freq
        if preNode.pre == None and nextNode.next == None:
            self.freq.pop(freq)
        if self.minfreq == freq:
            if not self.freq.keys():
                self.minfreq = float('inf')
            else:
                self.minfreq = min(self.freq.keys())
        return 
    
    def add(self, node):
        freq = node.freq
        if freq not in self.freq:
            start = Node()
            end = Node()
            start.next = node
            node.next = end
            end.pre = node 
            node.pre = start 
            self.freq[freq] = [start, end]
            if freq < self.minfreq:
                self.minfreq = freq
        else:
            start, end = self.freq[freq]
            preNode = end.pre
            preNode.next = node
            node.pre = preNode
            node.next = end
            end.pre = node
        return 
    
    def removeLastFreq(self, minfreq):
        if minfreq not in self.freq:
            return 
        start, end = self.freq[minfreq]

        node = start.next
        self.remove(node)
        self.data.pop(node.key)
        return 


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)