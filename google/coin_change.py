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
