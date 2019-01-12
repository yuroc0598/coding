#!/usr/bin/env python

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        cur = [['(',1,0]]
        
        for i in range(2*n-1):
            for j in range(len(cur)):
                if cur[j][1]==cur[j][2]:
                    if not cur[j][1]==n:
                        cur[j][0] += '('
                        cur[j][1] +=1
                elif cur[j][1]>cur[j][2]:
                    if not cur[j][1] == n:
                        cur.append(cur[j][:])
                        cur[j][0] += '('
                        cur[j][1] += 1
                        cur[-1][0] += ')'
                        cur[-1][2] += 1
                    else:
                        cur[j][0] += ')'
                        cur[j][2] += 1
                    
            print cur
        
        return [i[0] for i in cur ]


def main():
    s = Solution()
    print s.generateParenthesis(3)

if __name__ == '__main__':
    main()
