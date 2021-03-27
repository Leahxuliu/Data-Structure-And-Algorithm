
def combinationSum(candidates, target):
    # corner case
    if sum(candidates) < target:
        return []
    if min(candidates) > target:
        return []
    
    def find(start, comb):
        print(comb, target)
        if sum(comb) == target:
            res.append(comb[:])
            return
        if sum(comb) > target or start >= len(candidates):
            return 

        for i in range(start,len(candidates)):
            comb.append(candidates[i])
            find(i, comb)
            comb.pop()
        return

    res = []
    find(0, [])
    return res

combinationSum([2,3,6,7], 7)


'''
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