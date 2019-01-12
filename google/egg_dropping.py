#!/usr/bin/python

class Solution(object):
    def superEggDrop(self, K, N):
        def f(x):
            ans = 0
            r = 1
            for i in range(1, K+1):
                r *= x-i+1
                r //= i
                ans += r
                if ans >= N: break
            return ans

        lo, hi = 1, N
        while lo < hi:
            mi = (lo + hi) // 2
            if f(mi) < N:
                lo = mi + 1
            else:
                hi = mi
        return lo
        
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        #O(k*drops) --> see drops variable in function below
        #f(d, e) = highest floor that an egg can be dropped from without breaking for a certain number of drops (d) and a certain number of eggs (e).
        #We also know the result for the same number of drops and one fewer egg = f(d, e - 1) --> see example 1 given in ques to verify this.
        #Now we take an additional drop from floor "f(d, e - 1) + 1."
        #If it breaks, we know that we can find the result with one less egg f(d, e - 1).
        #If it doesn't break, we can explore the f(d, e) floors above the one we just dropped from. So we can get the result for a building with floors of height 1 + f(d, e - 1) + f(d, e).
        drops = 0      # the number of eggs dropped
        floors = [0 for i in range(K + 1)]  # floors[i] = no. of floors that can be checked with i eggs

        while floors[K] < N:                # until we can reach N floors with K eggs 
            for eggs in range(K, 0, -1):
                floors[eggs] += 1 + floors[eggs - 1]
                
            drops += 1

        return drops
        
