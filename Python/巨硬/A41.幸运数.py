'''
给一个大整数，和几个幸运数字，求比大整数小的全部由幸运数字组成的整数的最大值

例子
[1, 2, 4]  123  --> 122
'''



'''
核心
1. 是否成立
2. 是否需要降位
3. 如果需要降位的话，最大数值*（n-1）
4. 如果不需要降位的话
    找到第一个不存在arr里的数值，这一位尽可能的大，然后后面位都是最大值
    这一位在arr里，但是之后都用minVal也要比luck数字大，这一位要替换掉
'''

def findMaxInteger(arr, integer):
    ''' return the max integer combine with arr,and smaller than input integer
    Arges:
        arr: list of int
        integer: int
    Return:
        int
    '''
    maxVal = max(arr)
    minVal = min(arr) 
    arr = set(arr)

    luck_num = str(integer)
    n = len(luck_num)
    # 不存在
    if minVal >= integer:
        return -1
    
    # 降位
    if int(str(minVal) * n) >= integer:
        return int(str(maxVal) * (n - 1))
    
    # 不降位
    res = -1
    for i, each in enumerate(luck_num):
        if int(each) not in arr or int(luck_num[:i + 1] + str(minVal) * (n - i -1)) >= integer:
            for new in arr:
                if new < int(each):
                    temp = luck_num[:i] + str(new) + str(maxVal) * (n - i - 1)
                    res = max(res, int(temp))
            break
    
    return res


res = findMaxInteger([3,5,7], 777)
print(res)
