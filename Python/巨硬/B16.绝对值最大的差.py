'''
有十万个元素的数组，还有个数字k
每个元素有两个属性a，b
然后取k个数，求k个数的属性a的和与属性b的和做差的绝对值最大
max[sum(a) - sum(b)]
'''

from heapq import heapify, heappop, heappush, heappushpop


data = {1:[1, 2], 2:[3, 2], 3:[10,3], 4:[3,9]}

def find_max_diff(arr, K):
    if arr == []:
        return 0
    
    heap = []

    for i in arr:
        diff = abs(data[i][0] - data[i][1])
        if len(heap) < K:
            heappush(heap, diff)
        
        else:
            heappushpop(heap, diff)
    
    return sum(heap)


print(find_max_diff([1, 2, 3, 4], 2))