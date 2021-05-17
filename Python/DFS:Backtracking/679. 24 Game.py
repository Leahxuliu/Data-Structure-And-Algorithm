'''
backtracking

每次取两个数进行计算
'''

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        EPSILON = 1e-6

        def find(nums):
            if len(nums) == 1:
                return True if abs(nums[0] - 24) < EPSILON else False
            
            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    
                    new_list = []
                    # 把没有选中的number先放入new_list里面
                    for x in range(n):
                        if x != i and x != j:
                            new_list.append(nums[x])

                    # 对选了的两个数进行加减乘除的操作，得到的值放入new_list里面
                    # ADD, MULTIPLY, SUBTRACT, DIVIDE = 0, 1, 2, 3
                    for option in range(4):
                        # 优化（剪枝）加法和乘法的时候，a + b = b + a， a * b = b * a, 所以nums[i] > nums[j]剪枝
                        if option < 2 and i > j:
                            continue

                        # +
                        if option == 0:
                            count2 = nums[i] + nums[j]
                        # *
                        elif option == 1:
                            count2 = nums[i] * nums[j]
                        # -
                        elif option == 2:
                            count2 = nums[i] - nums[j]
                        # /
                        elif option == 3 and nums[j] != 0:
                            count2 = nums[i] / nums[j]

                        if find(new_list + [count2]):
                            return True
                    
            return False
        
        return find(nums)