'''
0 - 19
20 - 99
100 Hundred
1000 thousand
1000,000 million 百万
1000,000,000 billion 亿
'''

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        top19 = 'Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Eleven, Twelve, Thirteen, Fourteen, Fifteen, Sixteen, Seventeen, Eighteen, Nineteen'.split(', ')
        tens = ', , Twenty, Thirty, Forty, Fifty, Sixty, Seventy, Eighty, Ninety'.split(', ')

        def find(number):
            if number == 0:
                return []
            if number < 20:
                return [top19[number]]
            if number < 100:
                return [tens[number // 10]] + find(number % 10)
            if number < 1000:
                return [top19[number // 100]] + ['Hundred'] + find(number % 100)
            
            for i, unit in enumerate(['Thousand', 'Million', 'Billion'], 1):
                if 1000 ** i <= number < 1000 ** (i + 1):
                    return find(number // (1000 ** i)) + [unit] + find(number % (1000 ** i))
    
        return ' '.join(find(num)) 