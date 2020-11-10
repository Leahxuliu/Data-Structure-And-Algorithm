

class Solution:
    def minDeletions(self, s: str) -> int:
        info = {}
        for i in s:
            if i in info:
                info[i] += 1
            else:
                info[i] = 1
        
        sort = sorted(info.values(), key = lambda x:-x)
        
        res = 0
        temp = set()
        for i in sort:
            while (i in temp and i > 0):
                res += 1
                i -= 1
            
            temp.add(i)
        
        return res

'''
优化
首先统计各个字母的出现个数，再使用HashSet进行去重。
HashSet中保存不同的数目，如果加进来的数目已经存在，就自减，减到HashSet中没有的数目

为什么不用排序？例如添加顺序为4 4 3 2 1和3 2 1 4 4，
第一种是把4 3 2 1每个数都减1，答案为4。
第二种是直接把最后一个4减到0，答案也是4.
所以答案只需要在乎去重自减时，减少的个数，而不用在意顺序

'''