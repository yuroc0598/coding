# leetcode 353, snake game

from collections import deque
class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.food = map(tuple,food[::-1])
        self.width = width
        self.height = height
        self.curL = 1
        self.occupy = deque()
        self.occupy.append((0,0))
        self.set = set() 
        self.set.add((0,0))
        self.head = (0,0)
        

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        if direction == 'U':
            newi,newj = self.head[0]-1,self.head[1]
        elif direction == 'L':
            newi,newj = self.head[0],self.head[1]-1
        elif direction == 'R':
            newi,newj = self.head[0],self.head[1]+1
        else:
            newi,newj = self.head[0]+1,self.head[1]
        if newi<0 or newj<0 or newi>=self.height or newj >= self.width:
            return -1
        if (newi,newj) in self.set-set([self.occupy[-1]]): 
            #print set(self.occupy[-1])
            #print newi,newj
            #print self.occupy
            #print self.set
            return -1
        
        self.head = (newi,newj)
        if not self.food or (newi,newj) != self.food[-1]: 
            to_remove = self.occupy.pop()
            self.set.remove(to_remove)
            self.occupy.appendleft((newi,newj))
            #print "add {},{}".format(newi,newj)
            self.set.add((newi,newj))
            
            #print self.occupy
            #print self.set
            #print to_remove
            #print "remove {}".format(to_remove)
            
            #print self.set
            
        else:
            self.occupy.appendleft((newi,newj))
            self.set.add((newi,newj))
            self.curL += 1
            self.food.pop()
        
        return self.curL-1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
