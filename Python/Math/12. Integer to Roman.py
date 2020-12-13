class Solution:
    def intToRoman(self, num: int) -> str:
        info = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90:'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        res = ''
        while num > 0:

            for i in info.keys():
                if i <= num:  # 易错 一定要有=
                    res += info[i]
                    num -= i
                    break
        return res 
