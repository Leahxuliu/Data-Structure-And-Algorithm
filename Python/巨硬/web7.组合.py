'''
39
有一个数组元素[a0, a1 ...]无重复元素。从数组里面找出所有可能的组合加和是n

sort
backtracking
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # if target > candidates[-1]:
        #     return []
        
        def find(start, count, path):
            if count == target:
                res.append(path[:])
                return 
            if count > target:
                return 

            for i in range(start, len(candidates)):
                curr = candidates[i]
                if count + curr <= target:
                    find(i, count + curr, path + [curr])
            return 
        
        res = []
        find(0, 0, [])
        return res