class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.allNums = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.allNums:
            self.allNums[number] += 1
        else:
            self.allNums[number] = 1
        return 

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for k, v in self.allNums.items():
            diff = value - k
            if diff in self.allNums:
                if diff != k:
                    return True
                else:
                    if self.allNums[diff] >= 2:
                        return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        visited = set()
        for elem in self.lst:
            if (value - elem) in visited:
                return True
            else:
                visited.add(elem)
        return False
