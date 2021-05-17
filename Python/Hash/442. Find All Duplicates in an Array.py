'''
in-place hash
原地hash
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        
        res = set()
        for i, each in enumerate(nums):
            while i + 1 != each:
                change_index = each - 1
                if nums[change_index] == each:
                    res.add(each)
                    break
                nums[i], nums[change_index] = nums[change_index], nums[i]
                each = nums[i]  # 勿忘！
        return list(res)