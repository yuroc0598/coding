#leetcode 562 

from collections import defaultdict
class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        row,col = len(M),len(M[0])
        rowdict = defaultdict(list)
        coldict = defaultdict(list)
        diadict = defaultdict(list)
        antidict = defaultdict(list)
        
        def get_consect(nums):
            ans = 0
            curL = 1
            #print nums
            for i in xrange(len(nums)-1):
                if nums[i] + 1 == nums[i+1]:
                    curL += 1
                else:
                    ans = max(ans,curL)
                    curL = 1
            return max(ans,curL)
            
        def get_max(d):
            ans = 0
            for key in d:
                ans = max(ans,get_consect(d[key]))
            
            return ans
                
                
        for i in xrange(row):
            for j in xrange(col):
                if M[i][j] == 1:
                    rowdict[i].append(j)
                    bisect.insort(coldict[j],i)
                    bisect.insort(diadict[i-j],i)
                    bisect.insort(antidict[i+j],i)
        
        return max(get_max(rowdict),get_max(coldict),get_max(diadict),get_max(antidict))
