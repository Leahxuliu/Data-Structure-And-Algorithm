from collections import defaultdict
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if arr == []:
            return False
        if len(arr) % 2 == 1:
            return False
        
        remainders = defaultdict(int)
        for i in arr:
            remainders[i % k] += 1
        
        # for i in range(k // 2 + 1):
        #     if i == 0 or 2 * i == k:
        #         if remainders[i] % 2 != 0:
        #             return False
        #     else:
        #         if remainders[i] != remainders[k - i]:
        #             return False
        # 遍历remainders更加高效
        for key, value in remainders.items():
            if key == 0 or 2 * key == k:
                if value % 2 != 0:
                    return False
            else:
                if value != remainders[k - key]:
                    return False
        return True 

