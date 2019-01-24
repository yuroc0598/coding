#LC 486, given an array, player1 and player2 take turns to get the num from either end until the array is empty. The one with more point sum wins.
# the idea is to use recursion and dp, dp[(s,e)] means the max difference current player can get from interval [s,e] in nums

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = {}
        def helper(s,e):# return diff p1-p2
            if (s,e) not in memo:
                if s==e: memo[(s,e)] = nums[s]
                else:
                    tmp1 = nums[s] - helper(s+1,e)
                    tmp2 = nums[e] - helper(s,e-1)
                    memo[(s,e)] = max(tmp1,tmp2)
            return memo[(s,e)]
        return True if helper(0,len(nums)-1) >=0 else False
