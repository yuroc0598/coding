#!/usr/bin/env python

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        L1,L2 = len(nums1),len(nums2)
        if L1 > L2:
            L1, L2 = L2, L1
            nums1, nums2 = nums2, nums1
        low,high = 0,L1
	while low < high:
		left1 = (low + high) / 2
		right1 = left1 + 1
		left2 = (L1+L2)/2 - left1 - 2
		right2 = left2 + 1
		left_max = max(nums1[left1],nums2[left2])
		right_min = min(nums1[right1],nums2[right2])
	if left_max > right_min:
		high = left1
	elif left_max < right_min:
		
		
	
        
