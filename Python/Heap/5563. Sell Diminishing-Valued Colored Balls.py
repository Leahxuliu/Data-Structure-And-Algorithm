# heap
# 超出时间限制

from heapq import *

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def count(x, y):
            return (x + (x - y + 1)) * y // 2

        if len(inventory) == 1:
            return count(inventory[0], orders) % (10 ** 9 + 7)
        
        heap = [-x for x in inventory]
        heapify(heap)
        maxCurr = -heappop(heap)
        res = 0
        
        while (orders > 0):
            nums = 0
            if (len(heap) > 0):
                temp = -heappop(heap)
                nums = maxCurr - temp + 1
                heappush(heap, -(temp - 1))

                if nums > orders:
                    nums = orders
                
            else:
                nums = maxCurr
            
            res += count(maxCurr, nums)
            maxCurr = temp
            orders -= nums
        
        return res % (10 ** 9 + 7)

'''
orders = 12
invents  = [6, 10, 10]
1 2 3 4 5 6                 use 1
1 2 3 4 5 6 7 8 9 10        use 5
1 2 3 4 5 6 7 8 9 10        use 6
        |
nums[costs >=5] = 14
nums[costs >=6] = 11
所以找到第五列，随便选择12 - 11 个5 补齐
'''

'''
错
[2,8,4,10,6]
18

中间值是3，3的右边有20个数
3 4 5 6 7 8 9 10
3 4 5 6 7 8 
3 4 5 6 
3 4 

如果可以取3的话，取18个数的时候，优先取3而非剩下的4，取值如下
3 4 5 6 7 8 9 10
3 4 5 6 7 8 
3 4 5 6 

'''

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def count(x, y):
            return (x + (x - y + 1)) * y // 2

        def count2(mid, orders):
            res = 0
            
            for i in inventory:
                nums = 0
                if i >= mid:
                    nums = i - mid + 1
                    if orders < nums:
                        nums = orders
                res += count(i, nums)
                orders -= nums
            return res

        if len(inventory) == 1:
            return count(inventory[0], orders) % (10 ** 9 + 7)

        l = 1
        inventory = sorted(inventory, key = lambda x:-x)
        r = inventory[0]

        while l <= r:
            mid = l + (r - l) // 2
            rightNumb = sum(elem - mid + 1 for elem in inventory if elem >= mid) # right Part Numb Sum of mid
            if rightNumb == orders:
                return count2(mid, orders) % (10 ** 9 + 7)
            elif rightNumb > orders:
                l = mid + 1
            else:
                r = mid - 1
        # 错误点
        return count2(r, orders) % (10 ** 9 + 7)


# 订正
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def count(x, y):
            return (x + (x - y + 1)) * y // 2

        def count2(mid, orders):
            res = 0
            
            for i in inventory:
                nums = 0
                if i >= mid:
                    nums = i - mid + 1
                    if orders < nums:
                        nums = orders
                res += count(i, nums)
                orders -= nums
            return res

        if len(inventory) == 1:
            return count(inventory[0], orders) % (10 ** 9 + 7)

        l = 1
        inventory = sorted(inventory, key = lambda x:-x)
        r = inventory[0]
        

        while l <= r:
            mid = l + (r - l) // 2
            rightNumb = sum(elem - mid + 1 for elem in inventory if elem >= mid) # right Part Numb Sum of mid
            if rightNumb == orders:
                return count2(mid, orders) % (10 ** 9 + 7)
            elif rightNumb > orders:
                l = mid + 1
            else:
                r = mid - 1

        rightNumb = sum(elem - l + 1 for elem in inventory if elem >= l)
        res = count2(l, orders) + (l - 1) * (orders - rightNumb)
        
        return res % (10 ** 9 + 7)
            