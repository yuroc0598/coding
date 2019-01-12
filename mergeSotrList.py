#!/usr/bin/env python

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeTwoLists(self,l1,l2):	
		if not l1:
			return l2
		if not l2:
			return l1

		if l1.val >= l2.val:
			l1,l2 = l2,l1

		p1, p2 = l1, l2
		
		while p1 and p2:
			while p1.next and p1.next.val < p2.val:
				p1 = p1.next
			if not p1.next:
				p1.next = p2
				return l1
			while p2.next and p2.next.val < p1.next.val:
				p2 = p2.next
			new_l2 = p2.next
			p2.next = p1.next
			p1.next = l2
			p1 = p2.next
			l2 = new_l2
			p2 = new_l2
			if not p2:
				return l1



if __name__ == '__main__':
	s = Solution()
	l10=ListNode(1)
	l11=ListNode(2)
	l12=ListNode(4)
	l20=ListNode(1)
	l21=ListNode(3)
	l22=ListNode(4)

	l30=ListNode(5)
	
	l40=ListNode(4)
	
	l10.next = l11
	l11.next = l12

	l20.next = l21
	l21.next = l22

	result = s.mergeTwoLists(l10,l30)
	while result:
		print result.val
		result = result.next
		

