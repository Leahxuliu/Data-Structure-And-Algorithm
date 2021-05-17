'''
hash + slide window
固定窗口, 窗口内的string保存在新的dictionary里面
判断两个dictionary是否相同


相似题 76 滑动窗口
详见76

'''
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == '':
            return True
        if s2 == '':
            return False
        if len(s1) > len(s2):
            return False
        
        info = defaultdict(int)
        for i in s1:
            info[i] += 1
        
        left = 0
        visited = defaultdict(int)
        for right in range(len(s2)):
            if right < len(s1):
                visited[s2[right]] += 1
            
            else:
                visited[s2[right]] += 1
                visited[s2[left]] -= 1

                if visited[s2[left]] == 0:
                    visited.pop(s2[left])
                
                left += 1

            if info == visited:
                return True       

        return False