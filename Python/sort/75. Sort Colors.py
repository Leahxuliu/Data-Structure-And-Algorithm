'''
因为只有0，1，2， 所以遍历第一次把所有0放到最前面，再遍历一次，把1放到前面
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        
        point = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[point], nums[i] = nums[i], nums[point]
                point += 1
        
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[point], nums[i] = nums[i], nums[point]
                point += 1
        
        #return nums


# quick sort
'''
quick sort
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        
        def quickSort(l, r):
            
            if len(nums) < 2 or l >= r:
                return 
            
            pivot = nums[r]
            point = l 
            
            # find the index of pivot after sort
            for i in range(l, r + 1):
                if nums[i] <= pivot:
                    nums[point], nums[i] = nums[i], nums[point]
                    point += 1

            # point - 1 is the index of pivot
            # left pivot right
            quickSort(l, point - 2)  # 易错，不是point - 1
            quickSort(point, r)
            return
        
        quickSort(0, len(nums) - 1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        
        def sort(start, end):
            if start > end:
                return 
            if start == end:
                return 

            # nums[start]作为pivot，把小于pivot的值往前挪 
            point = start + 1
            for i in range(start, end + 1):
                if nums[i] < nums[start]:
                    nums[i], nums[point] = nums[point], nums[i]
                    point += 1
                
            nums[start], nums[point - 1] = nums[point - 1], nums[start]  # 把pivot放到中间
            # start ~ point - 2 <= point - 1(pivot) <= point ~ end

            sort(start, point - 2)
            sort(point, end)
            return
        
        sort(0, len(nums) - 1)
        return 

'''
Bubble sort
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        #return nums
