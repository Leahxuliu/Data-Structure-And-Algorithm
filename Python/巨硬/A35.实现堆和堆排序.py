'''
用list模拟完全二叉树，实现最小堆

head是index1处，永远保持最小
1. 初始化 heap
2. 加入新值
    a. 插入最末尾
    b. 上浮
3. poppush
    a. 与heap[1]比较，若小于heap[1]，无作为
    b. 把新值放入heap[1]，下沉

'''

class Minheap:
    def __init__(self):
        self.heap = [0]
    
    def rise_up(self):
        '''
        do rise up after appendding new value into self.heap
        rise_up: up the new value at optimal index 
        '''
        # 与上一层进行比较
        i = len(self.heap) - 1

        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
                i = i // 2
            else:
                break
        return 


    def sink_down(self):
        '''
        put the val in heap[1] into optimal place, and find the minVal
        put the minval into heap[1]
        '''
        
        i = 1
        n = len(self.heap)

        while i * 2 < n:
            # compare left child to right child
            child = i * 2
            if child + 1 < n:
                if self.heap[child + 1] < self.heap[child]:
                    child += 1
            
            # compare child to root
            if self.heap[child] < self.heap[i]:
                self.heap[child], self.heap[i] = self.heap[i], self.heap[child]
                i = child
            else:
                break
        return 


    def heappush(self, x):
        self.heap.append(x)
        self.rise_up()
        print(self.heap)
        return
    
    def heappoppush(self, x):
        if x < self.heap[1]:
            return x
        
        pop_val = self.heap[1]
        self.heap[1] = x
        self.sink_down()
        return pop_val
    
    def heappop(self):
        return self.heappoppush(float('inf'))
        


def sort(arr):
    heap = Minheap()
    for i in arr:
        heap.heappush(i)
    
    res = []
    for i in range(len(arr)):
        res.append(heap.heappop())
    return res
    


    

print(sort([4,5,1,3,6,7,8,4,3,2,1]))



class Solution: 
    def sink_down(self, heap, root, heap_len):
        i = root
        while i * 2 < heap_len:
            child = i * 2
            if child + 1 < heap_len and heap[child + 1] > heap[child]:
                child = child + 1
            if heap[child] > heap[i]:
                heap[child], heap[i] = heap[i], heap[child]
                i = child
            else:
                break
        return 

    def sortArray(self, nums: List[int]) -> List[int]:
        heap = nums
        for i in range(len(heap) - 1, -1, -1):
            self.sink_down(heap, i, len(heap))

        for i in range(len(heap) - 1, -1, -1):
            heap[i], heap[0] = heap[0], heap[i]
            self.sink_down(heap, 0, i)

        return heap

    

