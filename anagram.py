import string
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ls,lp,ans = len(s),len(p),[]
        if ls < lp:
            return []
        
        baseline = {char:0 for char in string.ascii_lowercase}
        window = {char:0 for char in string.ascii_lowercase}
        for char in p:
            baseline[char] += 1
        for char in s[0:lp]:
            window[char] += 1
        print baseline
        if window == baseline:
            ans.append(0)
        for j in range(1,ls-lp+1):
            window[s[j-1]] -= 1
            window[s[j+lp-1]] += 1
            #print window
            if window == baseline:
                ans.append(j)
        return ans


sl = Solution()
s = 'cbaebabacd'
p='abc'
print sl.findAnagrams(s,p)
