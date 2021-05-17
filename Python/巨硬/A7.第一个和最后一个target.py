class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
        if target < nums[0] or target > nums[-1]:
            return [-1, -1]

        def find_first(nums, target):
            l = 0 
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    r = mid - 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l if nums[l] == target else -1  # 重点

        
        def find_last(nums, target):
            l = 0 
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return r if nums[r] == target else -1   # 重点

        first = find_first(nums, target)
        if first == -1:
            return [-1, -1]
        last = find_last(nums, target)
        return [first, last] 
