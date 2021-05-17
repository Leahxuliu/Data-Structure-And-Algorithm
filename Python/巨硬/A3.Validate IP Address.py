'''
468
'''

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP == "":
            return "Neither"
        
        def checkIPv4(arr):
            for each in arr:
                if len(each) > 3 or each == "":
                    return False 
                for i in each:
                    if i.isdigit():
                        continue
                    return False 
                
                if int(each) > 255 or len(str(int(each))) != len(each):
                    return False
            return True
        
        def checkIPv6(arr):
            for each in arr:
                if len(each) > 4 or each == "":  # 注意
                    return False
                for i in each:
                    if i.isdigit():
                        continue
                    if i.isalpha():
                        if "a" <= i <= "f" or "A" <= i <= "F":
                            continue
                        else:
                            return False 
                    return False

            return True 


        arr = IP.split(".")
        if len(arr) == 4:
            if checkIPv4(arr):
                return "IPv4"
        arr = IP.split(":")
        if len(arr) == 8:
            if checkIPv6(arr):
                return "IPv6"
        return "Neither"
