#/usr/bin/env python

class Solution(object):
    def myAtoi(self,s):
        # strip
        if not s:
            return 0
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
        dig = '0123456789'
        sign = '-+'    
        s = s[i:]
        if s[0] not in dig+sign:
            return 0
        pos = True
        if s[0] == '-':
            pos = False
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        i = 0 
        while i<len(s):
            if s[i] in dig:
                i += 1
        s=s[:i]
        if not s:
            return 0
        L = len(s)
        ans = 0
        for i in range(L):
            ans + = (ord(s[L-1-i]) - ord('0'))* (10**i)
        return ans if pos else -ans
