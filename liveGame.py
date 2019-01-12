#!/usr/bin/env python
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row,col = len(board),len(board[0])
                
        def getVal(i,j):
            if 0<= i <= row-1 and 0<=j<= col-1:
                return board[i][j]
            else:
                return 0
        def countVal(i,j) :
            c = 0
            c += getVal(i-1,j-1)
            c += getVal(i-1,j)
            c += getVal(i-1,j+1)
            c += getVal(i,j-1)
            c += getVal(i,j+1)
            c += getVal(i+1,j+1)
            c += getVal(i+1,j)
            c += getVal(i+1,j-1)
            return c
        newB = [[-1 for i in range(col)] for j in range(row)]
        for i in range(row):
            for j in range(col):
                liveNo = countVal(i,j)
                if liveNo<2:
                    newB[i][j]=0
                elif 3<liveNo:
                    newB[i][j]=0
                elif liveNo == 3:
                    newB[i][j] = 1
        print "newB is :{}".format(newB)
        for i in range(row):
            for j in range(col):
                if newB[i][j]==0:
                    board[i][j] =0
                if newB[i][j]==1:
                    board[i][j] =1

def main():
    s = Solution()
    board=[
            [0,1,0],
            [0,0,1],
            [1,1,1],
            [0,0,0]
          ]
    print board
    s.gameOfLife(board)
    print board


if __name__ == '__main__':
    main()
