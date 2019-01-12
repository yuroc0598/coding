class BuildingPoint(object):

    def __init__(self, point, is_start, height):
        self.point = point;
        self.is_start = is_start
        self.height = height
        
    def __lt__(self, other):
        if self.point != other.point:
            return self.point < other.point
        else:
            if self.is_start:
                h1 = -self.height
            else:
                h1 = self.height

            if other.is_start:
                h2 = -other.height;
            else:
                h2 = other.height

            return h1 < h2
    
def get_skyline(buildings):

    building_points = []
    for building in buildings:
        building_points.append(BuildingPoint(building[0], True, building[2]))
        building_points.append(BuildingPoint(building[1], False, building[2]))
    for item in building_points:
        print item.point, item.is_start,item.height

    building_points = sorted(building_points)
    for item in building_points:
        print item.point, item.is_start,item.height
    queue = {}
    queue[0] = 1
    prev_max_height = 0
    result = []
    for building_point in building_points:
        if building_point.is_start:
            if building_point.height in queue:
                queue[building_point.height] = queue[building_point.height] + 1
            else:
                queue[building_point.height] = 1
    
        else:
            if queue[building_point.height] == 1:
                del queue[building_point.height]
            else:
                queue[building_point.height] = queue[building_point.height] - 1

        current_max_height = max(queue.keys())

        if prev_max_height != current_max_height:
            result.append([building_point.point, current_max_height])
            prev_max_height = current_max_height
    return result

if __name__ == '__main__':
    buildings = [[1,2,1],[1,2,2],[1,2,3]]
    print(get_skyline(buildings))
