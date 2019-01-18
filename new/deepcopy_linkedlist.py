# leetcode 138, deep copy of a linked list with additional random pointer, key idea is to build a map between old node and new node, and iter twice for nex and rand

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        newhead = RandomListNode(head.label)
        ant_org = head
        ant_new = newhead
        nodemap = {head:newhead}
        while ant_org.next:
            newnode = RandomListNode(ant_org.next.label)
            
            ant_new.next = newnode
            ant_org = ant_org.next
            ant_new = ant_new.next
            nodemap[ant_org] = ant_new
        ant_org = head
        ant_new = newhead
        while ant_org:
            if ant_org.random:
                ant_new.random = nodemap[ant_org.random]
            ant_org = ant_org.next
            ant_new = ant_new.next
        return newhead
