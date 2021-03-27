'''
 [0, 1, 2, 4, 5, 7]
  s        s
  f  f  f  f     f

'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # corner case
        if nums == []:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        # use two pointers(fast and slow) to find the smallest sorted list
        res = []
        s = 0
        f = 0
        
        while s < len(nums) and f < len(nums):
            while f + 1 < len(nums) and nums[f] + 1 == nums[f + 1]:
                f += 1
            if s == f:
                res.append(str(nums[s]))
                s += 1
                f += 1
            else:
                res.append('%d->%d' % (nums[s], nums[f]))
                s = f + 1
                f += 1
        return res



