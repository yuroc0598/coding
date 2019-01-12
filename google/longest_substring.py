#!/usr/bin/python
import sys
def longest_sub_sequence(a,b): # sub sequence is a sequence of characters appearing in the same order in the org string, not necessarily contiguous
    la,lb,dp = len(a),len(b),{}
    def helper(posa,posb):
        if (posa,posb) not in dp:
            if posa == la or posb == lb:
                dp[(posa,posb)] = 0
            else:
                if a[posa] == b[posb]:
                    dp[(posa,posb)] = 1 + helper(posa+1,posb+1)
                else:
                    dp[(posa,posb)] =  max(helper(posa+1,posb),helper(posa,posb+1))
        return dp[(posa,posb)]
    return helper(0,0)

a,b =  sys.argv[1],sys.argv[2]
print longest_sub_sequence(a,b)
