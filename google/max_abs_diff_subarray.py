# given an array, find two consecutive sub arrays that have the max abs diff

def max_diff_subarray(nums):
    L = len(nums)
    pre_sum_max = [nums[0]]
    pre_sum_min = [nums[0]]
    for i in xrange(1,L):
        if pre_sum_max[-1] < 0:
            pre_sum_max.append(nums[i])
        else:
            pre_sum_max.append(pre_sum_max[-1]+nums[i])
        if pre_sum_min[-1]<0:
            pre_sum_min.append(nums[i]+pre_sum_min[-1])
        else:
            pre_sum_min.append(nums[i])
    return pre_sum_max,pre_sum_min


nums = [-2, -3, 4, -1, -2, 1, 5, -3]
pre_sum_max, pre_sum_min = max_diff_subarray(nums)    

suf_sum_max,suf_sum_min = max_diff_subarray(nums[::-1])[0][::-1]  ,max_diff_subarray(nums[::-1])[1][::-1]  

#print pre_sum_max,pre_sum_min,suf_sum_max,suf_sum_min
ans = float('-inf')
for i in xrange(len(nums)-1):
    ans = max(abs(pre_sum_max[i]-suf_sum_max[i+1]),abs(pre_sum_min[i]-suf_sum_min[i+1]))
print ans
