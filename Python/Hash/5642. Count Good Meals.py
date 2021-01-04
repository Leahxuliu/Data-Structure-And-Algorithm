# 超时
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        d = deliciousness
        
        def backtraking(start, meal, d):
            if len(meal) == 2 and sum(meal) in info:
                self.res += 1
                return
            
            for i in range(start, len(d)):
                meal.append(d[i])
                backtraking(i + 1, meal, d)
                meal.pop()
            return
        
        self.res = 0
        info = set()
        info.add(0)
        info.add(1)
        pre = 1
        for i in range(50):
            info.add(pre * 2)
            pre = pre * 2
        #backtraking(0, [], d1)
        backtraking(0, [], d)
        return self.res % (10 ** 9 + 7)

# dict
# 类似two sum
from collections import defaultdict

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        info = defaultdict(int)
        power = [2 ** i for i in range(22)]
        
        res = 0
        for i in deliciousness:
            for j in power:
                res += info[j - i]
            info[i] += 1
        
        return res % (10 ** 9 + 7)