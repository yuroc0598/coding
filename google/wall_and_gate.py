#leetcode 286
# my bsf time limte exceeded

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if rooms and rooms[0]:
            
            dp = {}
            m,n = len(rooms),len(rooms[0])
            def helper(i,j,visited):
            
                if (i,j) in visited: return
                if rooms[i][j] == 0:
                    dp[(i,j)] = 0
                    return
                if rooms[i][j] == -1:
                    dp[(i,j)] = 2**31-1
                    return
                visited.add((i,j))
                dp[(i,j)] = 2**31-1
                for newi,newj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                    if newi<0 or newj<0 or newi>= m or newj>=n:
                        continue
                    helper(newi,newj,visited)
                    dp[(i,j)] = min(dp[(i,j)],dp[(newi,newj)]+1)
            for i in xrange(m):
                for j in xrange(n):
                    if rooms[i][j] not in [-1,0]:
                        visited = set()
                        helper(i,j,visited)
                        rooms[i][j] = dp[(i,j)]


# start from all the gates, find the nearby rooms by bfs
from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if rooms and rooms[0]:
            Q = deque()
            m,n = len(rooms),len(rooms[0])
            for i in xrange(m):
                for j in xrange(n):
                    if rooms[i][j] == 0:
                        Q.append([i,j])
            while Q:
                curi,curj = Q.popleft()
                for newi,newj in [[curi+1,curj],[curi-1,curj],[curi,curj+1],[curi,curj-1]]:
                    if newi<0 or newj<0 or newi>=m or newj>=n or rooms[newi][newj]!=2**31-1:
                        continue
                    rooms[newi][newj] = rooms[curi][curj]+1
                    Q.append([newi,newj])
        
