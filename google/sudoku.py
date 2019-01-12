#!/usr/bin/python3
class Solution:
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        def getGrid(i,j):
            I,J = i//3,j//3
            ans = []
            for m in range(3*I,3*I+3):
                for n in range(3*J,3*J+3):
                    ans.append(board[m][n])
            return ans
        def getEmpty():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        return row,col
            return -1,-1
        
        def helper():
            row,col = getEmpty()
            if row == -1:
                return True
            pool = []
            for possible in range(1,10):
                if str(possible) in board[row]:
                    continue
                if str(possible) in [board[i][col] for i in range(9)]:
                    continue
                if str(possible) in getGrid(row,col):
                    continue
                pool.append(possible)
            if not pool:
                return False
            #print("pool is {}".format(pool))
            for ele in pool:
                board[row][col] = str(ele)
                if not helper():
                    board[row][col] = '.'
                else:
                    return True
            
        helper()
        

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

s = Solution()
s.solveSudoku(board)
print(board)
