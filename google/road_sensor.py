# given a rectangle area representing a road, and a list of sensors with (x,y,r) as its location and radius. can the car pass the road?

class Radar(object):
	def __init__(self,x,y,r):
		self.x = x
		self.y = y
		self.r = r
		self.top = y+r
		self.bot = y-r

class unionFind(object):
	def __init__(self,array):
		self.cap = len(array)
		self.parent = {}
		for ele in array:
			self.parent[ele] = ele
	

	def find(self,rd):
		if self.parent[rd] != rd:
			self.parent[rd] = self.find(self.parent[rd])
		return self.parent[rd]

	def union(self,r1,r2):
		p1,p2 = self.find(r1),self.find(r2)
		if p1 == p2: return
		self.parent[p2] = p1
		p1.top = max(p1.top,p2.top)
		p1.bot = min(p1.bot,p2.bot)
		

def road_sensor(road,sensors):
	# road is defined as topleft coordinate and rightbot cord, M:[], N:[], sensor is a list of class radar
	U, D = road
	radars = []
	for x,y,r in sensors:
		tmp = Radar(x,y,r)
		radars.append(tmp)
	UF = unionFind(radars)
	L = len(radars)
	for i in xrange(L):
		for j in xrange(i+1,L):
			if (radars[i].x - radars[j].x)**2 + (radars[i].y-radars[j].y)**2 <= (radars[i].r + radars[j].r)**2:
				UF.union(radars[i],radars[j])

	for radar in radars:
		if UF.parent[radar] == radar:
			if radar.top >= U and radar.bot <= D: 
				#print radar.x,radar.y,UF.parent[radar].x,UF.parent[radar].y, UF.parent[radar].top,UF.parent[radar].bot
				return False
	return True

sensors = [[2,2,2],[2,5,1],[2,7,1],[2,9,0.9]]
print road_sensor([10,4],sensors)
