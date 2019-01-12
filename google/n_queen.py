# determine if a given board is a valid n queen

def is_valid(board):
    N = len(board)
    queen = []
    for i in xrange(N):
        for j in xrange(N):
            if board[i][j] == 1:
              queen.append((i,j))  
    rowset = set()
    colset = set()
    diffset = set()
    sumset = set()
    for i,j in queen:
        rowset.add(i)
        colset.add(j)
        diffset.add(j-i)
        sumset.add(i+j)
    return len(rowset)==N and len(colset)==N and len(diffset)==N and len(sumset)==N


# leetcode 51, N queens problem, get all N queens permutation

class Solution(object):
    def solveNQueens(self, N):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.' for _ in xrange(N)] for _ in xrange(N)]
        #print board
        def attack_above(i,j):
            ans = set()
            # same column
            for k in xrange(i-1,-1,-1):
                ans.add((k,j))
            #left diag (i-1,j-1)
            for m,n in zip(range(i-1,-1,-1),range(j-1,-1,-1)):
                ans.add((m,n))
            # right diag (i-1,j+1)
            for m,n in zip(range(i-1,-1,-1),range(j+1,N)):
                ans.add((m,n))
            return ans
        self.ans = []
        def helper(target_row):
            if target_row == N: 
                self.ans.append(map(''.join,board))
            for col in xrange(N):
                if any(board[i][j]=='Q' for (i,j) in attack_above(target_row,col)): 
                    continue
                board[target_row][col] = 'Q'
                helper(target_row+1)
                board[target_row][col] = '.'
        helper(0)
        return self.ans

