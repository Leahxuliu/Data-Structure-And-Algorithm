# 0. 汇总





# 1. 快速排序

**复杂度**

* 时间复杂度 ：O(NlogN)
* 空间复杂度：取决于写法，如下代码是O(1)

**讲义**

https://docs.google.com/presentation/d/1QjAs-zx1i0_XWlLqsKtexb-iueao9jNLkN-gW9QxAD0/edit#slide=id.g463de7561_042

**如下代码的步骤**

* 所选的nums的最后一个数是基准数(pivot)
* 在start-index的地方放一个指针，用来储存小于等于pivot的数(注意，不是0！！！)
* 遍历nums，把小于等于pivot的数与指针i上的数进行交换（包括nums最后，也就是pivot）
* 最终pivot被挪到nums[i]，pivot左边与右边再进行sort
  * 为了确保inplace，所以要在原list上进行操作

```python
'''
quick sort
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
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
        return nums
```





# 2. 冒泡排序

**复杂度**

* 时间复杂度: 
  * Best case: O(N)
  * Average case: O(N^2)
  * Worst case: O(N^2)
* 空间复杂度: O(1)

**步骤**

- 每一轮中，把最大的数移动到最末尾
- 在nums[:-1]中，把最大的数移动到末尾
- 在nums[:-2]中，把最大的数移动到末尾
- 重复此过程，直到nums[0]

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return nums
        
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
```





# 3. 归并排序





