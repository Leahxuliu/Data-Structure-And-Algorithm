# 时间复杂度 O(n*n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            flag = False
            find = False
            for j in nums2:
                if flag:
                    if j > i:
                        res.append(j)
                        find = True
                        break
                else:
                    if j == i:
                        flag = True

            if find == False:
                res.append(-1)
        return res

# 优化
# 把nums2放入到dict里
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        info = {each:i for i, each in enumerate(nums2)}
        res = []

        for i in nums1:
            index = info[i]
            flag = False
            for j in range(index + 1, len(nums2)):
                if nums2[j] > i:
                    res.append(nums2[j])
                    flag = True
                    break
            if flag == False:
                res.append(-1)
        return res

# 单调栈
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