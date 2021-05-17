# 先set去重，然后sort后，用while
# O(nlogn)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        # info = defaultdict(int)
        nums = list(set(nums))
        nums.sort()

        n = len(nums)
        i = 1
        res = 1
        while i < n:
            if nums[i] != nums[i - 1] + 1:
                i += 1
                continue

            count = 1
            while i < n and nums[i] == nums[i - 1] + 1:
                count += 1
                i += 1
            
            res = max(res, count)
        return res



# 方法二
# 哈希表  O(N)
# 也要去重
# n - 1不在arr里面说明这个n可能是最长subseq的start，开始寻找n+1，直到n+1不在arr里面
# 如果n-1在这个arr里面，说明这个是最长subseq当中的一部分
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        n = len(nums)
        nums = set(nums)
        res = 1

        for num in nums:
            if num - 1 not in nums:
                count = 1
                num += 1
                while num in nums:
                    count += 1
                    num += 1
                res = max(res, count)
            
        return res

            


