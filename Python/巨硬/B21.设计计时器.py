'''
362. Design Hit Counter

双端队列
'''
from collections import deque
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        # self.times = 0
        # self.count = 0
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        # self.times = timestamp
        # self.count += 1
        self.queue.append(timestamp)
        while self.queue and self.queue[0] <= timestamp - 300:
            self.queue.popleft()
            # self.count -= 1
        
        return 

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        # self.times = timestamp
        while self.queue and self.queue[0] <= timestamp - 300:
            self.queue.popleft()
            # self.count -= 1
        # return self.count
        return len(self.queue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)