#!/usr/bin/env python

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 0
        while A[i+1] > A[i]:
            print i
            i += 1
        return i

if __name__ == "__main__":
	s = Solution()
	nums = [0,1,0]
	print s.peakIndexInMountainArray(nums)
