'''
1. len(pw) < 6, return 6 - len(pw)
    缺失的（一个小写字母，一个大写字母，一个数字）个数 （m个）
    return max(6 - len(pw), m) 
    比如aaaaa，用大写字母替换中间的，在最后加一个数字

2. 6<= len(pw) <= 20
    only swap
    需要swap的次数=repeat/3
    return max(swap, misstype)

3. len(pw) > 20
    至少要删除len - 20，尽可能删的是repeat的    
    aaaa -> swap 1 times
    aaaaa -> swap 1 times
    aaaaaa -> swap 2 times
    尽可能地往3k+2上减,也就是先删3k的

    

处理连续3次
不能只数有多少个超过连续3的情况
比如aaaaa的话，替换中间的a，一次就可
'''

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        def missingTypes(password):
            low = 0
            upper = 0
            digit = 0

            for i, each in enumerate(password):
                if 97 <= ord(each) <= 122:
                    low = 1
                elif 65 <= ord(each) <= 90:
                    upper = 1
                elif each.isdigit():
                    digit = 1
                
            return 3 - (low + upper + digit)
        
        def countRepeat(password):
            '''
            eg: aaaaabbbcc, return [5,3]
            '''
            res = []

            count = 1
            for i in range(1, len(password)):
                if password[i] == password[i - 1]:
                    count += 1
                else:
                    if count >= 3:
                        res.append(count)
                    count = 1
            
            if count >= 3:
                res.append(count)
            return res
                
        needTypes = missingTypes(password)

        if len(password) < 6:
            return max(needTypes, 6 - len(password))
        
        elif len(password) >= 6 and len(password) <= 20:
            repeats = countRepeat(password)
            swap = 0
            for each in repeats:
                swap += each // 3
            return max(swap, needTypes)

        else:
            needRemove = len(password) - 20
            repeats = countRepeat(password)
            # 要删的额度用到重复的地方
            # 最划算的删除是把连续重复的6个字母删成5个，也就是先删3k的

            i = 0
            while i < len(repeats) and needRemove > 0:
                if repeats[i] % 3 == 0:
                    needRemove -= 1
                    repeats[i] = repeats[i] - 1
                i += 1
            
            # 次优是删除3k + 1，删掉2个
            i = 0
            while i < len(repeats) and needRemove > 0:
                if repeats[i] % 3 == 1 and needRemove >=2:
                    needRemove -= 2
                    repeats[i] = repeats[i] - 2
                i += 1
            
            # 最后是3k + 2, 删掉3个
            i = 0
            while i < len(repeats) and needRemove > 0:
                while repeats[i] >= 3 and needRemove >= 3:
                    needRemove -= 3
                    repeats[i] = repeats[i] - 3
                i += 1
            
            swap = 0
            for each in repeats:
                swap += each // 3
            return max(needTypes, swap) + len(password) - 20