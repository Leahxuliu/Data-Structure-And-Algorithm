'''
Xu

traversal the array and memo the number of consecutive
updata the max
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        res = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                res = max(res, count)
                count = 0
        # 易错
        res = max(res, count)
        return res
