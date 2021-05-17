'''
写了一道题，大概意思就是给定一个字符串'aaabbbccc{{a}b{c}}'
然后可替换的部分'a: [d, e], c: [f], dbf: [x], ebf: [y]'
最后返回所有可能生成的字符串
'''

def change_string(s, data):
    if s == "":
        return ""

    def change(s, start, path):
        nonlocal res
        if start == len(s):
            res.add(''.join(path))
            return 
        if start > len(s):
            return 
        
        temp_s = ""
        for i in range(start, len(s)):
            temp_s += s[i]
            if temp_s in data:
                for char in data[temp_s]:
                    # change
                    change(s, i + 1, path + [char])
                    # not change
                    change(s, i + 1, path + [temp_s])
            else:
                change(s, i + 1, path + [temp_s])
                break
        return 

    res = set()  # 注意去重
    change(s, 0, [])
    
    return list(res)

s = 'aaabbbccc{{a}b{c}}'
data = {'a': ['d', 'e'], 'c': ['f'], 'dbf': ['x'], 'ebf': ['y']}

test = change_string(s, data)
print(test)

if len(test) == len(list(set(test))):
    print(True)
else:
    
    print(False)
