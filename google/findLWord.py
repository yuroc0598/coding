#!/usr/bin/python3

import sys
def isSub(string,cur): # cur is shorter
    ls,lc = len(string),len(cur)
    if cur == string:
        return True
    curInd = 0
    for i in range(ls):
        if string[i]==cur[curInd]:
            curInd += 1
            if curInd == lc:
                return True
    
    return False

string = sys.argv[1]
cur = sys.argv[2]
print(isSub(string,cur))
    

