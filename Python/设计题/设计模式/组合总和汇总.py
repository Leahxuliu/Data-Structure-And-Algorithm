'''
39. Combination Sum

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

candidates里面没有重复数，但是可以重复利用
'''

# 方法一 选or不选
# 不需要先对candidates进行排序
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def find(start, count, path):
            if count == target:
                res.append(path[:])
                return 
            if start == len(candidates):
                return 
            
            # choose candidates[start]
            if count + candidates[start] <= target:
                find(start, count + candidates[start], path + [candidates[start]])

            # not choose candidates[start]
            find(start + 1, count, path)
            return 
        
        res = []
        find(0, 0, [])
        return res


# 先排序，然后用回溯的经典模版
# 因为这样的话就是剪枝了。时间会更加少
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        if target < candidates[0]:
            return []
        
        def find(start, count, path):
            if count == target:
                res.append(path[:])
                # print(start, path)
                return 
            if start == len(candidates):
                return 
            
            
            for i in range(start, len(candidates)):
                if candidates[i] + count <= target:
                    find(i, count + candidates[i], path + [candidates[i]])
                else:
                    # find(i + 1, count, path)  不需要！因为candidates是从小到大排好序的，这一轮已经超了，下一轮必然也是不符合要求的
                    break
            
            return 
        
        res = []
        find(0, 0, [])
        return res


'''
40. Combination Sum II

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

candidates里面有重复数，一个candidate只能用一次
注意output的去重
set里面不能放list，只能放tuple
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        if target < candidates[0]:
            return []
        
        def find(start, count, path):
            if count == target:
                res.append(path[:])
                # print(start, path)
                return 
            if start == len(candidates):
                return 
        
            for i in range(start, len(candidates)):
                # pass掉本层中重复的数字 核心
                # 所以 i >= start + 1  不是i>0
                # 核心是同层
                if i >= start + 1 and candidates[i - 1] == candidates[i]:
                    continue

                if candidates[i] + count <= target:
                    find(i + 1, count + candidates[i], path + [candidates[i]])
                else:
                    break
            
            return 
        
        res = []
        find(0, 0, [])
        return res


'''
377. Combination Sum IV

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.


nums里面没有重复数
找几种可能性
跟coin change2是否可以共享代码？ 不可，因为coin change2里面（1，3）和（3，1）是同一个
'''

'''
(3, 1)和（1，3）是两种情况的代码
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        if target < nums[0]:
            return 0
        
        dp = [0] * (1 + target)
        dp[0] = 1

        
        for i in range(target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[-1]


'''
(3, 1)和（1，3）是一种情况的代码
518. Coin Change 2

比如可选的有（1，2，3）
上面是选到2的时候，依旧可以选1
下面的代码是选到2的时候，2之前的就不能再选了
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        if target < nums[0]:
            return 0
        
        dp = [0] * (1 + target)
        dp[0] = 1

        for num in nums:
            for i in range(num, target + 1):
                dp[i] += dp[i - num]
        return dp[-1]