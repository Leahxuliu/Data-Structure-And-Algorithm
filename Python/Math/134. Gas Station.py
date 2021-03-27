class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # corner case
        if sum(gas) < sum(cost):
            return -1
        if len(gas) == 1:
            return 0

        def travel(start, i, tank):
            if i > len(gas) - 1:
                i = 0
            if i == start:
                return start
            if tank < 0:
                return -1

            tank = tank + gas[i] - cost[i]
            if tank < 0:
                return -1
            return travel(start, i + 1, tank)
        
        # traversal the start
        for i in range(len(gas)):
            res = travel(i, i + 1, gas[i] - cost[i])
            if res != -1:
                return res
        return -1


'''
优化
若x出发，只能到达y，则：
x,y 之间的任何一个加油站出发，都无法到达加油站 y 的下一个加油站。

利用以上性质，在遍历的时候，可以省略x,y之间的点作为出发点
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # corner case
        if sum(gas) < sum(cost):
            return -1
        if len(gas) == 1:
            return 0

        def travel(start, i, tank):
            if i > len(gas) - 1:
                i = 0
            if i == start:
                return start
            if tank < 0:
                return i

            tank = tank + gas[i] - cost[i]
            return travel(start, i + 1, tank)
        
        # traversal the start
        i = 0
        while i >= 0 and i < len(gas):
            res = travel(i, i + 1, gas[i] - cost[i])
            if res == i:
                return res
            i = res
        return -1