class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
	if not nums:
		return 0
    L = len(nums)
    left,right = 0,L-1
    while left <=right:
	mid = (left + right) / 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return mid
