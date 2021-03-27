'''
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
'''

'''
1. 用一个carry来表示需要加的内容
2. 从右往左遍历

'''
def plusOne(digits):
    if digits == []:
        return [1]

    n = len(digits)
    i = n - 1
    carry = 1

    res = []
    while i >= 0 or carry:
        if i >= 0:
            carry += digits[i]
        res.append(carry % 10)
        carry //= 10
        i -= 1
    
    return res[::-1]
