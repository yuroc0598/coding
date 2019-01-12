#!/usr/bin/env python
import sys
def binSearch(arr,target):
    low,high = 0,len(arr)
    while low<high:
        mid = (low+high)/2
        if arr[mid] == target:
            print "found, the original index is %d" % mid
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid 
    print "not found and the insertion point is %d" % low
    return low 

def main():
    
    arr = [1,1,3,3,15]
    print arr
    target = int(sys.argv[1])
    binSearch(arr,target)

if __name__ == '__main__':
    main()
    
