# 基本方法
# O(kn)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        while k > 0:
            last = nums.pop()
            nums.insert(0, last)
            k -= 1

# 技巧
# nums先reverse，然后前k个值互换，后k个值互换
# O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def change(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                
        k = k % len(nums)
        nums.reverse()
        change(0, k - 1)
        change(k, len(nums) - 1)