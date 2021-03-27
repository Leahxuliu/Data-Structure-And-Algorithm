'''
1239. 串联字符串的最大长度

给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，
如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
'''

'''
回溯
选与不选

'''

from collections import defaultdict
def maxLength(arr):
    
    if arr == []:
            return 0
        
        def find(start, data, count):
            if start == len(arr):
                self.res = max(count, self.res)
                return 
            
            # 不选
            find(start + 1, data, count)

            # 选
            flag =  True
            for i, char in enumerate(arr[start]):
                if data[char] == 1:
                    flag = False
                    for j in range(i):
                        data[arr[start][j]] -= 1
                    return 
                else: 
                    data[char] += 1

            if flag:
                find(start + 1, data, count + len(arr[start]))
            
                for char in arr[start]:
                    data[char] -= 1

            
            return 
        
        self.res = 0
        find(0, defaultdict(int), 0)
        return self.res