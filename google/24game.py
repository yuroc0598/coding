# leetcode 679, only four numbers in the array, and numbers must be and can only be used once

from operator import truediv, mul, add, sub

class Solution(object):
    def judgePoint24(self, A):
        if not A: return False
        if len(A) == 1: return abs(A[0] - 24) < 1e-6

        for i in xrange(len(A)):
            for j in xrange(len(A)):
                if i != j:
                    B = [A[k] for k in xrange(len(A)) if i != k != j]
                    for op in (truediv, mul, add, sub):
                        if (op is add or op is mul) and j > i: continue
                        if op is not truediv or A[j]:
                            B.append(op(A[i], A[j]))
                            if self.judgePoint24(B): return True
                            B.pop()
        return False


# what if there are more than 4 numbers and only select part of them, and they can be concatenated?
