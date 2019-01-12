import sys
class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def reverseBetween(head,m,n):
    if m==n:
        return head
    leftB,start = None,head
    for i in xrange(m-1):
        leftB = start
        start = start.next
    # pre is now left break point
    pre = None
    bk = start
    for i in xrange(n-m+1):
        pos = start.next
        start.next = pre
        pre = start
        start = pos
    # start is now the right breakpoint, pre is the new head of middle part
    if leftB:
        leftB.next = pre    
        bk.next = start
        return head
    else:
        bk.next = start
        return pre

def printList(head):
    ant = head
    while ant:
        print ant.val
        ant = ant.next
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
m = int(sys.argv[1])
n = int(sys.argv[2])
printList(n1)
print "from {} to {}".format(m,n)
new = reverseBetween(n1,m,n)
printList(new)
