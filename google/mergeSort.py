#!/usr/bin/python

def mergeSort(nums):
    L = len(nums)
    if L<2:
        return 
    mid = L/2
    left = nums[:mid]       
    mergeSort(left)
    right = nums[mid:]
    mergeSort(right)
    p1,p2,p = 0,0,0
    while p1<mid and p2<L-mid:
        if left[p1]<right[p2]:
            nums[p]=left[p1]
            p1 += 1
        
        else:
            nums[p]=right[p2]
            p2 += 1
        p += 1

    while p1<mid:
        nums[p] = left[p1]
        p1 += 1
        p += 1
    while p2<L-mid:
        nums[p] = right[p2]
        p2 += 1
        p += 1


def count_inversion(nums):
    L = len(nums)
    if L<2:
        return 0
    mid = L/2
    left = nums[:mid]       
    right = nums[mid:]
    c = count_inversion(left)
    c += count_inversion(right)
    p1,p2,p = 0,0,0
    while p1<mid and p2<L-mid:
        if left[p1]<=right[p2]:
            c += p2
            nums[p]=left[p1]
            p1 += 1
        
        else:
            nums[p]=right[p2]
            p2 += 1
        p += 1

    while p1<mid:
        c += L-mid
        nums[p] = left[p1]
        p1 += 1
        p += 1
    while p2<L-mid:
        nums[p] = right[p2]
        p2 += 1
        p += 1
    return c
nums = [5,6,1,2,3,7]
print nums
print "inversion : %d" % count_inversion(nums)
mergeSort(nums)
print nums
