#!/usr/bin/python

def updateBIT(nums,bitree,i,add_val): # i is in nums
    n = len(nums)
    i += 1
    while i <=n:
        bitree[i] += add_val
        i += i & ~(i-1)


def getSum(bitree,i):
    i += 1
    ans = 0
    while i>0:
        ans += bitree[i]
        i -= i & ~(i-1)
    return ans


nums = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
bitree = [0]*(len(nums)+1)
print nums
for i in range(len(nums)):
    updateBIT(nums,bitree,i,nums[i])
print bitree
for i in range(len(nums)):
    print getSum(nums,bitree,i)
    
