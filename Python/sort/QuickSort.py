def partition(arr,low,high): 
    i = low
    pivot = arr[high]     
  
    for j in range(low , high): 
  
        # 当前元素小于或等于 pivot 
        if arr[j] <= pivot: 
            arr[i],arr[j] = arr[j],arr[i]
            i = i+1 
  
    arr[i],arr[high] = arr[high],arr[i] 
    return i
  
 
# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引
  
# 快速排序函数
def quickSort(arr,low,high): 
    if low < high: 
        
        pi = partition(arr,low,high) 
        print(pi, low, high)
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
#arr = [10, 7, 8, 9, 1, 5] 
arr = [0, 0]
n = len(arr) 
quickSort(arr,0,n-1) 
print ("排序后的数组:") 
for i in range(n): 
    print ("%d" %arr[i])


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
        