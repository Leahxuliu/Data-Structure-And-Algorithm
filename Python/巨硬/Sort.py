# 912

# 堆排序

'''
快速排序
堆排序
merge排序

'''
# max-heap

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        if len(nums) == 1:
            return nums
        
        def sink_down(start, end):
            root = start
            
            while 2 * root <= end:
                child = 2 * root
                if child + 1 <= end and nums[child + 1] > nums[child]:
                    child += 1
                if nums[root] < nums[child]:
                    nums[root], nums[child] = nums[child], nums[root]
                    root = child
                else:  # 易忘！
                    break
            return 
        
        n = len(nums)
        for i in range(n - 1, -1, -1):
            sink_down(i, n - 1)

        for i in range(n - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            sink_down(0, i - 1)  # 注意是i - 1
        
        return nums


# merge

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        if len(nums) == 1:
            return nums
        
        def merge_sort(start, end):
            if start > end:
                return []
            if start == end:
                return [nums[start]]
            
            mid = start + (end - start) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid + 1, end)  # 是mid + 1而不是mid！！！
 
            i = 0
            j = 0
            arr = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr.append(left[i])
                    i += 1
                else:
                    arr.append(right[j])
                    j += 1
            if i < len(left):
                arr.extend(left[i:])
            
            if j < len(right):
                arr.extend(right[j:])

            return arr
        
        return merge_sort(0, len(nums) - 1)



# quick

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        if len(nums) == 1:
            return nums
        
        def quick_sort(start, end):
            if start > end:
                return 
            if start == end:
                return 
            
            pivot = nums[start]
            point = start + 1
            for i in range(start + 1, end + 1):
                if nums[i] < pivot:
                    nums[point], nums[i] = nums[i], nums[point]
                    point += 1
            
            nums[start], nums[point - 1] = nums[point - 1], nums[start]
            quick_sort(start, point - 2)
            quick_sort(point, end)

            return 

        quick_sort(0, len(nums) - 1)
        return nums