def minimum_page(nums,st):
    sumlst = []
    cursum = 0 
    L = len(nums)
    for num in nums:
        cursum += num
        sumlst.append(cursum)
    def helper(i,no_st):
        if no_st == 1:
            return sumlst[L-1]-sumlst[i]+nums[i]

        ans = float('inf')
        for k in xrange(i,L-no_st+1):
            cur = sumlst[k]-sumlst[i]+nums[i]
            rest = helper(k+1,no_st-1)    
            ans = min(ans,max(cur,rest))
        return ans
    return helper(0,st)


def from_geeks(nums,st):
    L = len(nums)
    def is_possible(num):
        st_rq = 1
        cursum = 0
        for k in nums:
            if k>num:
                return False
            else:
                if cursum + k > num:
                    st_rq += 1
                    cursum = k
                    if st_rq > st:
                        return False
                else:
                    cursum += k
        return True

    lo, hi = 0, sum(nums)
    ans = float('inf')
    while lo<=hi:
        mid = (lo+hi)/2
        if is_possible(mid):
            ans = min(ans,mid)
            hi = mid - 1
        else:
            lo = mid + 1
    return ans

nums = [12,13,14,20,34,40,50,67,90,100]
st = 5
print 'mine:'
print minimum_page(nums,st)
print 'geeks:'
print from_geeks(nums,st)
