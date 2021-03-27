# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        if n == 0:
            return -1
        
        def find_peak(mountain_arr):
            l = 0
            r = n - 1
            while l < r:
                mid = l + (r - l) // 2
                curr = mountain_arr.get(mid)
                if curr < mountain_arr.get(mid + 1):
                    l = mid + 1
                else:
                    r = mid 
            return r
                        
        def find_target(mountain_arr, start, end, target, key = lambda x: x):
            l = start 
            r = end
            target = key(target)

            while l <= r:
                mid = l + (r - l) // 2
                curr = key(mountain_arr.get(mid))
                if curr == target:
                    return mid
                elif curr < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        # [1,2,3,4,5,3,1] -> [1,2,3,4,5,-3,-1]
        peak = find_peak(mountain_arr)
        res = find_target(mountain_arr, 0, peak, target)
        if res != -1:
            return res
        res = find_target(mountain_arr, peak + 1, n - 1, target, lambda x: -x)
        return res
