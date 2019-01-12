# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderIter(node,p):
    if node:
        if node.left and node.val>p.val:
            leftV = inorderIter(node.left,p)
            if leftV:
                return leftV
        if node.val > p.val:
            return node
        if node.right and node.val<p.val:
            rightV = inorderIter(node.right,p)
            if rightV:
                return rightV
        return None




n1 = TreeNode(5)
n2 = TreeNode(1)
n3 = TreeNode(6)
n4 = TreeNode(4)
n5 = TreeNode(3)
n1.left = n2
n1.right = n3
n2.right = n4
n4.left = n5

inorderIter(n1,n5)
