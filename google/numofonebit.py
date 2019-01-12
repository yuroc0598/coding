#!/usr/bin/python3
import sys
def numofone(num):
    ans = 0
    while num:
        num = num&(num-1)
        ans += 1
    return ans


if __name__ == '__main__':
    num = int(sys.argv[1])
    print(numofone(num))
