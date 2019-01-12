#!/usr/bin/env python

import sys


def addBin(a,b):
    overflow, re = 0 ,0
    maxL = max(a.bit_length(),b.bit_length())
    for i in range(maxL+1):
        curBit = (a&1) ^ (b&1) ^ (overflow)
        re += curBit<<i
        overflow = ((a&1) + (b&1) + (overflow)) / 2
        a= a>>1
        b= b>>1
    print re
    return re

def main():
    a= int(sys.argv[1])
    b= int(sys.argv[2])
    addBin(a,b)

if __name__ == '__main__':
    main()
   
