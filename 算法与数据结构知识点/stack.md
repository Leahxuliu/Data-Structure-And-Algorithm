# 1. 单调栈

## 1.1 知识点

- 先进后出的逻辑顺序
- 栈内的元素都保持有序
  - 栈内元素单调递增或者单调递减的栈
- 单调栈只能在栈顶操作
- 单调栈的一大优势就是线性的时间复杂度，所有的元素只会进栈一次，而且一旦出栈后就不会再进来了。



**功能与用法 - 最近元素**

* 找到当前元素（当前元素指的是遍历到的那个元素，也就是即将放入stack的元素）左/右侧比自己小/大的最近元素
* 找左侧的元素：从左到右遍历
* 找右侧的元素：从右到左遍历
* 找下一个较大值，用递减
* 找下一个较小值，用递增
* 递增栈：stack弹出比顶部元素大的，stack剩下的就是最近的比顶部元素小的
  * 比如[1, 3, 4, 2] 递增stack，从左往右遍历
  * 遍历到2的时候，pop出来3，4，stack里面只留下1，这个1就是2左侧第一个比2小的元素

* 递减栈：stack弹出比顶部元素小的，stack剩下的就是最近的比顶部元素大的



**功能与用法 - 最远元素**

* 找到当前元素左/右侧比自己小/大的最远元素



## 1.2 模版

**递增**

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # 为了计算最后一个height
        stack = [-1]  # 必须要有，要保留开头
        largest = 0
        
        for i in range(len(heights)):
          # 注意判断是否需要等号
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                largest = max(largest, h * w)
            
            stack.append(i)
        
        return largest
```



**递减**

```python
class Solution:
    def findBiggerInteger(self, arr):
        stack = []
        res = [-1] * len(arr)
        arr.append(0)

        for i in range(len(arr)):
          # 注意判断是否需要等号
            while stack and arr[i] > arr[stack[-1]]:
                pre = stack.pop()
                steps = i - pre
                res[pre] = steps
            stack.append(i)
        return res

x = Solution()
print(x.findBiggerInteger([5, 3, 1, 2, 1, 4]))
```



## 1.3 LC题

### 1.3.1 Next Greater Number 

* 496.下一个更大元素I
  * 无重复数组
  * 右侧，下一个最大 --> 从右向左 单调递减

```python
# 从右向左 单调递减
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 == []:
            return []
        
        info = {}
        stack = []
        n = len(nums2)
        for i in range(n - 1, -1, -1):
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            if stack:
                info[nums2[i]] = stack[-1]
            else:
                info[nums2[i]] = -1
            stack.append(nums2[i])
        
        return [info[each] for each in nums1]
```



* 503.下一个更大元素II
  * circular array 

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        res = []
        n = len(nums)
        for i in range(2 * n - 1, -1, -1):
            index = i % n  
            while stack and nums[index] >= stack[-1]:
                stack.pop() 
            if stack:
                res.append(stack[-1])
            else:
                res.append(-1)
            stack.append(nums[index])

        # 注意取左边的n位，也就是res[::-1]里面的前n位
        return res[::-1][:n]
```

