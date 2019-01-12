def global_local_inversion(nums): # at each index i, compare the current max val from [0,i] with nums[i+2]
    if not nums:
        return True
    maxv = [0]
    for i in xrange(len(nums)-2):
        maxv = max(maxv,nums[i])
        if maxv > nums[i+2]:
            return False
    return True
