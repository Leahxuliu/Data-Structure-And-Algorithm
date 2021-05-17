class Solution:
    def countAndSay(self, n: int) -> str:
        def find(n):
            if n == 1:
                return '1'

            
            res = ''
            last = find(n - 1)
            count = 1  # 不能是0

            for i in range(1, len(last)):
                if last[i] == last[i - 1]:
                    count += 1
                else:
                    res += str(count) + last[i - 1]
                    count = 1
            
            if count != 0:
                res += str(count) + last[-1]
            return res
        
        return find(n)