#!/usr/bin/python3

def threesum(nums):
    L = len(nums)
    i = 0
    nums.sort()
    ans = []
    while i < L-2:
        target = -nums[i]
        low = i+1
        high = L-1
        found = 0
        while low<high:
            mid = low+(high-low)>>1
            sm = nums[low]+nums[high]
            if sm == target:
                found = 1
                ans.append([nums[i],nums[low],nums[high]])
                low += 1
                high -= 1
                while low<high and nums[low]==nums[low-1]:
                    low += 1
                while low < high and nums[high] == nums[high+1]:
                    high -= 1
                    
            elif sm < target:
                low +=1
            else:
                high -= 1
        i += 1
        while i<L-2 and nums[i]==nums[i-1]:
                i += 1
    return ans


nums = [1,-2,1,0,5]
print(threesum(nums))
