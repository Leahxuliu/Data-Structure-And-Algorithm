'''
17. 电话号码的字母组合

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

'''

'''
backtracking

time complexity: O(3 ** n + 4 ** m)
space complexity: O(n + m)
'''

def letterCombinations(digits):
    data = {'1':[], '2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
    
    if digits == '':
        return []
    
    def find(start, path):
        if start == len(digits):
            if len(path) == len(digits):
                res.append(''.join(path))
            return  
        
        if digits[start] not in data:
            return 
        
        for each in data[digits[start]]:
            path.append(each)
            find(start + 1, path)
            path.pop()
        return 
    
    res = []
    find(0, [])
    return res
