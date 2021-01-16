class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        
        pre = first
        for i in encoded:
            pre = pre ^ i
            res.append(pre)
        
        return res