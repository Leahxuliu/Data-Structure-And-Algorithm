# 每次取一个数，最左端或者最右端
# 取k次
# 找最大

'''
正确 但是超时
'''
class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        
        def DFS(card, k, Sum):
            if k == 0:
                return Sum

            Sum = max(DFS(card[1:], k - 1, Sum) + card[0], DFS(card[:-1], k - 1, Sum) + card[-1])
            return Sum
        
        return DFS(cardPoints, k, 0)



'''
依旧是超时
'''
class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        
        memo = {}
        def DFS(i, j, k, Sum):
            if k == 0:
                return Sum

            key = str(i) + 'a' + str(j)
            if key in memo:
                return memo[key]

            Sum = max(DFS(i+1, j, k - 1, Sum) + cardPoints[i], DFS(i, j - 1, k - 1, Sum) + cardPoints[j])
            memo[key] = Sum
            return Sum

        return DFS(0, n -1, k, 0)
X = Solution()
print(X.maxScore([1,2,3,4,5,6,1], 3))