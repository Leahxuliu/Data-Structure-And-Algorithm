class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return str(0)

        res = ''
        if num > 0: 
            flag = ''
        else:
            flag = '-' 
        
        num = abs(num)
        while num != 0:
            res = str(num % 7) + res
            num = num // 7
            
        return flag + res