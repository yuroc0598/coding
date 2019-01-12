#!/usr/bin/python


def countRangeSum_mergesort(nums, lower, upper):
        def mergesort(start,end):
            if end<=start:
                return 0
            mid = start + (end-start)/2
            c = mergesort(start,mid) + mergesort(mid+1,end)
            rind1 = mid+1
            rind2 = mid+1
            for i in range(start,mid+1):
                while rind1 <= end and sums[rind1]-sums[i]<lower: rind1 += 1
                while rind2 <= end and sums[rind2]-sums[i]<=upper: rind2 += 1
                c += rind2-rind1
            sums[start:end+1] = sorted(sums[start:end+1])
            return c
        sums = [0]
        for num in nums:
            sums.append(sums[-1]+num)
        
        return mergesort(0,len(nums))

'''
def countRangeSum_bit(nums,lower,upper):
    def getSum(bitree,i):
        i += 1
        ans = 0
        while i>0:
            ans += bitree[i]
            i -= i & (-i)
        return ans
    def update(bitree,i,L,add_val):
        i += 1
        while i < L+1:
            bitree[i] += add_val
            i += i & (-i)


    sums = [0]
    ans = 0
    L = len(nums)
    for num in nums:
        sums.append(sums[-1]+num)
    #sums is now a list with length L+1
    bitree = [0]*(L+2)
    # sums[j] - sums[i] in [low,up] => for each sums[j], sums[i] in [sums[j]-up, sums[j]-low]
    d = {v:i for i,v in enumerate(sorted(set(sums)))}
    for num in sums:
        ans += getSum(bitree,d[num-lower]) - getSum(bitree,d[num-upper])
        update(bitree,d[num],L,1)
    return ans

'''
nums = [-2,5,-1]
lower, upper = -2,2
#print countRangeSum(nums,lower,upper)
print countRangeSum_mergesort(nums,lower,upper)
