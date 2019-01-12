#!/usr/bin/python3

def heapify(arr,bound,root):
    
    mx = root
    lc = root*2+1
    rc = root*2+2
    if lc<=bound and arr[lc]>arr[mx]:
        mx = lc

    if rc<=bound and arr[rc]>arr[mx]:
        mx = rc
    if mx!=root:
        arr[root],arr[mx] = arr[mx],arr[root]
        heapify(arr,bound,mx)



def heapsort(arr):
    size = len(arr)
    start = (size-2)//2
    for i in range(start,-1,-1):
        heapify(arr,size-1,i)
    print("init max heap {}".format(arr))
    for i in range(size-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        print("swap {} and {}".format(arr[0],arr[i]))
        heapify(arr,i-1,0)
        print(arr)



arr = [12,11,13,5,6,7]
print(arr)
heapsort(arr)
print(arr)    
