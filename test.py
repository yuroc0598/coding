#!/usr/bin/env python

def func(a,c):
    if c == 10:
        return
    a.append(c)
    func(a,c+1)

nums = []
func(nums,0)
print nums
