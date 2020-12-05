'''
dict + heap
核心： 到x时构成的序列长度（存储数组中的每个数字作为结尾的子序列的数量），x值有几个，就一定有几段序列

时间复杂度：O(n \log n)O(nlogn)，其中 nn 是数组的长度。
'''

from collections import defaultdict
from heapq import *

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = defaultdict(list)

        for i in nums:
            #if i - 1 not in count: wrong 
            # 因为这样的话，i-1已经被使用完，清空后，虽然是[]但是是有这个key的
            # 比如[1,2,3,4,5,5,6] 第二个5的时候就会报错
            if count[i - 1] == []:
                # count[i] = [1]  wrong
                # 比如[1,2,3,3,4,5] 第二个3的时候，2里面是空的，3里面有一个3，这个时候是要往3里面append 
                heappush(count[i], 1)
            
            else:
                #print(count)
                min_len = heappop(count[i - 1])
                count[i].append(min_len + 1)

        for each in count.values():
            if len(each) > 0 and each[0] < 3:
                return False
        return True

'''
时间复杂度：O(n)

贪心
1. 把每个数值出现的次数储存到dict里
2. 遍历nums（x），同时用一个dict储存以改字母结尾的序列个数
3. 如果x-1存在序列个数，x-1的序列个数-1，x的序列个数+1，x的出现次数-1
4. 如果x-1不存在序列个数
    如果有可以使用的x+1，x+2，x+2的序列个数+1，x，x+1,x+2的出现次数-1
    如果不能构成长度为3的序列，则return false
'''

from collections import Counter, defaultdict
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        countMap = Counter(nums)
        seqCount = Counter()  # 这里用Counter要比defaultdict要好，因为可以不管是否有这个key

        for x in nums:
            if countMap[x] == 0:
                continue
                
            if seqCount[x - 1] >= 1:
                seqCount[x - 1] -= 1
                seqCount[x] += 1
                countMap[x] -= 1
            else:
                if countMap[x + 1] >= 1 and countMap[x + 2] >= 1:
                    seqCount[x + 2] += 1
                    countMap[x] -= 1
                    countMap[x + 1] -= 1
                    countMap[x + 2] -= 1
                else:
                    return False
        return True
        