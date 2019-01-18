#leetcode 163, given sorted int array nums, where the range of elements are in the inclusive range [lower,upper]

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
            ans = []
            nums = [lower-1] + nums + [upper+1]
            for i in xrange(1,nums):
                if nums[i] == nums[i-1]+2:
                    ans.append(str(nums[i-1]+1))
                elif nums[i] > nums[i-1]+2:
                    ans.append(str(nums[i-1]+1)+'->'+str(nums[i]-1))
            return ans

