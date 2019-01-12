#leetcode 55, given a list of nums represents the max jumps it can provide, check if we can arrive at the last num
class Solution(object):
    def canJump1(self,nums): # use dp, bottom up
        if not nums:
            return True
        L = len(nums)
        dp = [1]+[0]*(L-1)
        for i in xrange(1,L):
            for j in xrange(i-1,-1,-1):
                if dp[j]==1 and nums[j]+j >= i:
                    dp[i]=1
                    break
        return dp[L-1]==1


    def canJump(self, nums): # use greedy, start from the end, if we found a position that can jump to the last ind, then we make this position the last ind, 
        """
        :type nums: List[int]
        :rtype: bool
        """
        L = len(nums)
        lastind = L-1
        for i in xrange(L-1,-1,-1):
            if nums[i] + i >= lastind:
                lastind = i
        return lastind == 0
