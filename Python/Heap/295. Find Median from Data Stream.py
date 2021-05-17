'''
https://leetcode-cn.com/problems/find-median-from-data-stream/solution/tu-jie-pai-xu-er-fen-cha-zhao-you-xian-dui-lie-by-/

'''
from heapq import * 
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []    

    def addNum(self, num: int) -> None:
        # 当两堆长度相同时，先加到大顶堆，再把大堆顶元素加到小顶堆
        if len(self.left) == len(self.right):
            heappush(self.left, -num)
            popVal = heappop(self.left) * (-1)
            heappush(self.right, popVal)
        # 当两堆长度不相同时，先加到小顶堆，再把小堆顶元素加到大顶堆
        else:
            heappush(self.right, num)
            popVal = heappop(self.right) * (-1)
            heappush(self.left, popVal)
        return 


    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-1 * self.left[0] + self.right[0]) / 2.0
        else:
            return self.right[0] * 1.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()