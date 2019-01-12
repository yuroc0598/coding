#!/usr/bin/env python
import time

class ListNode(object):
	def __init__(self,x):
		self.val=x
		self.next=None


class Solution(object):
	def threeSum(self, nums):
		nums.sort()
		L=len(nums)
		result=[]
		if L<3:
			return result
        	ptr1=0
		while ptr1<L-2:
			ptrl=ptr1+1
			ptrr=L-1	
			while ptrl<ptrr:
				ts=nums[ptrl]+nums[ptrr]+nums[ptr1]
				if ts<0:
					ptrl+=1
					while nums[ptrl]==nums[ptrl-1] and ptrl<ptrr:
						ptrl+=1
				elif ts>0:
                			ptrr-=1				    
					while nums[ptrr]==nums[ptrr+1] and ptrl<ptrr:
						ptrr-=1
						
				else:
					result.append([nums[ptr1],nums[ptrl],nums[ptrr]]) 
                    			ptrl+=1
					ptrr-=1
					while nums[ptrl]==nums[ptrl-1] and ptrl<ptrr:
						ptrl+=1
					while nums[ptrr]==nums[ptrr+1] and ptrl<ptrr:
						ptrr-=1
           
			ptr1+=1
			while nums[ptr1]==nums[ptr1-1] and ptr1<L-2:
		                ptr1+=1
		return result

	
if __name__=='__main__':
	s=Solution()
	'''
	test=[-2,2,3,1,0,1,6,-3,4,-3]
	test1=[-2,0,0,2,2]
	test2=[0,0,0]
	test3=[-4,-4,-4,-4,-2,-2,-2,-2,-2,0,0,0,0,0,0,2,2,2,2,2,2,2,3,3,3,3,3,33,3,-1,-1,-1,-1,-1,5,5,5,5,5,5,5,5,-5,-5,-5,-5,-5,6,6,6,6,6,6,6]
	s.threeSum(test3)
	'''


	l10=ListNode(-9)
	l11=ListNode(3)
	l20=ListNode(5)
	l21=ListNode(7)


	l10.next = l11
	l20.next = l21

        s.mergeTwoLists(l10,l20)
	print "merged list:"
	while l10:
		print l10.val
		l10 = l10.next
