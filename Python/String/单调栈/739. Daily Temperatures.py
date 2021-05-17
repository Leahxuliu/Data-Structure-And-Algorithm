'''
monotone stack

decreasing
1. traversal the T in list
2. put T and index into stack
3. if T > stack[-1], pop stack and count the days


单调递减栈
把温度和index都放入stack
'''

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if T == []:
            return []
        
        stack = []
        res = [0] * len(T)

        for i in range(len(T)):
            while stack and stack[-1][0] < T[i]:
                pre_t, day = stack.pop()
                res[day] = i - day
            stack.append((T[i], i))
        
        return res