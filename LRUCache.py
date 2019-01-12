from collections import deque
class LRUCache(object):
	def __init__(self,capacity):
		self.capacity = capacity
		self.time_queue = deque()
		self.value_dict = {}
		
	def update_time(self,key,needPop):
		self.time_queue.append(key)
		if needPop:
			return self.time_queue.popleft()

	def get(self,key):
		if not key in self.value_dict:
			return -1
		self.update_time(key,0)	
		return self.value_dict[key]

	def put(self,key,value):
		if key in self.value_dict:
			self.update_time(key,0)
			self.value_dict[key] = value
			return
		self.value_dict[key] = value
		if len(self.value_dict)-1 < self.capacity:
			self.update_time(key,0,0)
		else:
			key_remove = self.update_time(key,1)
			self.value_dict.pop(key_remove,None)
			






if __name__ == '__main__':
    test = LRUCache(2)
    test.put(1,1)
    test.put(2,2)
    test.get(1)
    test.put(3,3)
    test.get(2)
    test.put(4,4)
    test.get(1)
    test.get(3)
    test.get(4)
    

