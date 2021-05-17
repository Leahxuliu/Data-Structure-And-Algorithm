'''
1001个数字，全部都在1-1000内，所有数字都只出现一次，只有一个出现了两次，找到重复的数字，要用XOR
'''

'''
* ^ 异或（XOR）满足结合律
  * 相同是0， 不相同是1
  * a ^ b ^ c = a ^ (b ^ c) 
* 完整版的nums ^ 缺一个数的nums = 缺失的数
'''

def find_twice_number(arr):
    res1 = arr[0]
    for i in arr[1:]:
        res1 ^= i 
    
    res2 = 1
    for i in range(2, 1001):
        res2 ^= i
    
    return res1 ^ res2


arr = [i for i in range(1, 1001)] + [66]
print(find_twice_number(arr))

