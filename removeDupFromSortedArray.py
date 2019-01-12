#!/usr/bin/env python

class Solution(object):
	def removeDuplicates(self,nums):
		L = len(nums)
		if not L:
			return L
		
		result = 0
		for i in range(1,L):
			if nums[i] != nums[i-1]:
				result += 1
				nums[result] = nums[i]	
		return result+1



if __name__ == '__main__':
	s = Solution()
	nums = [0,0,1,1,1,2,2,3,3,4]
	nums1 = [1,1]
	print s.removeDuplicates(nums)
	print nums
	
