#!/usr/bin/env python
import sys


def partition(nums):
    if not nums:
        return nums
    L = len(nums)
    left,right = 0, L-1
    while left<right:
        if nums[left] == 0:
            if nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
            right -= 1
        else:
            left += 1
    print nums



nums = [3,0,1,0,2,3,4]

partition(nums)
