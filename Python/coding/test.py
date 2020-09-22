class Dog():
    weight = 0
    
    def makeNoise(self):
        if self.weight > 10:
            print("bark!") 

d = Dog()
d.weight = 15
d.makeNoise()