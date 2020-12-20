'''
two point - slide window
use a dict to store the number of integer


'''
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """ return the max value of erased subarray
        Args: 
            nums:List[int]
        
        Returns:
            max value:int
        """
        
        info = {}  # key: integer; value: index
        res = 0
        start = 0
        temp_sum = 0
        
        for i, each in enumerate(nums):
            if each in info:
                res = max(res, temp_sum)
                new_start = info[each] + 1
                for j in range(start, new_start):
                    temp_sum -= nums[j]
                    info.pop(nums[j])
                start = new_start
            info[each] = i
            temp_sum += each
            
        return max(res, temp_sum)