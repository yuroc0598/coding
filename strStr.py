#!/usr/bin/env python

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int: return -1 if needle is not found, return 0 if needle is empty
        """
	
	if not needle:
		return 0
	
	L = len(haystack)
	l = len(needle)

	if L < l:
		return -1
	p1, p2 = 0,0 
	while p1 <= L-l:
		pp1 = p1
		while haystack[pp1] == needle[p2]:
			pp1 += 1
			p2 += 1
			if p2 == l:
				return pp1-l
		
		p2 = 0
		p1 += 1
	return -1
			

if __name__ == '__main__':
	s = Solution()
	haystack = 'mississippi'
	needle = 'issip'
	print s.strStr(haystack,needle)
	
