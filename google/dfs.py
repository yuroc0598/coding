#!/usr/bin/python3


class Node(object):
    def __init__(self,val):
        self.val = val
        self.nb = []




def dfs(n1,seen):
    if n1 not in seen:
        seen.add(n1)
        print(n1.val)
        for k in n1.nb:
            dfs(k,seen)

def topo(n1,seen,stack):
    if n1 not in seen:
        seen.add(n1)
        for k in n1.nb:
            topo(k,seen,stack)
        stack.append(n1)

def main():
    n1 = Node(5)
    n2 = Node(4)
    n3= Node(2)
    n4 = Node(0)
    n5 = Node(1)
    n6 = Node(3)

    n1.nb = [n3,n4]
    n2.nb = [n4,n5]
    n3.nb = [n6]
    n6.nb = [n5]

    seen = set()
    graph = [n1,n2,n3,n4,n5,n6]
    print("dfs results:\n")
    for node in graph:
        dfs(node,seen)
    seen = set()
    stack = []
    print("topo results:\n")
    for node in graph:
        topo(node,seen,stack)
    while stack:
        print(stack.pop().val)

if __name__ == '__main__':
    main()
