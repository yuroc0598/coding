# leetcode LRU cache, use double linked list and hashmap, perform get and  put both in O(1) time

class Node(object):
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None
 

class LRUCache(object):

   
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.map = {} # {key:node}
        self.cap = capacity
        self.len = 0
     
    def remove_node(self,node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def append_node(self,node):
        node.pre = self.tail.pre
        node.next = self.tail
        node.pre.next = node
        node.next = self.tail
        
    def update_node(self,node):
        self.remove_node(node)
        self.append_node(node)
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        curNode = self.map[key]
        self.update_node(curNode)
        return curNode.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        
        if key in self.map:
            curNode = self.map[key]
            curNode.val = value
            self.update_node(curNode)
        else:
            curNode = Node(key,value)
            if self.len<self.cap:
                self.map[key] = curNode
                self.append_node(curNode)
                self.len += 1
            else:
                evictNode = self.head.next
                evictKey = evictNode.key
                del self.map[evictKey]
                self.remove_node(evictNode)
                self.append_node(curNode)
                self.map[key] = curNode
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


