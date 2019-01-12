#!/usr/bin/env python
class Solution(object):
	def exist(self,board,word):
		if not board:
			return not word
		if not word:
			return False
		lw,row,col = len(word),len(board),len(board[0])
		def dfs(i,j,target):
			if target >= lw:
				return True
			if i<0 or j<0 or i>row-1 or j>col-1 or not board[i][j] == word[target]:
				return False
			target += 1
			bk = board[i][j]
			board[i][j] = '#'
			re = dfs(i-1,j,target) or dfs(i+1,j,target) or dfs(i,j-1,target) or dfs(i,j+1,target)
			board[i][j] = bk
			return re
		for i in range(row):
			for j in range(col):
				if dfs(i,j,0):
					return True
		return False
def main():
	s = Solution()
	board=[
		["C","A","A"],
		["A","A","A"],
		["B","C","D"]
	]
	word = 'AAB'
	if s.exist(board,word):
		print 'found'
	else:
		print 'not found'
if __name__ == '__main__':
	main()
