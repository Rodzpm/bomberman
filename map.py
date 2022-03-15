from random import randint

class MapGenerator:
    def __init__(self,width,height,scale,spawn_rate):
        self.size = (width,height)
        self.scale = scale
        self.spawn_rate = spawn_rate
        self.block_size = (self.scale/100*self.size[0],self.scale/100*self.size[1])
    def generate_map(self):
        map = []
        for i in range(self.scale):
            map.append([])
            for j in range(self.scale):
                r = randint(1,self.spawn_rate)
                if r == 1:
                    map[i].append(1)
                else:
                    map[i].append(0)
        return map

                


