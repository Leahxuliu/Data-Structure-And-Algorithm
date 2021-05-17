'''
不用Python内置的dict类型，如何实现一个字典的setter方法(存key-value对)和getter方法（根据key取value）
key: int 
value: list

思路1：
two list
one save key
one save value

思路2
先建立list作为存储空间，长度为1000
取key的__hash__()属性的%1000的余作为放入list中的index
如果已经存在，则把value改为[value],再增加一个elem,[value, new_value]

核心：
把key变成hash code，hash code相当于list里面的index，把value放入到对应index里面
'''

class D:
    def __init__(self):
        self.dict = [[float('inf')] for _ in range(1000)]
    
    def setter(self, key, value):
        key_hasecode = key.__hash__() % 1000
        if self.dict[key_hasecode] == [float('inf')]:
            self.dict[key_hasecode] = [value]
        else:
            self.dict[key_hasecode].append(value)
        return 
    
    def getter(self, key):
        key_hasecode = key.__hash__() % 1000
        if self.dict[key_hasecode] == [float('inf')]:
            return "KeyError"
        else:
            return self.dict[key_hasecode]
         





# print('s'.__hash__() % 1000)

dict = D()
dict.setter(5, 6)
dict.setter(5, 6)
dict.setter(10, 6)
print(dict.getter(5))
print(dict.getter(6))


'''
hash code会有冲突
解决办法之一， 开放地址
https://harveyqing.gitbooks.io/python-read-and-write/content/python_advance/python_dict_implementation.html
'''

'''
706
1000个桶，桶里面放[key,value]
'''

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.map = [[] for _ in range(self.buckets)]

    def hashcode(self, key):
        return key % self.buckets

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        key_hashcode = self.hashcode(key)
        for each in self.map[key_hashcode]:
            if each[0] == key:
                each[1] = value
                return
        self.map[key_hashcode].append([key, value])
        return 


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        key_hashcode = self.hashcode(key)
        for each in self.map[key_hashcode]:
            if each[0] == key:
                return each[1]
                
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        key_hashcode = self.hashcode(key)
        for i, each in enumerate(self.map[key_hashcode]):
            if each[0] == key:
                self.map[key_hashcode].pop(i)
                return       
        return



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# key value分开储存也可以

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key = [[] for _ in range(1000)]
        self.value = [[] for _ in range(1000)]

    def get_hashcode(self, x):
        return x % 1000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashcode = self.get_hashcode(key)
        for i, each in enumerate(self.key[hashcode]):
            # print(each, key)
            if each == key:
                self.value[hashcode][i] = value
                return 
        self.key[hashcode].append(key)
        self.value[hashcode].append(value)
        return 


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashcode = self.get_hashcode(key)
        for i, each in enumerate(self.key[hashcode]):
            if each == key:
                return self.value[hashcode][i]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashcode = self.get_hashcode(key)
        for i, each in enumerate(self.key[hashcode]):
            if each == key:
                self.value[hashcode].pop(i)
                self.key[hashcode].pop(i)
                return 

        return 