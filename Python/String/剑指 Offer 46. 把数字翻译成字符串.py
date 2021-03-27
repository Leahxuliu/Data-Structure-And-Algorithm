class Solution:
    def translateNum(self, num: int) -> int:
        if num <= 9:
            return 1
        
        def find(start):
            if start == len(s):
                self.res += 1
                return

            # start:end
            # no 01
            if s[start] == '0':
                find(start + 1)
                return 

            for end in range(start, start + 2): 
                if end < len(s):
                    integer = s[start:end + 1]
                    if int(integer) <= 25:
                        find(end + 1)
            return

        s = str(num)
        self.res = 0
        find(0)
        return self.res