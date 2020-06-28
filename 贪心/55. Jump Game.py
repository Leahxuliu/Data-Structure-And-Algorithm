'''
Greedy
1. traverse each step
2. find the most jump, most = i + nums[i]
3. if i <= most, renew most, most = max(most, i + nums[i])
4. if last index is equal or less most, return true,
   else return False
   
time: O(n)
space: O(1)
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums == []:
            return True
        
        most = 0
        for i, jump in enumerate(nums):
            if i <= most:
                most = max(most, i + jump)
                print(most)
            
        return most >= len(nums) - 1


    
'''
[2,3,1,1,4]
 0 1 2 3 4

most: 0, 2, 4
i: 0, 1, 2, 3
jump: 2, 3, 1, 1

return True

[3,2,1,0,4]
 0 1 2 3 4
 
 most:0, 3
 i: 0, 1, 2, 3, 4
 jump: 3, 2,1,0, 4
 i + jump: 3, 3, 3, 3

'''