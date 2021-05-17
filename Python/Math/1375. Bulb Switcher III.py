'''
当前所有灯都是蓝色，那么亮灯的编号和必定等于1+2+...+亮灯数目

all bule:
sum(the index of turned on bulb) == (1 + 2 + 3 + ... the number of turned on bulb)
'''

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        if len(light) < 2:
            return len(light)
        
        blue = 0
        count = 0
        res = 0

        for i in range(len(light)):
            blue += light[i]
            count += i + 1
            if blue == count:
                res += 1
        return res