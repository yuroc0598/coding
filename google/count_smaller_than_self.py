def countSmaller_bit(nums): # binary indexed tree
    def getSum(bitree,i):
        i += 1
        ans = 0
        while i > 0:
            ans += bitree[i]
            i -= i & ~(i-1)
        return ans
    def update(n,bitree,i,add_val):
        #nums[i] += add_val
        i += 1
        while i < n+1:
            bitree[i] += add_val
            i += i & ~(i-1)
    
    
    ans = []
    L = len(nums)
    if L == 0:
        return []
    indd = {v:i for i,v in enumerate(sorted(set(nums)))}
    bitree = [0]*(L+1)
    for i in range(L-1,-1,-1):
        num = nums[i]
        ans.append(getSum(bitree,indd[num]-1))
        update(L,bitree,indd[num],1)
    
    return ans[::-1]


def countSmaller_merge(nums): # use merge sort
    if not nums:
        return []
    L = len(nums)
    if L<2:
        return [0]
    ans = [0]*L
    def mergeSort(enum):
        le = len(enum)
        if le<2:
            return enum
        mid = le/2
        left = mergeSort(enum[:mid])
        right = mergeSort(enum[mid:])
        pl,pr,p = 0,0,0
        while pl<mid and pr<le-mid:
            if left[pl][1]<=right[pr][1]:
                ans[left[pl][0]] += pr
                enum[p] = left[pl]
                pl += 1
            else:
                enum[p] = right[pr]
                pr += 1
            p += 1
        while pl < mid:
            ans[left[pl][0]] += le-mid
            enum[p] = left[pl]
            pl += 1
            p += 1
        while pr < le-mid:
            enum[p] = right[pr]
            pr += 1
            p += 1
        return enum

    mergeSort(map(list,enumerate(nums)))
    return ans



nums = [5,3,4,1,2,2]
print nums
print "bit method:"
print countSmaller_bit(nums)
print "merge sort method:"
print countSmaller_merge(nums)

