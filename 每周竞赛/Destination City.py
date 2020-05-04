class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        info = {}
        
        for i, j in paths:
            if i in info:
                info[i] += 1
            else:
                info[i] = 1
            
            if j not in info:
                info[j] = 0
        
        for k,v in info.items():
            if v == 0:
                return k