# KMP is used to find the occurence of pattern in string org


# first build the longest proper prefix suffix table

def longest_prefix(s):
    ls = len(s)
    table = [0]*ls
    for i in xrange(1,ls):
        tmpl = table[i-1]
        while tmpl > 0 and s[i]!=s[tmpl]:
            tmpl = table[tmpl-1]
        if s[i] == s[tmpl]:
            tmpl += 1
        table[i]  = tmpl
    return table

def KMP(org,pat):
    table = longest_prefix(pat)
    print table
    i,j,lorg,lpat,ans = 0,0,len(org),len(pat),[]
    while i<lorg:
        if org[i]==pat[j]:
            i += 1
            j += 1
        if j == lpat:
            ans.append(i-lpat)
            j = table[j-1]
        elif i<lorg and org[i]!=pat[j]:
            if j != 0: j = table[j-1]
            else: i += 1
    return ans

org = 'abababccbab'
pat = 'ab'
org="mississippi"
pat= "issip"
print KMP(org,pat)

        
