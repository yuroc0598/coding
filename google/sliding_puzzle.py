# leetcode 773, use BFS
from collections import deque
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        
        Q = deque()
        initB,initI = [],0
        desired = [1,2,3,4,5,0]
        nex = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4],4:[1,3,5],5:[2,4]}
        for i in xrange(2):
            for j in xrange(3):
                initB.append(board[i][j])
                if board[i][j] == 0:
                    initI = 3*i+j
        
        Q.append([initB,initI,0])
        seen = set()
        ans = float('inf')
        while Q:
            #print Q
            curB,curI,curM = Q.popleft()
            seen.add(tuple(curB))
            if curB == desired: 
                return curM
            else:
                for newi in nex[curI]:
                    if newi<0 or newi>5: continue
                    newB = curB[:]
                    newB[curI],newB[newi] = newB[newi],newB[curI]
                    if tuple(newB) in seen: continue
                    #print newB
                    Q.append([newB,newi,curM+1])
        return -1
