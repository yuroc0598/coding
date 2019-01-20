
#problem 1
# find the longest substring that consists of K unique char 15:45
from collections import defaultdict
def longest_subk(s,k):
    counter = {}
    start,end = 0,0
    hit = 0
    ans = 0
    L = len(s)
    while end<L:
        char = s[end]
        if char in counter:
            counter[char] += 1
        
        else:
            counter[char] = 1
            hit += 1
            if hit == k+1:
                ans = max(ans,end-start)
                while start < end and counter[s[start]] > 1:
                    counter[s[start]] -= 1
                    start += 1
                if start<end:
                    counter[s[start]] -= 1
                    start += 1
                    hit -= 1
        end += 1
    return max(ans,end-start)


s='aaaaaaaab'
k = 2
print longest_subk(s,k)

           


# problem 2
# find the longest substring where each letter repeat at lease K times, LC 395, use recursive, you dont have to find all the bad char at the first iter, find one is enough

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(z, k) for z in s.split(c))
        return len(s)
