
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs):
        n = len(croakOfFrogs)
        m = n // 5

        if n % 5 != 0:
            return -1

        for i in 'croak':
            if croakOfFrogs.count(i) != m:
                return -1

        

X = Solution()
print(X.minNumberOfFrogs('crcoakroak'))