'''
1. 从右往左遍历，找到第一位下降的数，a[i]
2. 从右往左遍历，找到第一个比a[i]大的数，a[j]
3. 交换a[i]和a[j]
4. 把a[i+1:]之后的数组进行转置
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return []
        
        n = len(nums)
        min_index = -1
        max_index = -1  # 如果for循环之后，依旧为-1，则认为没有找到

        # 从右向左遍历，找到第一个下降的数a[i]
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                min_index = i 
                break

         # 从右向左遍历，找到第一个比a[i]大的数字a[j]
        for i in range(n - 1, min_index, -1):
            if nums[i] > nums[min_index]:
                max_index = i 
                break

        # 交换a[i]和a[j]，然后把a[i+1]开始的到结尾的数进行转置
        if min_index != -1:
            nums[max_index], nums[min_index] = nums[min_index], nums[max_index]
            i = min_index + 1
            j = n - 1
        else:
            i = 0
            j = n - 1
        
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return 
    

