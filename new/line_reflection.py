# leetcode 356
from collections import defaultdict
class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points: return True
        def getCenter(ss):
            nums = sorted(set(ss))
            
            if len(nums)==1: return nums[0]
            lo,hi = 0,len(nums)-1
            s = nums[lo]+nums[hi]
            while lo<=hi and nums[lo]+nums[hi] == s:
                lo += 1
                hi -= 1
            if nums[lo]+nums[hi]==s: return float(s)/2
            return float('inf')
        
        dd = defaultdict(list)
        
        for x, y in points:
            dd[y].append(x)
        sample_y, sample_x = dd.popitem()
        center = getCenter(sample_x)
        if center == float('inf'): 
            #print '1'
            return False
        for xlist in dd.values():
            xset = set(xlist)
            
            while xset:
                cur = xset.pop()
                #print center,cur, xset
                if cur!=center:
                    if center*2 - cur not in xset: 
                        #print '3'
                        return False
                    else:
                        xset.remove(center*2 - cur)
        return True
            
