'''
设计一个类中的put
类内部有一个int size属性，然后另个数组，一个是用于存放key的，另一个用于存放value
key需要保持有序
然后如果key相同可以直接覆盖
index相同但是key不同的话，有元素的value是惰性删除，所以也可以覆盖

'''

class test:
    def __init__(self, x):
        self.size = 0
        self.key = []
        self.value = []
