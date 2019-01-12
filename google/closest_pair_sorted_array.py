# problem 1: find the closest pair in two sorted array

def closest_pair(nums1,nums2):
#use merge sort processes, when pointer switches, a possible answer appear
    p1=p2=0
    ans = float('inf')
    l1, l2 = len(nums1),len(nums2)
    if nums1[p1]<nums2[p2]:
        flag = 1
        pre = nums1[p1]
        p1 += 1
        
    else:
        flag = 2
        pre = nums2[p2]
        p2 += 1
    while p1<l1 and p2<l2:
        if nums1[p1] < nums2[p2]:
            if flag == 2:
                ans = min(ans,nums1[p1]-pre)
                print ans
                flag = 1

            pre = nums1[p1]
            p1 += 1
        elif nums1[p1]>nums2[p2]:
            if flag == 1:
                ans = min(ans,nums2[p2]-pre)
                print ans
                flag = 2

            pre = nums2[p2]
            p2 += 1
        else: return 0
    if p1 == l1: ans = min(ans,nums2[p2]-pre)
    if p2 == l2: ans = min(ans,nums1[p1]-pre)
    return ans
            


# problem 2:find the pair that sums closest to the target
def closest_sum(nums1,nums2,target):
    l1,l2 = len(nums1),len(nums2)
    i,j = 0,l2-1
    mindiff = float('inf')
    mini,minj = -1,-1
    while i<l1 and j>=0:
        curs = nums1[i]+nums2[j]
        if abs(curs-target) < mindiff:
            mindiff = abs(curs-target)
            mini,minj = i,j
        if curs > target:
            j -= 1
        elif nums1[i]+nums2[j] < target:
            i += 1
        else: return i,j
    return mini,minj,mindiff

# problem3 : find three closest elements from given three sorted arrays, such that max(abs(a-b),abs(a-c),abs(b-c)) is minimized
def closest_tuple(n1,n2,n3):
    ans = []
    mindiff = float('inf')
    i=j=k=0
    l1,l2,l3= len(n1),len(n2),len(n3)
    while i<l1 and j<l2 and k<l3:
        minv = min(n1[i],min(n2[j],n3[k]))
        maxv = max(n1[i],max(n2[j],n3[k]))
        curdiff = maxv - minv
        if curdiff == 0:
            return [i,j,k]
        if curdiff < mindiff:
            mindiff = curdiff
            ans = [i,j,k]
        if n1[i] == minv: i += 1
        if n2[j] == minv: j += 1
        if n3[k] == minv: k += 1
    return ans



nums1 = [20,24,100]
nums2 = [2,19,22,79,800]
nums3 = [10,12,23,24,119]
print closest_pair(nums1,nums2)
print closest_sum(nums1,nums2,20)
print closest_tuple(nums1,nums2,nums3)
