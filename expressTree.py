#!/usr/bin/env python
import sys
import re

class node(object):
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None

def createTree(root):
    if not root.val:
        return 
    L = len(root.val)
    
    if set(['+','-','*','/']).intersection(set(list(root.val))):
        foundPlus = False
        for i in range(L):
            if root.val[i] in ['+','-']:
                if i > L-1:
                    print "invalid expression +/- occurs in root value:{} and index:{}".format(root.val, i)
                    return
                foundPlus = True
                root.left = node(root.val[:i])
                root.right = node(root.val[i+1:])
                root.val = root.val[i]
                print "found +/- and new node val is {}, left val is {}, right val is {}".format(root.val,root.left.val,root.right.val)
                break
        if not foundPlus:
            for i in range(L):
                if root.val[i] in ['*','/']:
                    if i> L-1:
                        print "invalid \* or \/"
                        return
                    foundTime = True
                    root.left = node(root.val[:i])
                    root.right = node(root.val[i+1:])
                    root.val = root.val[i]
                    break

        createTree(root.left)
        createTree(root.right)
        return root

               
def inOrder(root):
    if root:
        inOrder(root.left)
        print root.val
        inOrder(root.right)

def calTree(root):
    op = ['+','-','*','/']
    if root.val not in op:
        return int(root.val)
    else:
        valueL = calTree(root.left)
        valueR = calTree(root.right)
        if root.val == '+':
            root.val = valueL + valueR
        elif root.val == '-':
            root.val = valueL - valueR
        elif root.val == '*':
            root.val = valueL * valueR
        else:
            root.val = valueL / valueR
        root.left, root.right  = None,None
        return root.val
                
   
def calString(s):
    # remove *// first:
    op = ['+','-','*','/']
    while '*' in s:
        ind_star = s.find('*')
        curNum = ''
        for i in range(ind_star-1,-1,-1):
            if s[i] not in op:
                curNum = s[i] + curNum
            else:
                break
                # s[i] now is in op
        if i == 0:
            i=-1
        leftV = int(curNum)
        curNum = ''
        for j in range(ind_star+1,len(s)):
            if s[j] not in op:
                curNum = curNum + s[j]
            else:
                break
                # s[j] now is in op
        if j == len(s) -1:
            j = len(s)
        rightV = int(curNum)

        # calc:
        print "in *, left v is {}, right V is {}".format(leftV, rightV)
        tmp_result = leftV*rightV
        # replace
        s = s[:i+1] + str(tmp_result) + s[j:]
    while '/' in s:
        ind_star = s.find('/')
        curNum = ''
        for i in range(ind_star-1,-1,-1):
            if s[i] not in op:
                curNum = s[i] + curNum
            else:
                break
                # s[i] now is in op
        if i == 0:
            i = -1
        leftV = int(curNum)
        curNum = ''
        for j in range(ind_star+1,len(s)):
            if s[j] not in op:
                curNum = curNum + s[j]
            else:
                break
                # s[j] now is in op
        if j == len(s) -1 :
            j = len(s)
        rightV = int(curNum)

        # calc:
        print "in /, left v is {}, right V is {}".format(leftV, rightV)
        tmp_result = leftV/rightV
        # replace
        s = s[:i+1] + str(tmp_result) + s[j:]

    print "after calc * and /: %s" %s
    # now only +/-, take all as number, if starts with -, neg value
    curNum, stack  = '', []
    for i in range(len(s)):
        if s[i] not in op:
            curNum = curNum + s[i]
        if s[i] == '+':
            stack.append(int(curNum))
            curNum = ''
        if s[i] == '-':
            stack.append(int(curNum))
            curNum = '-'
    stack.append(int(curNum))
    
    return sum(stack)        

def calc(s):
    stack = re.findall('\((.*?)\)',s)
    if  stack:
        for ele in stack:
            print "part result: %d" % calString(ele)

def main():
    s = sys.argv[1]
    #root = node(s)
    #newR = createTree(root)
    ## verify tree by inorder traversal
    #print "start inOrder traversal:"
    #inOrder(newR)
    #print "start calc:"
    #calTree(newR)
    #print "traverse the calculated tree"
    #inOrder(newR)
    #print "result is %s" % newR.val
    print "the result is %d" % calc(s)

if __name__ == '__main__':
    main()
