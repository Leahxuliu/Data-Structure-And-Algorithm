'''
use the backtracking to simulate the restore
'''

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []

        def backtracking(start, address):
            if start == len(s) and len(address) == 4:
                count = 0
                for i, each in enumerate(address):
                    count += len(each)
                    if int(each) > 255:
                        return
                    if str(int(each)) != each:
                        return 
                if count == len(s):
                    RES.append('.'.join(address))
                return 
            
            for i in range(start, len(s)):
                # add into last str
                pre = address[-1]
                address[-1] = pre + s[i]
                backtracking(i + 1, address)
                address[-1] = pre

                # add into a new str
                address.append(s[i])
                backtracking(i + 1, address)
                address.pop()
            return
        
        RES = []

'''
优化
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []

        def backtracking(start, address):
            if int(address[-1]) > 255:
                return
            if str(int(address[-1])) != address[-1]:
                return
            if start == len(s) and len(address) == 4:
                RES.append('.'.join(address))
                return 
            if start >= len(s):
                return
            
            '''
            因为字符串是要连续的
            只需要start该位置的情况
            '''
            pre = address[-1]
            address[-1] = pre + s[start]
            backtracking(start + 1, address)
            address[-1] = pre

            address.append(s[start])
            backtracking(start + 1, address)
            address.pop()
            return
        
        RES = []
        backtracking(1, [s[0]])
        return RES


'''
idea from Li-chief
每一个str其实是三种情况，选1个char，选2个char，选3个char
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []

        def backtracking(start, address):
            if len(address) > 0:
                if int(address[-1]) > 255:
                    return
                if str(int(address[-1])) != address[-1]:
                    return
            if start == len(s) and len(address) == 4:
                RES.append('.'.join(address))
                return 
            
            for i in range(start, start + 3):
                if i >= len(s):
                    continue
                address.append(s[start:i + 1])  # i + 1 易错
                backtracking(i + 1, address)
                address.pop()

            return
        
        RES = []
        backtracking(0, [])
        return RES