'''
166
'''

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = []

        # + or -
        if numerator * denominator < 0:  # 不能是if numerator < 0 or denominator < 0
            res.append('-')
        
        # change to positive
        numerator = abs(numerator)
        denominator = abs(denominator)

        # integer
        div, rem = divmod(numerator, denominator)
        res.append(str(div))
        if rem == 0:
            return ''.join(res)
        
        # float
        res.append('.')
        info = {}
        
        # 易错
        # 先判断，再加入dict，再除
        while rem:
            if rem in info:
                pre = info[rem]
                return ''.join(res[:pre]) + '(' + ''.join(res[pre:]) + ')' 

            info[rem] = len(res)
            rem *= 10
            div, rem = divmod(rem, denominator)
            res.append(str(div))
            

        return ''.join(res)



