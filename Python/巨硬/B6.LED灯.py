'''
LED7段式灯管的红绿灯，上面有数字表示红灯有多少秒，绿灯有多少秒
现在有些灯管是坏的，所以看到的数字可能不是正确的数字
比方说数字23红色部分是坏掉的灯管，黑色部分是现在看到的数字，问你真正的数字可能是什么，23 --> 88或者89
'''


change_data = {0: [8],
                1: [0, 1, 3, 4, 7, 8, 9],
                2: [8],
                3: [8, 9],
                4: [8, 9],
                5: [6, 8, 9],
                6: [8],
                7: [3, 8, 9], 
                8: [],
                9: [8]}

def find(arr):
    def dfs(i, path):
        if i == 2:
            res.append(path[:])
            return 
        
        for each in change_data[arr[i]]:
            dfs(i + 1, path + [each])
        return 

    res = []
    dfs(0, [])
    return res
    
    
arr = [2, 3]
print(find(arr))
