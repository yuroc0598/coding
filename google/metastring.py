#!/usr/bin/python3
import sys
def metastring(a,b):
    if len(a) != len(b):
        return False
    diff = 0
    in1, in2 = -1 ,-1
    for i in range(len(a)):
        if a[i]!=b[i]:
            diff += 1
            if diff>2:
                return False
            if diff == 1:
                in1 = i
            if diff == 2:
                in2 = i
    return a[in1] == b[in2] and a[in2] == b[in1]


a=sys.argv[1]
b=sys.argv[2]
print(metastring(a,b))
