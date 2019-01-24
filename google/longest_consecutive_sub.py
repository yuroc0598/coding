#LC 128, idea is, for each num, check if num+1 is in set(nums), if not, start from num, check if num-1 is in set(nums),

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        nums = set(nums)
        ans = 0
        for num in nums:
            if num+1 not in nums:
                curL = 1
                while num-1 in nums:
                    num -= 1
                    curL += 1
                ans = max(ans,curL)
        return ans
