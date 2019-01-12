#!/usr/bin/python3
import sys

def bitdiff_single(n1,n2):
    return numofone(n1^n2)


def bitdiff(nums): # assuming a 32-bit int size
    ans, L = 0,len(nums)
    for bit in range(0,32):
        mask = 1<<bit
        ones = 0
        for num in nums:
            if num & mask:
                ones += 1
        zeros = L - ones
        ans += ones*zeros*2
    return ans

if __name__ == '__main__':
    nums = list(map(int,list(sys.argv[1:])))
    print(bitdiff(nums))


