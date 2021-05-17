'''
用一个队列模拟固定窗口

翻转原则：
被翻偶数次，A[i]不发生改变，如果A[i] == 0, 则还需要再翻
被翻奇数次，A[i]发生改变，如果A[i] == 1, 则现在变成了0，还需要再翻
--> len(queue) % 2 == A[i]

用一个队列模拟固定窗口
窗口里面放的是范围内被翻转过的index
queue[0]是K数组范围内被翻转过的第一个index
(也就是维持的是i-k+1 ～ i大小)

'''
from collections import deque
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        queue = deque()

        res = 0
        for i in range(n):
            if queue and i >= queue[0] + K:
                queue.popleft()
            
            if len(queue) % 2 == A[i]:
                if i + K > n:
                    return -1
                res += 1
                queue.append(i)
        return res


'''
没看明白
差分数组

1. 差分数组：diff[i] = A[i-1] - A[i]
2. 翻转区间 [l,r]，只会影响到 l 和 r+1 位置的差分值
    diff[l] += 1
    diff[r + 1] -= 1
3. 累加差分数组就是当前位置需要翻转的次数 change
4. 若 A[i]+change 是偶数，说明当前元素的实际值是 0。需要翻转 [i, i+K-1]
    直接将 change 加 1
    diff[i+K] 减 1
5. 若 i+K>n，则无法进行翻转操作，返回 -1

'''