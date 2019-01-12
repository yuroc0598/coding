class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        if target == 0:
            return [[]]
        candidates.sort()
        L, ans = len(candidates),[]
        for i in xrange(L):
            if target - candidates[i] >= candidates[0]:
                tmp = self.combinationSum(candidates[i:],target-candidates[i])
                for item in tmp:
                    print "enter"
                    ans.append(item.append(candidates[i]))
                
        return ans

s= Solution()
cand = [2,3,5]
t = 8
print s.combinationSum(cand,8)
