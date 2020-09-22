#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/26

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            if isBadVersion(mid) == True:
                r = mid - 1
            else:
                l = mid + 1
        return l


