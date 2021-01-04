'''
1. 初始都是一颗糖
2. 从左往右遍历，i比i-1分数高，则i比i-1多一颗糖
3. 从右往左遍历，i比i+1分数高，则max(res[i], res[i + 1] + 1)
'''

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if ratings == []:
            return 0

        n = len(ratings)
        res = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                #res[i] = res[i + 1] + 1  # 错误 比如[1,3,4,5,2]， 从左到右扫完之后是[1,2,3,4,1],再从右往左扫时，倒是第二个变成了2
                res[i] = max(res[i], res[i + 1] + 1)
        return sum(res)    