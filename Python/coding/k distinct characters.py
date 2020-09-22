'''
Count number of substrings with exactly k distinct characters / return list of strings

Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly k distinct characters. If the given string doesn't have k distinct characters, return 0.
https://leetcode.com/problems/subarrays-with-k-different-integers

Example 1:

Input: s = "pqpqs", k = 2
Output: 7
Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
Example 2:

Input: s = "aabab", k = 3
Output: 0
Constraints:

The input string consists of only lowercase English letters [a-z]
0 ≤ k ≤ 26
'''


from collections import defaultdict

def subarraysWithKDistinct(self, s, K):
    if s == '':
        return 0
    
    def count(s, T):
        l = 0  # left pointer
        c_info = defaultdict(int)
        count = 0
        res = 0
        
        for r, each_s in enumerate(s):
            if c_info[each_s] < 1:
                count += 1
            c_info[each_s] += 1
            while count > T:
                c_info[s[l]] -= 1
                if c_info[s[l]] == 0:
                    count -= 1
                l += 1
        
            res += r - l + 1
        return res
        
    return count(K) - count(K - 1)


# 大佬答案
import collections
def subarraysWithKDistinct(self, A, K):
    return self.atMostK(A, K) - self.atMostK(A, K - 1)

def atMostK(self, A, K):
    count = collections.Counter()
    res = i = 0
    for j in range(len(A)):
        if count[A[j]] == 0: K -= 1
        count[A[j]] += 1
        while K < 0:
            count[A[i]] -= 1
            if count[A[i]] == 0: K += 1
            i += 1
        res += j - i + 1
    return res


# exactly(K) = atMost(K) - atMost(K-1) why????