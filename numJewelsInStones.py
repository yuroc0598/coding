#!/usr/bin/env python

class Solution(object):
	def numJewelsInStones(self,J,S):
		re = 0
		for char in S:
			if char in J:
				re +=1
		return re

if __name__ == '__main__':
	s=Solution()
	J = 'aA'
	S = 'aAAbbbb'
	print s.numJewelsInStones(J,S)
