'''
384
'''

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.change = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.change = self.nums[:]
        return self.change

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.change)):
            j = random.randrange(i, len(self.change))
            self.change[i], self.change[j] = self.change[j], self.change[i]
        return self.change 
