# 超时
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        def findMin(start, end):
            target = float(inf)
            index = 0
            for i in range(start, end):
                if target > nums[i]:
                    target = nums[i]
                    index = i
            return target, index
        
        res = []
        start = 0
        for i in range(k):
            target, index = findMin(start, len(nums) - (k - (i + 1)))
            res.append(target)
            start = index + 1
        
        return res
        



# 单调栈
# 要留下k个数字
# 也就是最多只能pop len(nums) - k次

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        #if nums == [] or k == 0:
        #    return []

        stack = []
        count = len(nums) - k

        for i in nums:
            while stack and count > 0 and i < stack[-1]:
                stack.pop()
                count -= 1
            stack.append(i)

        # 易错
        # [2,4,3,3,5,4,9,6]， k=4
        # 如果不取k个的话，答案是[2,3,3,4,6]
        return stack[:k]
        