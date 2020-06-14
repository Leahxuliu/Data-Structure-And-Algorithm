'''
input: nums: len(nums): 0~inf; sorted; repeated; int; the value of elements in nums: lower <= i <= upper
output: str
corner case: len(nums) == 0, return lower to upper


two pointer
1. lower + nunms + upper
2. set i, j start at first int and second int
    [0, 0, 1, 3, 50, 75, 100]
        s  f
    num[s] + 1 == nums[f], ok
    else, add nums[s] + 1 -> nums[f] - 1 into res
3. s += 1, f += 1 then repeat step2 until f == len(nums) - 1

time: O(n)
space:O(n)


'''

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums.insert(0, lower - 1)  # key
        nums.append(upper + 1)  # key
        
        i = 0
        j = 1
        res = []
        while j <= len(nums) - 1:
            if nums[i] == nums[j]:
                pass
            elif nums[i] + 1 == nums[j]:
                pass
            else:
                if nums[i] + 2 == nums[j]:
                    res.append(str(nums[i] + 1))
                else:
                    res.append('%d->%d' % (nums[i] + 1, nums[j] - 1))
            i += 1
            j += 1
        return res
                    
        