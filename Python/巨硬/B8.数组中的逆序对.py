'''
剑指 Offer 51. 数组中的逆序对

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

输入: [7,5,6,4]
输出: 5
'''

'''
left [5, 7] right [4, 6]

left[l] > right[r], 也就意味着l（包括l）之后的num都比right[r]大
self.res += len(left) - l

'''

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        def merge_sort(start, end):
            if start > end:
                return []
            if start == end:
                return [nums[start]]
            
            mid = start + (end - start) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid + 1, end)

            arr = []
            l = 0
            r = 0
            while l < len(left) and r < len(right):
                if left[l] > right[r]:
                    self.res += len(left) - l  # 核心
                    arr.append(right[r])
                    r += 1
                else:
                    arr.append(left[l])
                    l += 1
            
            if l < len(left):
                arr.extend(left[l:])
                    
            if r < len(right):
                arr.extend(right[r:])

            return arr 
        
        self.res = 0
        merge_sort(0, len(nums) - 1)
        return self.res
