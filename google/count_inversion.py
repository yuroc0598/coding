def count_inversion(nums): # use merge sort
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


def count_inversion_bit(nums):
    def getSum(bitree,i):
        i += 1
        ans = 0
        while i>0:
            ans += bitree[i]
            i -= i & (-i)
        return ans

    def update(bitree,L,i,add_val):
        i += 1
        while i < L+1:
            bitree[i] += add_val
            i += i & (-i)

    def convert_nums(nums):
        tmp = sorted(map(list,enumerate(nums)),key =lambda x:x[1])
        for i in range(len(tmp)):
            tmp[i][1] = i
        return map(lambda x: x[1],sorted(tmp))

    L = len(nums)
    bitree = [0]*(L+1)
    nums = convert_nums(nums)
    ans = 0
    for num in nums[::-1]:
        ans += getSum(bitree,num)
        update(bitree,L,num,1)
    return ans

nums = [3,4,1,5,7,2]
print "merge method count inversion: %d" % count_inversion(nums)
nums = [3,4,1,5,7,2]
print "binary indexed tree  method count inversion: %d" % count_inversion_bit(nums)
