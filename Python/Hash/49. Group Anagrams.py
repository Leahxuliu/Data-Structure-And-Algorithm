from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == []:
            return []
        if len(strs) == 1:
            return [strs]
        
        info = defaultdict(list)
        for i in strs:
            sorted_i = sorted(i)
            info[''.join(sorted_i)].append(i)
        

        res = []
        for k, v in info.items():
            res.append(v)
        return res