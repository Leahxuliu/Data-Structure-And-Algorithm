from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        target = k

        # store the nums into dict, key: integer; value: list, indexs
        info = defaultdict(list)
        for i, each in enumerate(nums):
            info[each].append(i)

        # traversal the integer in the dict and count the difference between i and j
        for k, v in info.items():
            n = len(v)
            for i in range(n):
                if i == n - 1:
                    continue 
                if v[i + 1] - v[i] <= target:
                    return True
        return False


# 优化一
# 在保存到dict里的同时判断是否有这样的两个数

# 优化二
# 用一个k大小的窗口去找
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if nums == []:
            return False
        
        window = set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True

            window.add(nums[i]) 
            if len(window) > k:
                window.discard(nums[i - k])
        return False