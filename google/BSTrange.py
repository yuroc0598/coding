#!/usr/bin/python


def count_range_node(root,a,b):
    c = [0]
    def helper(node):
        if not node:
            return 0
        if root.val > a:
            helper(node.left)
        if a<= node.val <=b:
            c[0] += 1
        if root.val < b:
            helper(node.right)    
    helper(root)
    return c[0]


class  Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


n1 = Node(10)
n2 = Node(5)
n3 = Node(50)
n4 = Node(1)
n5 = Node(40)
n6 = Node(100)


n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n5
n3.right = n6


print count_range_node(n1,5,45)
