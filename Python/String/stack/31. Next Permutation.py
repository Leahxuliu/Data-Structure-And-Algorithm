'''
1. 从右向左遍历，找到尽可能靠右的较小值,也就是第一个a[i] < a[j]时的a[i]
2. 找较大值，要尽可能的小，从右向左扫a[i:],找到第一个a[i]<a[j],a[j]就是较大值
3. 反转a[i+1:],使得a[i+1:]部分是降序
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        minIndex = -1
        maxIndex = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                minIndex = i
                break
        
        for j in range(len(nums) - 1, minIndex, -1):
            if nums[minIndex] < nums[j]:
                maxIndex = j
                break  
        
        if minIndex >= 0:
            nums[maxIndex], nums[minIndex] = nums[minIndex], nums[maxIndex]
        
        l = minIndex + 1
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return

