#leetcode 651, screen clipboard problem, four operations: A , ctrl A, ctrl C, crtl V

# solution 1
class Solution(object):
    def maxA(self, N):
        best = [0, 1]
        for k in xrange(2, N+1):
            best.append(max(best[x] * (k-x-1) for x in xrange(k-1)))
            best[-1] = max(best[-1], best[-2] + 1) #addition
        return best[N]


# solution 2: in solution 1, we dont have to try the cases when k is larger than 5

# solution 3:

class Solution(object):
    def maxA(self, N):
        best = [0, 1, 2, 3, 4, 5, 6, 9, 12,
                16, 20, 27, 36, 48, 64, 81]
        q = (N - 11) / 5 if N > 15 else 0
        return best[N - 5*q] * 4**q
