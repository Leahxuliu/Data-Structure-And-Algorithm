'''
有负数

前缀和+dictionary （key是前缀和，value是该前缀和出现的次数）
找是否存在count-k的值再dict里
'''
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if nums == []:
            return 0
        
        # key:prefix; value: times
        prefix = defaultdict(int)
        prefix[0] = 1
        count = 0
        res = 0

        for i in range(len(nums)):
            count += nums[i]
            res += prefix[count - k]  # 核心
            prefix[count] += 1
        
        # print(prefix)
        return res