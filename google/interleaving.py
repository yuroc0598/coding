'''
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1,l2,l3 = len(s1),len(s2),len(s3)
        if l1+l2!=l3:
            return False
        if l1==0:
            return s2==s3
        if l2==0:
            return s1==s3
                    
        def helper(curInd1,curInd3,remain):
            if curInd1 == l1:
                if remain!=s2:
                    return False
                return True    
            if curInd3==l3:
                return False
            p2 = helper(curInd1,curInd3+1,remain)
            if s1[curInd1]!=s3[curInd3]:
                return p2
            else: 
                breakp = len(remain)- (l3-curInd3-1) -1
                after = remain[breakp+1:]
                before = remain[:breakp]
                new_remain = before+after
                #print "curInd1 is {}, curInd3 taken: {} and new pre is {} and new remain is {},before is {} and after is {}".format(curInd1,curInd3,pre1+s1[curInd1],new_remain,before,after)
                p1 = helper(curInd1+1,curInd3+1,new_remain)
                return p1 or p2
        
        
        
        return helper(0,0,s3)
'''


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1,l2,l3 = len(s1),len(s2),len(s3)
        if l1+l2!=l3:
            return False
        if l1==0:
            return s2==s3
        if l2==0:
            return s1==s3
        
        dp = {}
        def helper(p1,p2): # p3 = p1+p2?
            if (p1,p2) not in dp:
                if p1==l1:
                    if p2 == l2:
                        dp[(p1,p2)] = True
                    else:
                        dp[(p1,p2)] = s2[p2:]==s3[p1+p2:]
                if p2==l2:
                    if p1 == l1:
                        dp[(p1,p2)] = True
                    else:
                        dp[(p1,p2)] = s1[p1:]==s3[p1+p2:]
                else:    
                    r1,r2=False,False
                    if p1<l1 and s1[p1] == s3[p1+p2]:
                        r1 = helper(p1+1,p2)
                    if p2<l2 and s2[p2] == s3[p1+p2]:
                        r2 = helper(p1,p2+1)
                    dp[(p1,p2)] = r1 or r2
            return dp[(p1,p2)]
        return helper(0,0)
