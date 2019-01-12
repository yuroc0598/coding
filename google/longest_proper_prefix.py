
import sys
def longest_pre(s):
    # find the longest proper prefix and suffix that are equal to each other
    ls =len(s)
    table = [0]*ls
    for i in xrange(1,ls):
        tmpL = table[i-1]
        while tmpL > 0 and s[i]!=s[tmpL]:
            tmpL = table[tmpL]
        if s[i] == s[tmpL]:
            tmpL += 1
        table[i] = tmpL
    return table[-1]


s = sys.argv[1]
print longest_pre(s)
