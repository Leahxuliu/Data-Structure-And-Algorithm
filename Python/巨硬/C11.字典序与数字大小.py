'''
386
生成1-n的字典序数组
'''
def make_arr(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    
    def bulid(i):
        if i > n:
            return 
        
        res.append(i)
        for j in range(10):
            bulid(i * 10 + j)
        return 

    
    res = []
    for i in range(1, 10):
        bulid(i)
    return res

# 用stack 
# better
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        if n == 0:
            return []
        if n < 10:
            return [each for each in range(1, n + 1)]
        
        stack = [each for each in range(9, 0, -1)]  # 易错
        res = []
        while len(res) < n:        
            num = stack.pop()
            if num > n:
                continue

            res.append(num)
            if num * 10 <= n:
                for each in range(9, -1, -1):  # 要包含0，易错
                    stack.append(num * 10 + each)
        return res

'''
从字典序转变成数字顺序

按照位数输出
'''

def change_order(arr):
    if len(arr) < 2:
        return arr

    info = [[] for _ in range(len(arr) // 10 + 1)]
    for i in range(len(arr)):
        temp = arr[i] // 10 
        info[temp].append(arr[i])
    
    # res = [each for each in info]
    res = []
    for each in info:
        res.extend(each)
    return res

    
    
def check(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return False
    return True

# arr = make_arr(1650)
# print(arr)
arr = lexicalOrder(1234665)

arr = change_order(arr)
# print(arr)

print(check(arr))