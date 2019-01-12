#!/usr/bin/python

def minimum_square(l,w): # l longer than w
    dp = {}
    for i in range(1,max(l,w)+1):
        dp[(i,1)] = i
        dp[(i,0)] = 0
    dp[(0,0)] = 0
    def helper(a,b): # a larger than b
        if a<b:
            a,b = b,a
        if (a,b) not in dp:
            if a==b:
                dp[(a,b)] = 1
            else:
                ans = a*b
                for i in range(1,b+1):
                    tmp1 = 1 + helper(a-i,b)+helper(b-i,i)
                    tmp2 = 1 + helper(a-i,i)+helper(a,b-i)
                    ans = min(ans,tmp1,tmp2)
                dp[(a,b)] = ans
        return dp[(a,b)]
    return helper(l,w)

l,w = 36,30
print minimum_square(l,w)
    
