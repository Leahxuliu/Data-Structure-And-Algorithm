
'''
brout force
use backtacking to simulate jump 

'''
class Solution:
    def canCross(self, stones: List[int]) -> bool:

        if len(stones) < 2:
            return True

        if stones[1] > 1:
            return False
        
        def find(start, steps):
            '''simulation of jumpping 
            Args:
                start(int):the start index of stones
                steps(int): can jump k units
            Return:
                None
            '''
            if self.res:
                return
                
            if start == len(stones) - 1:
                self.res = True
                return 
            if start >= len(stones):
                return 
            
            minJ = max(steps - 1, 1)
            maxJ = steps + 1
            for k in range(minJ, maxJ + 1):
                next_uite = stones[start] + k
                if next_uite in info:
                    find(info[next_uite], k)
                    
            return 
        
        info = {}
        for i, each in enumerate(stones):
            info[each] = i


        self.res = False
        find(1, 1)
        return self.res


'''
DFS + memo

'''
class Solution:
    def canCross(self, stones: List[int]) -> bool:

        if len(stones) < 2:
            return True

        if stones[1] > 1:
            return False
        
        def find(start, steps):
            if (start, steps) in memo:
                return memo[(start, steps)]
                
            if start == len(stones) - 1:
                return True
            if start >= len(stones):
                return False
            
            res = False
            minJ = max(steps - 1, 1)
            maxJ = steps + 1
            for k in range(minJ, maxJ + 1):
                next_uite = stones[start] + k
                if next_uite in info:
                    if find(info[next_uite], k):
                        res = True 
                        break

            memo[(start, steps)] = res
            return res
        
        info = {}
        for i, each in enumerate(stones):
            info[each] = i

        memo = {}
        find(1, 1)
        return find(1, 1)
