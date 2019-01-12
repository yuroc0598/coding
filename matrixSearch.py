#!/usr/bin/env python
import time
import sys
class Solution(object):
    def binSearch(self,arr,target):
            low,high = 0,len(arr)-1
            while low<=high:
                mid = (low+high)/2
                if arr[mid] == target:
                    return [1,mid]
                if arr[mid] > target:
                    high = mid - 1
                else:
                    low = low + 1
            return [0,low]
    def searchMatrix(self, matrix, target): 
        if not matrix or not matrix[0]:
            return False
        if matrix[0][0]>target or matrix[-1][-1]<target:
            return False
        row,col = len(matrix),len(matrix[0])
        i = self.binSearch(matrix[0],target)
        j = self.binSearch([matrix[k][0] for k in range(row)],target)    
        if i[0]==1 or j[0]==1:
            return True
        newMatrix = [matrix[m][1:i[1]] for m in range(1,j[1])]
        return self.searchMatrix(newMatrix,target)

class Solution1(object):
    def binSearch(self,arr,target):
            low,high = 0,len(arr)-1
            while low<=high:
                mid = (low+high)/2
                if arr[mid] == target:
                    return mid
                if arr[mid] > target:
                    high = mid - 1
                else:
                    low = low + 1
            return -1
    def searchMatrix(self, matrix, target): 
        if not matrix or not matrix[0]:
            return False
        if matrix[0][0]>target or matrix[-1][-1]<target:
            return False
        row,col = len(matrix),len(matrix[0])
        for i in range(min(row,col)):
            if matrix[i][i]>=target:
                break
        if matrix[i][i] == target:
                return True
        # now matrix[i][i] > target
        
        while i< min(row,col):
            if matrix[i][0] <= target:
                if not self.binSearch(matrix[i][0:i],target)==-1:
                    return True
            if matrix[0][i] <= target:
                if not self.binSearch([matrix[j][i] for j in range(i)],target) == -1:
                    return True
            i += 1
        if i<min(row,col): return False
        if row<col:
            return self.searchMatrix([matrix[j][i:col] for j in range(row)],target)
        return self.searchMatrix(matrix[i:],target)

def main():
    s = Solution()
    s1 = Solution1()
    t = int(sys.argv[1])
    mat = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    time1 = time.time()
    s.searchMatrix(mat,t)
    time2 = time.time()
    s1.searchMatrix(mat,t)
    time3 = time.time()
    print time2-time1
    print time3-time2
if __name__ == '__main__':
    main()
