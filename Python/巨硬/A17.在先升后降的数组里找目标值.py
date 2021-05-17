'''
1095. Find in Mountain Array
'''

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        if mountain_arr == []:
            return -1
        if mountain_arr.length() == 1:
            return target == mountain_arr[0]
        
        def find_peak(arr):
            '''return the index of peak
            args:
                arr: mountain_arr list
            return:
                int
            '''
            l = 0
            r = arr.length() - 1

            while l < r:
                mid = l + (r - l) // 2
                if arr.get(mid) < arr.get(mid + 1):
                    l = mid + 1
                else:
                    r = mid
            return l 
        
        def find_target(start, end, flag):
            '''
            return the index of target index in mountain_arr[start:end + 1]
            (if can not find, return -1)
            '''
            l = start
            r = end

            while l <= r:
                mid = l + (r - l) // 2
                if mountain_arr.get(mid) == target:
                    return mid
                elif flag * mountain_arr.get(mid) > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        
        peak = find_peak(mountain_arr)
        res = find_target(0, peak, 1)
        if res != -1:
            return res
        else:
            return find_target(peak + 1, mountain_arr.length() - 1, -1)