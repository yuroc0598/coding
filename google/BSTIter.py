#!/usr/bin/python3

class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BSTIter(object):
    def __init__(self,root):
        self.root = root
        self.lst = []
        if root:
            self.lst.append(root)
            while root.left:
                self.lst.append(root.left)
                root = root.left

    def Next(self):
        cur = self.lst.pop()
        ans = cur.val
        if cur.right:
           tmp = cur.right
           while tmp:
                self.lst.append(tmp)
                tmp = tmp.left
        return ans
            
    def hasNext(self):
        return len(self.lst)>0

n1 = Node(3)
n2 = Node(1)
n3 = Node(5)
n4 = Node(4)
n5 = Node(2)
n6 = Node(6)


n1.left = n2
n1.right = n3
n4.left = n5
n4.right = n6


def merge1(root1,root2):
    iter1 = BSTIter(root1)
    iter2 = BSTIter(root2)
    ans = []
    if not iter1.hasNext():
        while iter2.hasNext():
            ans.append(iter2.Next())
        print(ans)
    
    if not iter2.hasNext():
        while iter1.hasNext():
            ans.append(iter1.Next())
        print(ans)
    
    v1,v2 = iter1.Next(),iter2.Next()
    if v1<v2:
        flag = 1
        ans.append(v1)
    else:
        flag = 2
        ans.append(v2)
    
    while (flag==1 and iter1.hasNext()) or (flag==2 and iter2.hasNext()):
        if flag==1:
            v1 = iter1.Next()
        else:
            v2 = iter2.Next()
        print("compare between %d and %d\n" %(v1,v2))
        if v1<v2:
            flag = 1
            ans.append(v1)
        else:
            flag = 2
            ans.append(v2)
    
    if flag == 1:
        print("remaining v2 is %d\n" % v2)
        ans.append(v2)
        while iter2.hasNext():
            ans.append(iter2.Next())
    
    if flag == 2:
        print("remaining v1 is %d\n" % v1)
        ans.append(v1)
        while iter1.hasNext():
            ans.append(iter1.Next())
           
    return ans


def merge(root1,root2):
    ans = []
    if not root1 and not root2:
        return ans
    if not root1:
        iter2 = BSTIter(root2)
        while iter2.hasNext():
            ans.append(iter2.Next())
        return ans
    if not root2:
        iter1 = BSTIter(root1)
        while iter1.hasNext():
            ans.append(iter1.Next())
        return ans
    iter1 = BSTIter(root1)
    iter2 = BSTIter(root2)
    ans = []
    v1,v2 = iter1.Next(),iter2.Next()
    flag = 0
    while True:
        if v1 < v2:
            ans.append(v1)       
            if iter1.hasNext():
                v1 = iter1.Next()
            else:
                flag = 1
                break
        else:
            ans.append(v2)
            if iter2.hasNext():
                v2 = iter2.Next()
            else:
                flag = 2
                break

    if flag == 1:
        while True:
            ans.append(v2)
            if iter2.hasNext():
                v2 = iter2.Next()
            else:
                break
    if flag == 2:
        while True:
            ans.append(v1)
            if iter1.hasNext():
                v1 = iter1.Next()
            else:
                break

    return ans

print merge1(n1,n4)
print merge(n1,n4)
