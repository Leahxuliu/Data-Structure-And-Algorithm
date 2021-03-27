from collections import defaultdict
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if len(A) < L + M:
            return 0
        
        prefix = [A[0]]
        for i in range(1, len(A)):
            prefix.append(prefix[-1] + A[i])
        
        res = prefix[L + M - 1]
        maxL = prefix[L - 1]
        maxR = prefix[M - 1]
        start = L + M - 1

        for i in range(start, len(prefix)):
            maxL = max(maxL, prefix[i - M] - prefix[i - L - M])
            m = prefix[i] - prefix[i - M]
            res = max(res, maxL + m)

            maxR = max(maxR, prefix[i - L] - prefix[i - L - M])
            l = prefix[i] - prefix[i - L]
            res = max(res, maxR + l)  
        return res