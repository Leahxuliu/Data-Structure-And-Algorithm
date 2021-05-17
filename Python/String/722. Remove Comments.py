class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        if source == []:
            return []
        
        res = []
        block_flag = False
        n = len(source)
        level = []

        for line in source:
            m = len(line)
            i = 0
            if block_flag == False:
                level = []

            while i < m:
                each = line[i:i + 2]
                if block_flag == False:
                    if each == '//':
                        break
                    elif each == '/*':
                        block_flag = True
                        i += 2
                    else:
                        level.append(line[i])
                        i += 1
                
                else:
                    if each == '*/':
                        block_flag = False
                        i += 2
                    else:
                        i += 1
            
            if level and block_flag == False:
                res.append(''.join(level))

        return res
