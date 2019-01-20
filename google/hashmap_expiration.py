# design a hash map to store task that will expire. Two cases: the expiration is global to all tasks, or each task has its own expiration

# suppose we have a class Task

_EXPIRATION = 32

class Task(object):
    def __init__(self,key,data,create_time,exp = _EXPIRATION):
        self.key = key
        self.data = data
        self.ctime = create_time
        self.exp = exp

# (key,task):

# design three functions: 
# add_task: add task into hashmap
# get_task: get taskf from hashmap, if expired, return None
# cleanup: remove the tasks in hashmap that have already expirated


# case 1, global expiration. design circular array


class HASHEXP(object):
    def __init__(self,cap):
        self.cir_map = {}
        self.cap = cap
    def add_task(self,task):
        key = task % self.cap
        self.cir_map[key] = [task,task.ctime]
    def get_task(self,key):
        keymod = key%self.cap
        if keymod not in self.cur_map:
            return None
        task, taskexp = self.cir_map[keymod][0],self.cir_map[keymod][1]
        if time.time() - task.ctime > taskexp:
            del self.cir_map[keymod]
            return None
        # if time update is required: task.ctime = time.time()
        return task
    def cleanup(self):
        for key in self.cir_map.keys():
            task,taskexp  = self.cir_map[key]
            if time.time()-task.ctime > taskexp:
                del self.cir_map[key]
        
            



# case 2, expiration is unique to each task, hashmap + double linked list, similar to LRU cache
