#!/usr/bin/env python

import sys
class Solution(object):
	def countAndSay(self,n):
		if n == 1:
			return '1'
		last_str = self.countAndSay(n-1)
		L = len(last_str)
		result = ''
		occ = 0
		val = last_str[0]
		for i in range(0,L):
			if last_str[i] == val:
				occ += 1
			else:
				result = result + str(occ) + val
				val = last_str[i]
				occ = 1
			if i == L-1:
				result = result + str(occ) + val

		return result

	def countAndSay1(self,n):
		if n == 1:
			return '1'
		last_str = self.countAndSay(n-1)
		L = len(last_str)
		val = last_str[0]
		result = '1' + val
		for i in range(1,L):
			if last_str[i] == val:
				result = result[:-2] + str(int(result[-2])+1) + val
			else:
				result = result + '1' + last_str[i]
				val = last_str[i]

		return result


if __name__ == '__main__':
	s = Solution()
	n = sys.argv[1]
	print	s.countAndSay1(int(n))
