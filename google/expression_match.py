# pattern only contain '*' and regular string, dict contains only words

def match(pat,word):
    i,j = 0,0
    lp,lw = len(pat),len(word)
    while i<lp and j<lw:
        if pat[i]==word[j]:
            i += 1
            j += 1
        elif pat[i] == '*':
            tmp = word[j]
            i += 1
            while i<lp and pat[i] == tmp:
                i += 1
            j += 1
            while j<lw and word[j] == tmp:
                j += 1
        else:
            return False
    return True

pat = 'he*o'
word = 'hello'
pat1 = 'a*p'
word1 = 'apple'

print match(pat1,word1)
