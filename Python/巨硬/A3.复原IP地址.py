'''
backtracking
'''

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if s == "":
            return []
        # 注意
        if len(s) > 12:
            return []
        
        def find(start, path):
            '''
            param: start(int), the index can be picked
            param: path(list), built addresses
            return None
            '''
            if start == len(s):
                if len(path) == 4:
                    res.append('.'.join(path))
                return 
            if start > len(s):
                return 
            
            curr = ""
            end = min(start + 3, len(s))
            for i in range(start, end):
                if s[i].isdigit() == False:
                    break

                curr += s[i]
                # 0-start
                if len(curr) != len(str(int(curr))):
                    break
                # more than 255
                if int(curr) > 255:
                    break
                # vaild
                path.append(curr)
                find(i + 1, path)
                path.pop()
            
            return 
        
        res = []
        find(0, [])
        return res 