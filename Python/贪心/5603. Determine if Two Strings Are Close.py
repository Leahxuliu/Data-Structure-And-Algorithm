'''

解题思路
1.记录两个字符串每个字母的出现次数
2.比较两个字符串出现字母是否相同
3.比较出现次数是否一致
'''

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        info1 = {}
        info2 = {}
        for i, j in zip(word1, word2):
            if i in info1:
                info1[i] += 1
            else:
                info1[i] = 1
            
            if j in info2:
                info2[j] += 1
            else:
                info2[j] = 1
        
        diffAlp = 0
        diffTime1 = []
        diffTime2 = []
        
        for k, v in info1.items():
            if k not in info2:
                return False
            
            if info2[k] != v:
                diffTime1.append(v)
                diffTime2.append(info2[k])
        
        diffTime1.sort()
        diffTime2.sort()
        for i, j in zip(diffTime1, diffTime2):
            if i != j:
                return False
        
        return True