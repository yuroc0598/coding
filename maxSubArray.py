#!/usr/bin/env python

class Solution(object):
    def maxSubArray(self,nums):
        if not nums:
            return 
        L = len(nums)
        if L == 1:
            return nums[0]
        curMax = 0
        for i in range(1,L):
            if nums[i-1] <= 0 :
                curMax = nums[i]
            else:
                nums[i] += nums[i-1]
                curMax = max(nums[i],curMax)
        return curMax

def main():
    s = Solution()
    nums=[1,2,-3,4,-1,5,-1,1,3,4]
    print s.maxSubArray(nums)

if __name__ == '__main__':
    main()
