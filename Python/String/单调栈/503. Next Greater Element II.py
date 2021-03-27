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