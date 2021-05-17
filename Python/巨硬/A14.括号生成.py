class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ['()']
        
        def find(left, right, pair):
            if left == n and right == n:
                res.append(''.join(pair))
                return
            
            if left < n:
                pair.append('(')
                find(left + 1, right, pair)
                pair.pop()
            if right < left:
                pair.append(')')
                find(left, right + 1, pair)
                pair.pop()
            return

        res = []
        find(0, 0, [])
        return res