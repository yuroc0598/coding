#!/usr/bin/python3

def find2num(nums):
    xorall = 0
    for num in nums:
        xorall ^= num
    x,y = 0,0
    comparebit = xorall & ~(xorall-1)
    for num in nums:
        if num&comparebit:
            x ^= num
        else:
            y ^=num

    return x,y

nums = [2, 4, 7, 9, 2, 4]
print(find2num(nums))
