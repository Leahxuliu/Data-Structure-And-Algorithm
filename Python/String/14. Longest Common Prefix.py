'''
按单词横向扫
终止条件，单词长度，字母不相等
为了节约时间复杂度，把第一个单词当作res，然后再用一个len_res来记录最长公共prefix
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        
        res = strs[0]
        len_res = len(res)
        for word in strs[1:]:
            for i in range(len_res):
                if i >= len(word):  # 勿忘
                    len_res = i 
                    break
                if word[i] != res[i]:
                    len_res = i 
                    break
        return res[:len_res]


'''
方法二

纵向扫
扫第一个字母，然后扫第二个字母
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        
        res = ''
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if len(strs[j]) - 1 < i:
                    return res 
                if strs[j][i] != strs[0][i]:
                    return res 

            res += strs[0][i]
        return res 