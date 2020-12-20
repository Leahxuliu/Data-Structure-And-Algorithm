import random
'''
遍历list，i
随机random取一个i之后的数(一定要包括i位)，与i进行互换
反复
'''

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.lst = [i for i in nums]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.lst = [i for i in self.original]
        return self.lst


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.lst) - 1):
            swap_idx = random.randrange(i, len(self.lst))
            self.lst[i], self.lst[swap_idx] = self.lst[swap_idx], self.lst[i]
        return self.lst




# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()