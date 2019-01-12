#!/usr/bin/python3

def bstring(ins):
    ans = []
    def helper(pre,s):
        if len(s)==1:
            if s == '?':
                ans.append(pre+'1')
                ans.append(pre+'0')
            else:
                ans.append(pre+s)
        else:
            if s[0]=='?':
                helper(pre+'1',s[1:])
                helper(pre+'0',s[1:])
            else:
                helper(pre+s[0],s[1:])
    helper('',ins)
    return ans

def bs2(ins):
    if not ins:
        return ''
    ans = [ins[0]] if ins[0]!='?' else ['1','0']
    for char in ins[1:]:
        L = len(ans)
        if char!='?':
            for x in range(L):
                ans[x] += char
        else:
            for x in range(L):
                ans.append(ans[x]+'0')
                ans[x] += '1'
    return ans



ins = '1??0?101'
print(bstring(ins))

print(bs2(ins))
