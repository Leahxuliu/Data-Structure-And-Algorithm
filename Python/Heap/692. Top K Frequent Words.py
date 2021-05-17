class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if words == []:
            return []
        
        info = defaultdict(int)
        for each in words:
            info[each] += 1
        
        sorted_info = sorted(info.items(), key = lambda x:[-x[1], x[0]])

        res = []
        for i in range(k):
            res.append(sorted_info[i][0])
        
        return res 

'''
用heap
'''

'''
次数：由大到小
字母：由小到大
'''
from heapq import heappop, heappush, heappushpop
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)

        K = k
        heap = []
        '''
        错误代码，因为这样顶端是次数最小且字母也最小
        次数相同的时候，字母小的反而被pop掉了，而题意是要字母大的
        '''
        for k, v in counter.items():
            if len(heap) < K:
                heappush(heap, (v, k))
            else:
                heappushpop(heap, (v, k))
            
        res = []
        while heap:
            res.append(heappop(heap)[1])
        return res[::-1]



'''
次数：由大到小
字母：由小到大

只能是先全部放入heap，max-heap（-v，k）这样就是次数：由大到小，字母：由小到大
然后pop
'''

from heapq import heappop, heapify
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)

        heap = [(-v, k) for k, v in counter.items()]
        heapify(heap)
        
        res = []
        for _ in range(k):
            res.append(heappop(heap)[1])
        return res