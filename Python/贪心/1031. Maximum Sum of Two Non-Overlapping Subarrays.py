
'''
prefix + 固定窗口
L ｜ M
M ｜ L
两个变量固定一个
'''

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if L + M > len(A):
            return 0 
        
        prefix = [0]
        for i in A:
            prefix.append(prefix[-1] + i)
        
        res = prefix[L + M]
        maxL = prefix[L]
        maxM = prefix[M]
        
        for r in range(L + M, len(prefix)):      
            # L,M(r), 包括r端点的（L+M)长度窗口
            # maxL + curM 相当于遍历该窗口之前所有可能的L里面取最大L，然后加上该窗口内的M
            maxL = max(maxL, prefix[r-M] - prefix[r-M-L])
            curM = prefix[r] - prefix[r - M]
            res_LM = maxL + curM
            # print('LM', 'res:', res_LM, 'L:', prefix[r-M] - prefix[r-M-L], 'maxL:', maxL, 'M:', curM)
            
            # M,L(r)
            # maxM + curL 相当于遍历该窗口之前所有可能的M里面取最大M，然后加上该窗口内的L
            curL = prefix[r] - prefix[r-L]
            maxM = max(maxM, prefix[r-L] - prefix[r-L-M])
            res_ML = maxM + curL
            # print('ML', 'res:', res_ML, 'L:', curL, 'M:', prefix[r-L] - prefix[r-L-M], 'maxM:', maxM)
            res = max(res, res_LM, res_ML)

        return res