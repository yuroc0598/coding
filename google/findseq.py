#!/usr/bin/python3

class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def findSeq(root):
    ans = [0]
    def helper(node,seq):
        if not node:
            return ans[0]
        if node.left:
            helper(node.left,seq*10+node.val)
        if node.right:
            helper(node.right,seq*10+node.val)
        if not node.left and not node.right:
            ans[0] += seq*10+node.val
    helper(root,0)
    return ans[0]

n1 = Node(6)
n2 = Node(3)
n3 = Node(5)
n4 = Node(2)
n5 = Node(5)
n6 = Node(4)
n7 = Node(7)
n8 = Node(4)
        
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n5.left = n7
n5.right = n8
n3.right = n6


print(findSeq(n1))
