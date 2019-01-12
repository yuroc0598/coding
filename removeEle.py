#!/usr/bin/env python

class Solution(object):
	def removeElement(self,nums,val):
		L = len(nums)
		if L < 1:
			return L
		result = 0
		for i in range(0,L):
			if nums[i] != val:
				nums[result] = nums[i]
				result += 1
		return result

if __name__ == '__main__':
	s = Solution()
	nums = [2]
	val = 1
	print s.removeElement(nums,val)
	print nums
			
