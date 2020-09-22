'''
Method - Two pointers (fast and slow)
Steps:
    1. set i, j start at 0, 0
    2. if nums[j] == val, j += 1
       if nums[j] != val, nums[i] = nums[j], i += 1, j += 1
       
       3  2  2  3   val:3
       i  i
       j  j  j
    3. until j = the number of nums - 1
    4. return i
       
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums == []:
            return 
        
        i, j = 0, 0
        while j <= len(nums) - 1:
            if nums[j] == val:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        
        return i