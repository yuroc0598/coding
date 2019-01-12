#!/usr/bin/env python


def partition(arr,low,high):
    pivot = arr[high]
    i = low -1
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j], arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quickSort(arr,low,high):
    if low < high:
        idx = partition(arr,low,high)
        quickSort(arr,low,idx-1)
        quickSort(arr,idx+1,high)


def main():
    arr = [3,2,4,1,4,6,0,9]
    print arr
    quickSort(arr,0,len(arr)-1)
    print arr

if __name__ == '__main__':
    main()
    
