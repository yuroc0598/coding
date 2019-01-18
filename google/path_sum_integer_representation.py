# leetcode 666
class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        complete = {}
        for num in nums:
            complete[num/10] = num%10
        
        known = {} # known[i] = j, represents from node i back to root, the sum is j
        
        
        def helper(num_key): # reutrn known[num_key]
            
            if num_key not in known:
                
                curD,curP = num_key/10, num_key%10
                #print num_key
                curV = complete[num_key]
                if curD == 1:
                    known[num_key] = curV
                else:
                    parD,parP = curD-1,(curP+1)/2
                    par_key = 10*parD+parP
                    known[num_key] = curV + helper(par_key)
            
            return known[num_key]
            
        ans = 0
        while nums:
            cur = nums.pop()
            if cur/10 not in known:
                ans += helper(cur/10)
        return ans
            

class Solution(object):
    def pathSum(self, nums):
        self.ans = 0
        values = {x / 10: x % 10 for x in nums}
        def dfs(node, running_sum = 0):
            if node not in values: return
            running_sum += values[node]
            depth, pos = divmod(node, 10)
            left = (depth + 1) * 10 + 2 * pos - 1
            right = left + 1

            if left not in values and right not in values:
                self.ans += running_sum
            else:
                dfs(left, running_sum)
                dfs(right, running_sum)

        dfs(nums[0] / 10)
        return self.ans
