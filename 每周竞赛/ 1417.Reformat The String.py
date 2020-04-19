class Solution:
    def reformat(self, s: str) -> str:
        if s == '':
            return ''
        if len(s) > 1:
            if s.isalpha() == True:
                return ''
            if s.isdigit() == True:
                return ''
        if len(s) == 1:
            return s
        
        a = []
        d = []
        
        for i in s:
            if i.isdigit():
                d.append(i)
            else:
                a.append(i)
                
        n = len(a)
        m = len(d)
        new_s = ''
        if n > m:
            for j in range(n):
                if j != n - 1:
                    new_s += a[j] + d[j]
                else:
                    new_s += a[j]
        elif m > n:
            for j in range(m):
                if j != m - 1:
                    new_s += d[j] + a[j]
                else:
                    new_s += d[j]
        else:
            for j in range(m):
                new_s += d[j] + a[j]
               
        return new_s