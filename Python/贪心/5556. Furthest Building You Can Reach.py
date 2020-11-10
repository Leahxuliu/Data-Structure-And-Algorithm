# 贪心
# 如下case是错的
'''
[1,5,1,2,3,4]
4
1
'''

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        for i, each in enumerate(heights):
            if i == 0:
                continue
            
            temp = each - heights[i - 1]
            if temp <= 0:
                continue
                
            if temp > bricks and ladders == 0:
                return i - 1
            
            if temp <= bricks:
                bricks -= temp
            else:
                if ladders > 0:
                    ladders -= 1
        return len(heights) - 1

# 贪心的思想，用heap解决问题
'''
用L架梯子和B个砖块进行爬坡
梯子相当于一次性的无限量砖块，所以要用在刀刃上。
也就是说，梯子应该被用在坡度最大的时候，剩下情况用砖块

测试数据:
[1,5,1,2,3,4]
4
1

方法：
1. 维护一个L(梯子的个数)大的最小堆heap
2. 遍历坡度差
3. 将坡度差存入heap，若heap已满，则pop出最小值
4. pop出来的坡度差是需要用砖块来填充的，heap里面的高度差是用梯子来填充的
5. 当pop出来的坡度差超过砖块数时，也就意味着不能再继续爬了
'''
from heapq import *
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        used = 0
        for i in range(1, len(heights)):
            H = heights[i] - heights[i - 1]
            if H > 0:
                if len(heap) < ladders:
                    heappush(heap, H)
                else:
                    used += heappushpop(heap, H)
            if used > bricks:
                return i - 1
        
        return len(heights) - 1