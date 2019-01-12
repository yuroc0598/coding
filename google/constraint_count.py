#!/usr/bin/python3
from math import factorial

def C_num(a,b):
    return factorial(a)/(factorial(b)*factorial(a-b))

def constraint_count(n,x,y):# n is number of total chars, x num of a, y num of b, using 'a''b''c'
    res = 0
    for nx in range(x+1):
        for ny in range(y+1):
            nc = n-nx-ny
            res += C_num(n,nx)*C_num(n-nx,ny)

    return int(res)


print(constraint_count(4,1,2))

