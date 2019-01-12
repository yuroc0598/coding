#!/usr/bin/python3
import sys
import time
def modular_exp(x,y,p):
    if p == 0:
        print("invalid p")
        return
    if x == 1 or y == 0:
        return 1

    x = x%p
    ref = [x]
    seen = set(ref)
    nex = (x*x)%p
    while nex not in seen:
        ref.append(nex)
        seen.add(nex)
        nex = (nex*x)%p
    L = len(ref)
    y = y%L
    return ref[y-1]
def m2(x,y,p):
    x = x%p
    ans = 1
    while y:
        if y&1:
           ans = (x*ans)%p
        y = y>>1
        x = (x*x)  %p
    return ans

if __name__ == '__main__':
    x,y,p =  list(map(int,list(sys.argv[1:])))
    t1 = time.time()
    print(modular_exp(x,y,p))
    t2 = time.time()
    print(m2(x,y,p))
    t3 = time.time()
    print(t2-t1,t3-t2)
