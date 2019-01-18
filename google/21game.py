#leetcode 837, the first two method will exceed time or memo limit
from collections import deque
class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        # explanation: get points no less than K, each time the point can be [1,W], what is the pos of final point being less or equal to N
        # example: 10,1,10 -> 1
        # example: 6,1,10 -> 0.6
        if K == 0: return 1
        if K>N: return 0
        if N>=K-1+W: return 1
        if K == 1: 
            if N<W:
                return N/float(W) 
            return 1

        totalp = desp = 0
        pre = [[i,1/float(W)] for i in xrange(1,W+1)]
        pre = deque(pre)
        
        while pre:
            s,p = pre.popleft()
            if s<K:
                for j in xrange(1,W+1):
                        pre.append([s+j,p/float(W)])
            else:
                
                totalp += p
                if s<=N:
                    desp += p
        
        
        return float(desp)/totalp

    def new21Game1(self,N,K,W): # try to use dfs
        if K == 0: return 1
        if K>N: return 0
        if N>=K-1+W: return 1
        if K == 1: 
            if N<W:
                return N/float(W) 
            return 1

        self.totalp = self.desp = 0
        def helper(s,p):
            if s>=K:
                self.totalp +=p
                if s<=N:
                    self.desp += p
            else:
                for i in xrange(1,W+1):
                    helper(s+i,float(p)/W)

        helper(0,1)
        return self.desp/self.totalp

    def new21Game_leetcode(self,N,K,W): # intuition is, use f(x) to represent the p of success when we have x points, f(x) = 1 when x in [K,N], f(x) = 0 when x > N. f(x) = (sum(f(x+i)))/W, i in [1,W], use S(x)=f(x+1)+f(x+2)+...+f(x+W)
        if K == 0: return 1
        if K>N: return 0
        if N>=K-1+W: return 1
        if K == 1: 
            if N<W:
                return N/float(W) 
            return 1

        f = [0]*K + [1]*(N-K+1)+[0]*(W-N+K-1)
        pres = N-K+1
        for i in xrange(K-1,-1,-1):
            f[i] = float(pres)/W
            pres = pres-f[i+W]+f[i]
        print f
        return f[0]


s = Solution()
N, K, W = 1,1,2
#print s.new21Game(N,K,W)
#print s.new21Game1(N,K,W)
print s.new21Game_leetcode(N,K,W)
