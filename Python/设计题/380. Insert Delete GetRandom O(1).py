'''
用set的话，remove时候的时间复杂度不是O（1）
.remove(value)  --> O(n)
.pop(index) --> O(n-index)

用dict，key是num，value是index
remove 把list里面最后一位的与target互换，然后pop最后一位，这样时间复杂度就是o(1)
注意变化dict里面的index
'''

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data:
            return False

        self.lst.append(val)
        self.data[val] = len(self.lst) - 1
        return True 


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.data:
            return False
        
        index = self.data[val]
        self.data.pop(val)
    
        if self.lst[-1] == val:  # 如果value是lst的最后一位
            self.lst.pop()
        else:
            self.lst[index] = self.lst[-1]
            self.data[self.lst[index]] = index
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # index = random.randrange(len(self.lst))
        # return self.lst[index]
        # print(self.lst)
        return random.choice(self.lst)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()