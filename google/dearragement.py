# leetcode 634, use set theory, dp[n] = n * dp[n-1] + (-1)**n

class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur,MD,sign = 0,10**9+7,1
        for i in xrange(2,n+1):
            cur,sign = (i*cur+sign) % MD,-sign
        return cur
