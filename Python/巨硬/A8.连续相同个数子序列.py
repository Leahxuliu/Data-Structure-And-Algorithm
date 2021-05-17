'''
* 把0记成-1，1记成1来计算
* 用dictionary来保存，index和count
* 对于同值的count，只记录第一次出现时的index（因为是找符合条件的最长subarray）
* 符合条件的subarray：**i - info[count]**
  * 比如，现在count是-1，找info里面储存为-1的index，也就是说上一段-1，现在也是-1，也就是i-info[count]这一段，0，1个数相同，相加为0
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # corner case
        if nums == []:
            return 0

        info = {0: -1}  # 切记切记！
        count = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += -1
            else:
                count += 1
            
            # 不是0 - count是找count
            # 比如-2到-2，说明从-2点之后开始到再次到-2，这一段里面的0，1个数相同
            if count not in info:
                info[count] = i
            else:
                res = max(res, i - info[count])  # i - info[count]
        
        return res