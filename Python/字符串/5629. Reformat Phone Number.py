class Solution:
    def reformatNumber(self, number: str) -> str:
        """reformat number into 3 number
        Args:
            numbers: a string
        Returns:
            A string, the reformated string
        """
        res = []
        
        temp = ''
        for s in number:
            if s == ' ' or s == '-':
                continue
            
            temp += s
            if len(temp) == 3:
                res.append(temp)
                temp = ''
        
        if len(temp) >= 2:
            res.append(temp)
        elif len(temp) == 1:
            temp = res[-1][-1] + temp
            res[-1] = res[-1][:2]
            res.append(temp)
        
        return '-'.join(res)