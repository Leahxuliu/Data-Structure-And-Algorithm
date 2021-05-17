'''
遍历string 储存到dictionary里
遍历dictionary的values，已经遇到过的value就-1，直到set里面没有该value
注意：value减到0的时候，这个值就不能再减了
'''
from collections import defaultdict
class Solution:
    def minDeletions(self, s: str) -> int:
        if s == '':
            return 0
        
        info = defaultdict(int)
        for i in range(len(s)):
            info[s[i]] += 1

        # nums = sorted(info.values(), key = lambda x:-x) 
        # res = 0
        # # print(nums)
        # i = 1
        # while i < len(nums):
        #     pre = nums[i - 1]
        #     if nums[i] != pre:
        #         i += 1
        #         continue 

        #     while i < len(nums) and nums[i] == pre:
        #         nums[i] = max(nums[i - 1] - 1, 0)
        #         res += max(pre - nums[i], 0)
        #         i += 1
        # return res                
        
        res = 0
        nums = set()
        for v in info.values():
            while v in nums:
                v -= 1
                res += 1
                if v == 0:
                    break

            nums.add(v)
        return res

from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def minDeletions(self, s: str) -> int:
        if len(s) < 2:
            return 0
        
        info = defaultdict(int)
        for i in s:
            info[i] += 1

        heap = []
        for i in info.values():
            heappush(heap, -i)
        
        res = 0
        while heap:
            curr = heappop(heap)
            if heap and curr == heap[0]:
                res += 1
                if curr + 1 < 0:
                    heappush(heap, curr + 1)
        return res

