#!/usr/bin/env python
class Solution(object):
	def __init__(self,grid):
	#put a ring of water
		self.row = len(grid)+2
		self.col = len(grid[0])+2
		self.grid = [[0 for i in range(self.col)] for j in range(self.row)]
	
		for i in range(1,self.row-1):
			for j in range(1,self.col-1):
				self.grid[i][j] = grid[i-1][j-1]
		self.direction = 0 # 0,1,2,3 for east, south, west, north
		self.next_step = [0,0]	
		self.next_left = [0,0]
		self.next_right = [0,0]
	def walk(self,current): #bug is between (i,j) and the island center
		i, j = current[0],current[1]
		if self.direction == 0:
			self.next_left = [i,j+1]
			self.next_right = [i+1,j+1]
		elif self.direction == 1:
			self.next_left = [i+1,j]
			self.next_right = [i+1,j-1]
		elif self.direction == 2:
			self.next_left = [i,j-1]
			self.next_right = [i-1,j-1]
		else:
			self.next_left = [i-1,j]
			self.next_right = [i-1,j+1]
		left_value = self.grid[self.next_left[0]][self.next_left[1]] 
		right_value = self.grid[self.next_right[0]][self.next_right[1]]
		if left_value == 1 and right_value == 1:
			# turn left
			self.direction += 3
			self.direction %= 4
			return [i,j]

		elif left_value == 0 and right_value == 1:
			# continue
			return self.next_left
		else:
			# turn right
			self.direction += 1
			self.direction %= 4
			return self.next_right


	def numIslands(self):
	# walk, always keep water in the left and land in the right, until return to the origin
		origin = [0,1]
		current = self.walk(origin)
		while current!= origin:
			print "{},{}".format(current,self.direction)
			current = self.walk(current)
def main():
	mygrid = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
	mygrid1 = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
	s = Solution(mygrid)
	s.numIslands()

if __name__ == '__main__':
	main()
