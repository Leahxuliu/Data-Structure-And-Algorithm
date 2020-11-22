# 暴力
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []

        for i in range(len(A)):
            if i % 2 == 0 and A[i] % 2 != 0:
                odd.append(i)
            elif i % 2 != 0 and A[i] % 2 == 0:
                even.append(i)

        for i in range(len(odd)):
            temp = A[odd[i]]
            A[odd[i]] = A[even[i]]
            A[even[i]] = temp
        
        return A


# 双指针
# j 下一个不符合要求 且跟i能互换的点
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j = 0
        for i in range(len(A)):
            if i % 2 == 0 and A[i] % 2 != 0:
                while not (j % 2 != 0 and A[j] % 2 == 0):
                    j += 1
                A[i], A[j] = A[j], A[i]
                j += 1

            elif i % 2 != 0 and A[i] % 2 == 0:
                while not(j % 2 == 0 and A[j] % 2 != 0):
                    j += 1
                A[i], A[j] = A[j], A[i]
                j += 1
        
        return A


# 双指针
# 再优化
# i看偶数位，j看奇数位
# for i in rang(0, len(A), 2)
# j += 2
# 时间复杂度:O(N)
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2 != 0:
                while A[j] % 2 != 0:
                    j += 2
                A[i], A[j] = A[j], A[i]
                j += 2
        
        return A
            