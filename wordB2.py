#!/usr/bin/env python

class Solution(object):
    def wordBreak(self,s,wd):
        
        if not wd:
            return None
        
        def helper(s):
            if s=='': return ['']
            ans = []
            for word in wd:
                if not s.startswith(word):
                    continue
                wordL = len(word)
                if len(s) >=  wordL:
                    childV = helper(s[wordL:])
                    if childV:
                        for item in childV:
                            if item=='':
                                item = word
                            else:
                                item = word+' '+item
                            ans.append(item)
            return ans
        return helper(s)


s = Solution()
ss='catsanddog'
wd=['cat','cats','and','sand','dog']
print s.wordBreak(ss,wd)
