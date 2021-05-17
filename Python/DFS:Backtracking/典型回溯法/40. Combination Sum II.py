'''
有重复数
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == []:
            return []
        if sum(candidates) < target:
            return []
        
        candidates.sort()
        
        def find(start, count, path):
            if count == target:
                res.append(path[:])
                return 
            if start == len(candidates):
                return 

            for i in range(start, len(candidates)):
                # pass掉本层中重复的数字 核心
                if i >= start + 1 and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] + count <= target:
                    find(i + 1, count + candidates[i], path + [candidates[i]])
            return 
        
        res = []
        find(0, 0, [])
        return res