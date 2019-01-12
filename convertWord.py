#!/usr/bin/env python


def ezconvert(s):
    if not s:
        return ''
    lst = s.split(' ')
    lst.reverse()
    print ' '.join(lst)


def convert(s):
    if not s:
        return ''
    re = ''
    curWord = ''
    for i in range(len(s)):
        if i == len(s)-1:
            curWord += s[i]
            re = curWord+' '+re
        elif s[i] == ' ':
            re = curWord+' '+re
            curWord = ''
        else:
            curWord = curWord + s[i]
    print re[:-1]


def convertInt(num):
    if num == 0:
        return '0'
    ans = ''
    neg = False
    if num <0:
        num = -num
        neg = True
    while num:
        ans = str(num%10) + ans
        num = num/10
    if neg:
        ans = '-' +ans
    print ans
    return ans
    



def main():
    s='sky is blue'
    ezconvert(s)
    convert(s)
    convertInt(123)
    convertInt(-123)


if __name__ == '__main__':
    main()
