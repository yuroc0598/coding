#!/usr/bin/env python


a={1:'a',2:'b',3:'c'}

for key in a.keys():
    del a[key]

print a
