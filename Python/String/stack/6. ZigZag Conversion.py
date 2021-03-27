class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s

        res = ['' for _ in range(numRows)]
        i = 0
        flag = -1

        for each in s:
            res[i] += each

            if i == 0 or i == numRows - 1:
                flag = - flag
            
            i += flag
        
        return ''.join(res)