#!/usr/bin/python3

def isWord(word,mat): # determine if char in mat can form word
    L = len(word)
    row,col = len(mat),len(mat[0])
    def helper(step,seen,i,j):        
        if step==L:
            return True

        if i<0 or j<0 or i>=row or j>=row:
            return False
        if (i,j) in seen:
            return False
        if mat[i][j]!=word[step]:
            return False
        seen.add((i,j))
        if  helper(step+1,seen,i-1,j) or helper(step+1,seen,i+1,j) or  helper(step+1,seen,i,j+1) or helper(step+1,seen,i,j-1) or helper(step+1,seen,i-1,j-1) or helper(step+1,seen,i+1,j+1) or helper(step+1,seen,i-1,j+1) or helper(step+1,seen,i+1,j-1):
            return True
        seen.remove((i,j))
        return False
    seen = set()
    for i in range(row):
        for j in range(col):
            if helper(0,seen,i,j):
                return True
    return False


mat = [['G','I','Z'],['U','E','K'],['Q','S','E']]
word = 'YUROC'
print(isWord(word,mat))
