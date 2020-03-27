class Solution:
    def twoSum(self, numbers, target):
        if numbers == None:
            return []
        
        def find(T, arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = l + (r - l)//2
                if T == arr[mid]:
                    return mid
                elif T > arr[mid]:
                    l = mid + 1
                elif T < arr[mid]:
                    r = mid - 1
            return -1
        
        for i in range(len(numbers) - 1):
            new_T = target - numbers[i]
            index = find(new_T, numbers[i+1:])
            if index != -1:
                return [i+1, (i+1+index+1)]

x = Solution()
print(x.twoSum([2,7,11,15],9))           