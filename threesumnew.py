#!/usr/bin/env python

from collections import defaultdict
class Solution(object):
    def threeSum(self,nums):
        dd,pos,neg,zero,ans = defaultdict(int),[],[],0,[]
        for ele in nums:
            if ele in dd:
                dd[ele] += 1
            else:
                dd[ele] = 1
                if ele>0:
                    pos.append(ele)
                elif ele<0:
                    neg.append(ele)
                else:
                    zero += 1
        if zero>2:
            ans.append([0,0,0])
        for p in pos:
            for n in neg:
                target = 0-p-n
                if target in dd:
                    if target in [p,n] and dd[target]>1:
                        ans.append([n,p,target])
                    elif target>p or 0>= target > n:
                        ans.append([n,p,target])
        return ans


def main():
    nums = [-1,0,1,2,-1,-4]
    s = Solution()
    print s.threeSum(nums)

if __name__=='__main__':
    main()
