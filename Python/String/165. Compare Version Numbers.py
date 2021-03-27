class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # split string by '.'
        v1 = version1.split('.')
        v2 = version2.split('.')

        i = 0
        j = 0

        # compare the v1 and v2
        while i < len(v1) and j < len(v2):
            if int(v1[i]) == int(v2[j]):
                i += 1
                j += 1
            elif int(v1[i]) > int(v2[j]):
                return 1
            else:
                return -1
        
        # len(v1) > len(v2)
        while i < len(v1):
            if int(v1[i]) > 0:
                return 1
            i += 1 

        # len(v1) < len(v2)
        while j < len(v2):
            if int(v2[j]) > 0:
                return -1
            j += 1

        return 0