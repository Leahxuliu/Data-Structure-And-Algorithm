class Solution:
    def intToRoman(self, num: int) -> str:
        if num == 0:
            return ''
        
        info = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 
                40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 
                500: 'D', 900: 'CM', 1000: 'M'}
        
        choose = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        res = ''
        
        while num > 0:
            for i in choose:
                if num - i >= 0:
                    res += info[i]
                    num = num - i 
                    break
        return res