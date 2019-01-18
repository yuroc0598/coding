#leetcode 294

class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def findInd(a): # return all possible starting ind of two consecutive ++
            ans = []
            for i in xrange(len(a)-1):
                if a[i]=='+' and a[i+1]=='+':
                    ans.append(i)
            return ans
        
        possible = findInd(s)
        if not possible: return False
        if len(possible) == 1: return True
        for i in possible:
            news = s[:i]+'--'+s[i+2:]
            if not self.canWin(news): return True
        return False
