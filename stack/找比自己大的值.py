'''
# https://zhuanlan.zhihu.com/p/26465701
给一个数组，返回一个大小相同的数组。
返回的数组的第i个位置的值应当是，对于原数组中的第i个元素，至少往右走多少步，
才能遇到一个比自己大的元素（如果之后没有比自己大的元素，或者已经是最后一个元素，则在返回数组的对应位置放上-1）。

简单的例子：

input: 5,3,1,2,4

return: -1 3 1 1 -1
'''

'''
Input: arr: list[int]; non-negative; repeated?
output: arr: list[int]

Method - monotone stack (big -> small)

'''

class Solution:
    def findBiggerInteger(self, arr):
        stack = []
        res = [-1] * len(arr)
        arr.append(0)

        for i in range(len(arr)):
            while stack and arr[i] > arr[stack[-1]]:
                pre = stack.pop()
                steps = i - pre
                res[pre] = steps
            stack.append(i)
        return res

x = Solution()
print(x.findBiggerInteger([5, 3, 1, 2, 1, 4]))