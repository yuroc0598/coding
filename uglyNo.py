#!/usr/bin/env python
import sys
import time

class Solution(object):
	def __init__(self):
		self.dp = [1]
		self.L = 1
	def isUgly(self,m):
		if m <=0:
			return 0
		if m == 1:
			return 1
		while m % 2 == 0:
			m = m/2
		while m % 3 ==0:
			m = m/3
		while m % 5 == 0:
			m = m/5
		if m == 1:
			return 1
		return 0
	def nextNo(self,n):
		while True:
			n += 1
			if self.isUgly(n):
				return n
			
	def uglyNo(self,N):
		if self.L >= N:
			return self.dp[N-1]
		for i in range(self.L,N):
			self.dp.append(self.nextNo(self.dp[-1]))
			self.L += 1
		return self.dp[-1]
	def getNthUglyNo(self,n): 
		ugly = [0] * n # To store ugly numbers 
		ugly[0] = 1
		i2 = i3 =i5 = 0
		next_multiple_of_2 = 2
		next_multiple_of_3 = 3
		next_multiple_of_5 = 5
		for l in range(1, n): 
			ugly[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5) 
			if ugly[l] == next_multiple_of_2: 
				i2 += 1
				next_multiple_of_2 = ugly[i2] * 2
			if ugly[l] == next_multiple_of_3: 
				i3 += 1
				next_multiple_of_3 = ugly[i3] * 3
			if ugly[l] == next_multiple_of_5:  
				i5 += 1
				next_multiple_of_5 = ugly[i5] * 5
		return ugly[-1]
def main():
	s = Solution()	
	N = sys.argv[1]
	s1=time.time()
	s.uglyNo(int(N))
	s2=time.time()
	s.getNthUglyNo(int(N))
	s3=time.time()
	print s2-s1
	print s3-s2

if __name__ == '__main__':
	main()
