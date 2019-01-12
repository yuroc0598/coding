#!/usr/bin/python
import sys
# 1, find minimum insertion to convert a str to palindrome

def mini_insertion(s):
    dp = {}
    def helper(lo,hi):
        if (lo,hi) not in dp:
            if lo == hi:
                dp[(lo,hi)] = 0
            elif lo > hi: 
                dp[(lo,hi)] = 0
            else:
                if s[lo] == s[hi]:
                    dp[(lo,hi)] = helper(lo+1,hi-1)
                else:
                    dp[(lo,hi)] = min(helper(lo+1,hi),helper(lo,hi-1))+1

        return dp[(lo,hi)]
    return helper(0,len(s)-1)



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


s = sys.argv[1]
print "minimum insertion to convert '{}' to palindrome is {}".format(s,mini_insertion(s))
print "minimum insertion to convert '{}' to palindrome is {}".format(s,len(s)-longest_sub_sequence(s,s[::-1]))

