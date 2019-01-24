# leetcode 322
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0: return 0
        coins.sort(reverse = True)
        lc = len(coins)
        self.ans = float('inf')
        def helper(ind,target,cur_count):
            if ind == lc:
                if target == 0: 
                    self.ans = min(cur_count,self.ans)
                return
            if cur_count + target/(coins[ind]) > self.ans: 
                return
            if coins[ind]==target: 
                self.ans = min(self.ans,cur_count+1) 
            
            if coins[ind]<target:    
                helper(ind,target-coins[ind],cur_count+1)
            helper(ind+1,target,cur_count)
                
            
        helper(0,amount,0)
        return self.ans if self.ans!=float('inf') else -1


# LC 518, find the number of combinations that can form the target amount using given array
# this is an intuitive and non-optimized solution:

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        L = len(coins)
        dp = [[0 for _ in xrange(amount+1)] for _ in xrange(L+1)]
        dp[0][0] = 1
        #dp[coin_ind][money] = dp[coin_ind-1][money]+dp[coin_ind][money-coins[coin_ind]]
        for coin_ind in xrange(1,L+1):
            dp[coin_ind][0] = 1
            for money in xrange(1,amount+1):
                if money<coins[coin_ind-1]:
                    dp[coin_ind][money] = dp[coin_ind-1][money]
                else:
                    dp[coin_ind][money] = dp[coin_ind-1][money]+dp[coin_ind][money-coins[coin_ind-1]]
        return dp[L][amount]

# since dp[i][j] only depends on dp[i-1][j] and dp[i][j-x], we use one-dimensional dp
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        L = len(coins)
        dp = [1] + [0]*amount
        #dp[coin_ind][money] = dp[coin_ind-1][money]+dp[coin_ind][money-coins[coin_ind]]
        for coin_ind in xrange(0,L):
            for money in xrange(coins[coin_ind],amount+1):
                    dp[money] += dp[money-coins[coin_ind]]
        return dp[amount]
