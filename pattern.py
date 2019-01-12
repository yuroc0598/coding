import string
class Solution(object):
    def canBeZero(self,s):
        dt = string.ascii_lowercase+'.'
        if not s:
            return True
        if s[-1] in dt:
            return False
        for i in range(len(s)-1):
            if s[i] in dt and s[i+1] in dt:
                return False
        return True    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dt = string.ascii_lowercase
        preEqual = 0
        i,j=0,0
        while i<len(p) and j<len(s):
            if p[i] in dt:
                if p[i]!=s[j]:
                    if i+1>= len(p):
                        return False
                    else:
                        if not p[i+1]=='*':
                            return False
                        else:
                            preEqual = 1
                            i+=2
                else:
                    preEqual = 1
                    i+=1
                    j+=1
            elif p[i]=='.':
                preEqual = 1
                i+=1
                j+=1
            else:
                if preEqual:
                    while j <len(s) and s[j]==s[j-1]:
                        j+=1
                    while i+1<len(p) and (p[i+1]==p[i-1] or p[i+1]=='*'):
                        i+=1
                    if j == len(s) and i == len(p)-1:
                        return True
                    if j == len(s) and not i==len(p)-1:
                        if self.canBeZero(p[i:]):
                            return True
                        else:
                            return False
                    if (not j == len(s)) and i==len(p)-1:
                        if self.canBeZero(s[j:]):
                            return True
                        else:
                            return False
                    # TODO:
                    
                else:
                    # '*' is zero
                    preEqual = 1
                    i +=1
                
        if i == len(p) and j == len(s):
            return True
        if i== len(p):
            if self.canBeZero(s[j:]):
                return True
        if j == len(s):
            if self.canBeZero(p[i:]):
                return True
        return Falseeturn False
