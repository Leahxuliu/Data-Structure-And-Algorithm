class Solution:
    def dayOfYear(self, date: str) -> int:
        data1 = {0:0, 1: 31, 2: 59, 3: 90, 4: 120, 5: 151, 6:181, 7: 212,  
                8: 243, 9: 273, 10: 304, 11: 334, 12: 365}
        
        data2 = {0:0, 1: 31, 2: 60, 3: 91, 4: 121, 5: 152, 6:182, 7: 213,  
                8: 244, 9: 274, 10: 305, 11: 335, 12: 366}

        date = date.split('-')
        year = int(date[0])
        flag = False

        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            flag = True
        
        def count(month, day, data):
            return data[month - 1] + day
        
        if flag:
            return count(int(date[1]), int(date[2]), data2)
        else:
            return count(int(date[1]), int(date[2]), data1)