'''
用一个dict记录将要去匹配的单词
    key是字母
    value是单词，比如cat，如果c已经找到过了，那么现在这个cat应该是 a:at
如果已经匹配到单词的最后一个字母，那么子序列单词数加 1。
'''
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        info = defaultdict(list)

        for each in words:
            info[each[0]].append(each)
        
        res = 0
        for char in s:
            if info[char] != []:
                new_list = []
                for each in info[char]:
                    if len(each) == 1:
                        res += 1
                        continue
                    # 比如 bb
                    if each[0] == each[1]:
                        new_list.append(each[1:])
                    else:
                        info[each[1]].append(each[1:])
                info[char] = new_list
        return res