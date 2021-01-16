**基础概念**

- 前提条件：已经排序好的序列
- 方法：首先与序列中间的元素进行比较, 如果小于这个元素, 就在当前序列的前半部分继续查找, 如果大于这个元素, 就在当前序列的后半部分继续查找,直到找到相同的元素, 或者所查找的序列范围为空为止.



**时间空间复杂度**

- 时间复杂度：O(log n)
- 空间复杂度：O（1）



**常考类型**

- 一维数组(从小到大sort / 部分sort / 旋转 (比如[5,6,7,2,3,4])):
  - 找Target
  - 找峰值
  - 找target第一次出现或者最后一次出现的位置
- 二维数组：
  - 行内递增且这一行比下一行小 / 行内递增，列内递增
- 易错点：注意数组里面是否存在重复数



# 1. 常规模版

while l <= r:

* l,r互换的时候跳出循环；
* lr可相等，这样边界的值也能够被考虑进去,
  * 比如[1],l,r都是0



## 1.1 常规找指定target

* 代表题：367
* 拓展：167 Two Sum II - Input array is sorted
  * 也可用对撞two points
  * 也可用dict
* 易错点！！！一定要注意是移动r还是l！！！

```python
# 从小到大sort好的数列arr
# 找到target的数，输出其index（0-based）
# 若不存在target，则输出-1

class Solution:
    def search(self, arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:  # l,r位置互换时，跳出循环，r,l可相等是为了边界也能被搜索
            mid = l + (r - l) // 2  # (l+r)//2 不这么写是为了防止超限
            if target == arr[mid]:
                return mid
            elif target < arr[mid]:
                r = mid - 1
            elif target > arr[mid]:
                l = mid + 1
        return -1
                
```



## 1.2 找target出现的第一个和最后一个

**l,r互换位置是很多解题的关键**

* l, r互换的位置也就是while结束循环的位置

* 若找不到target
  * 循环到l，r互换的位置，左边也就是比target小，右边也就是比target大
* 有target，且存在多个
  * 第一个： 返回l
  * 最后一个：返回r

代表题: 34.Find First and Last Position of Element in Sorted Array

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
         # 如果没有这些条件， [2,2]，8就会报错，因为l会out of range
        if nums[0] > target:
            return [-1, -1]
        if nums[-1] < target:
            return [-1, -1]
        
        def findFirst(target, start):
            l = start
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] >= target:  # 继续往右边找
                    r = mid - 1
                else:
                    l = mid + 1
            return l if nums[l] == target else -1  # 返回l，易错

        def findLast(target, start):
            l = start
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r if nums[r] == target else -1
        
        first = findFirst(target, 0)
        print(first)
        if first == -1:
            return [-1, -1]
        last = findLast(target, first)
        return [first, last]

```

# 2. 旋转

易忘，需要复习

例如：[4, 5, 6, 7, 0, 1, 2]

**关键点：**判断左边是不是sort，反之另一侧就是不sort

## 2.1 找明确Target

代表题：33，81

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] == nums[mid]:
                l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1 
```



## 2.2 找极值

代表题：153， 154

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        res = float('inf')
        while l <= r:
            mid = l + (r - l) // 2
            if nums[l] <= nums[mid]:
                res = min(res, nums[l])
                l = mid + 1
            else:
                res = min(res, nums[mid]) 
                r = mid - 1
        return res
```



# 3. 找峰值

容易忘

**while l <= r:**

* l,r互换的时候跳出循环；
* lr可相等，这样边界的值也能够被考虑进去,
  * 比如[1],l,r都是0



**while l < r:**

* lr相等时，跳出循环

* 因为判断峰值需要至少要有两个数字

  * nums[mid] > nuns[mid + 1]

  

代表题：162  852  5438

```python
# 关键点在比较 nums[mid] 与 nums[mid + 1]，然后判断是到峰，未到峰，已经过峰

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:  # return peak value's index
        if nums is None:
            return None

        l, r = 0, len(nums) - 1
        while l < r :  # 注意l不能等于r，r=mid，这样的话，会陷入无限循环
            mid = l + (r - l) // 2
            if nums[mid] <= nums[mid + 1]:  # mid还没到峰
                l = mid + 1  # 峰值不可能是mid
            if nums[mid] > nums[mid + 1]:  # mid是峰或者已经过峰
                r = mid  # 峰值可能是mid
        
        return r  # return的时候，l跟r都是同一个值
```



# 4. 二维数组

## 4.1 行内递增，下一行比上一行大

- 例如：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
- 代表题 74

```python
'''
方法一 brute force
方法二 按行进行binary search
'''

'''
想像成二维数组都拉成一长条
找中间点，开始search

n是行数，m是列数
一共有n*m个数
matrix[mid // m][mid % m]

时间复杂度: O(log(NM)) 
空间复杂度: O(1)
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        if n == 0 and m == 0:
            return False
        
        l = 0
        r = n * m - 1

        while l <= r:
            mid = l + (r - l) // 2
            num = matrix[mid // m][mid % m]
            if num == target:
                return True
            elif num > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
```



## 4.2 行内递增，列内递增

- 例如：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
- 代表题 240

```python
'''
方法一 brute force
方法二 按行进行binary search
O(nlog(m))
'''

'''
方法三
search space reduction
从matrix[m-1][0]开始找，也就是最左下角的数开始对比，如果比target大，往上走也就是i-1，如果比target小，往右走j+1

时间复杂度: O(M + N) 
空间复杂度: O(1)
'''

class Solution:
    def searchMatrix(self, matrix, target):
        if matrix == [] or matrix == [[]]:
            return False
        
        i = len(matrix) - 1
        j = 0
        while i >= 0 and j < len(matrix[0]):
            num = matrix[i][j]
            if num == target:
                return True
            elif num > target:
                i -= 1
            else:
                j += 1
        return False
```



```python
'''
方法四
diagoal bianry search
对角线上的点-横行search-竖列search

Time Complexity: O(logN!) < O(NlogN)
空间复杂度: O(1)
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [] or matrix == [[]]:
            return False

        def horizontal(i):
            l = i 
            r = len(matrix[i]) - 1

            while l <= r:
                mid = l + (r - l) // 2
                num = matrix[i][mid]
                if num == target:
                    return True
                if num > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False    
        
        def vertical(i):
            l = i 
            r = len(matrix) - 1
            
            while l <= r:
                mid = l + (r - l) // 2
                num = matrix[mid][i]
                if num == target:
                    return True
                if num > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False
        
        n = len(matrix)
        m = len(matrix[0])
        for i in range(min(m, n)):
            if horizontal(i):
                return True
            if vertical(i):
                return True
        return False
```



# 5. 二分答案法

* mid = l + (r - l) // 2
  * 这里的l，r不是index，而是integer，数值
* 大多数情况下用于求解满足某种条件下的最大（小）值



代表题

* 378. Kth Smallest Element in a Sorted Matrix

求第k小的数值

<img src="/Users/leah/Library/Application Support/typora-user-images/截屏2021-01-09 下午3.09.13.png" alt="截屏2021-01-09 下午3.09.13" style="zoom:50%;" />

```python
'''
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
return 13

对目标值进行二分的时候
如果用常规模版，那么mid=14的时候，find(14) = 8
答案就会是14，可是14并不存在于matrix里面
所以当find(target) = k的时候，这里的target不一定是答案，需要进一步缩小
核心：找到第一个target值 + 二维里的search space reduction

'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        def find(target):
            n = len(matrix)
            i = n - 1
            j = 0
            num = 0

            while i >= 0 and j < n:
                if matrix[i][j] <= target:
                    num += i + 1  # don't forget +1
                    j += 1
                else:
                    i -= 1
            return num
        
        l = matrix[0][0]
        r = matrix[-1][-1]
        while l <= r:
            mid = l + (r - l) // 2
            num = find(mid) 
            if num >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l
```





# 5. 做题笔记

## 5.1 Math

* 判断一个数是否可以开平方（num）
  * 1，2，3单独考虑
  * 用二分搜索遍历1到num//2，mid*mid==num就可以被开平方
  * 参考 367





## 5.2 python





## 5.3 错题

* nums[mid] > target则移动r, r = mid - 1
  * 大了就减，r = mid -1
  * 小了就加,  l = mid + 1



### 5.3.1 Median of Two Sorted Arrays

* LC 4
* 